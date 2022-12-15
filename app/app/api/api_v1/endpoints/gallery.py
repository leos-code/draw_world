from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import Field
from sqlalchemy.orm import Session
from pathlib import Path 

from app import crud, models, schemas
from app.api import deps
from app.schemas.response import Response
from googletrans import Translator
from app.third_party import generate

router = APIRouter()
translator = Translator()

# @router.get("/list", response_model=List[schemas.GalleryBase])
@router.get("/creative/gallery")
def gallery_list(
    db: Session = Depends(deps.get_db),
    type: int = 1,
    page: int = 0,
    size: int = 20,
) -> Any:
    """
    Retrieve items.
    """
    skip = (page - 1) * size
    if skip < 0:
        skip = 0
    limit = size
    if limit > 20:
        limit = 20
    items = crud.gallery_crud.get_gallery_list(db, skip=skip, limit=limit)
    result = {"total": 60, "items":items}
    return Response(data=result) 


@router.post("/creative/generate")
def generate_image(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.gallery.GalleryCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new item.
    """
    prompt = item_in.prompt
    # detect_res = translator.detect(item_in.prompt)
    # if detect_res.lang != "en":
    #     trans_result = translator.translate(item_in.prompt, src="zh-CN", dest="en")
    #     prompt_en = trans_result.text
    #     item_in.prompt_en = prompt_en
    #     prompt = prompt_en
    # else:
        # item_in.prompt_en = prompt
    item_in.prompt_en = prompt

    #排队生成
    gen_res = generate.generate(prompt)
    img_file = gen_res[0]
    img_path_obj = Path(img_file)
    img_url = "https://api.xuexirust.com/image/" + img_path_obj.name
    # img_url = ""

    #insert
    item_in.user_id = current_user.id
    item_in.stat = 1
    item_in.img_url = img_url 
    result = crud.gallery_crud.generate_image(db, item_in)
    if result:
        return Response(msg="ok", data={"img_url": img_url})
    else:
        return Response(code=-1, msg="服务异常")

@router.get("/prompt/list")
def get_prompts_list(page:int = 1, size: int = 10, db: Session = Depends(deps.get_db)):
    skip = size
    limit = (page - 1) * size
    data = crud.crud_gallery.gallery_crud.get_prompts_list(db, skip, limit)
    return Response(data=data)

    
@router.get("/creative/artist_list")
def get_artist_list():
    artist_list = [
      {
        "id": 63,
        "name": "国好通深"
      },
      {
        "name": "石际器适",
        "id": 77
      },
      {
        "id": 69,
        "name": "则月今按非行"
      },
      {
        "name": "权然合用向东",
        "id": 53
      }
    ]
    return Response(data=artist_list)


@router.get("/creative/style_list") 
def get_style_list():
    style_list = [
      {
        "name": "头在算长构新",
        "id": 69
      },
      {
        "id": 66,
        "name": "受技九算品"
      },
      {
        "id": 94,
        "name": "治即听解级话"
      }
    ]
    return Response(data=style_list)
    
