from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.schemas.response import Response

router = APIRouter()

# @router.get("/list", response_model=List[schemas.GalleryBase])
@router.get("/list")
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


@router.post("/")
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
