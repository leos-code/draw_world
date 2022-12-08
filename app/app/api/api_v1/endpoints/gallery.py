from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import Field
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.schemas.response import Response

router = APIRouter()

# @router.get("/list", response_model=List[schemas.GalleryBase])
@router.get("/creative/gallery/{page}/{pageSize}")
def gallery_list(
    db: Session = Depends(deps.get_db),
    page: int = 0,
    pageSize: int = 20,
) -> Any:
    """
    Retrieve items.
    """
    skip = (page - 1) * pageSize
    if skip < 0:
        skip = 0
    limit = pageSize
    if limit > 20:
        limit = 20
    items = crud.gallery_crud.get_gallery_list(db, skip=skip, limit=limit)
    return Response(data=items) 


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
    item_in.user_id = current_user.id
    item = crud.gallery_crud.generate_image(db, item_in)
    return item

@router.get("/prompt/list/{page}/{pageSize}")
def get_prompts_list(page:int = Field(ge=0), pageSize: int = Field(ge=10), db: Session = Depends(deps.get_db)):
    skip = pageSize 
    limit = (page - 1) * pageSize
    data = crud.crud_gallery.gallery_crud.get_prompts_list(db, skip, limit)
    return data

    
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
    return artist_list


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
    return style_list
    
