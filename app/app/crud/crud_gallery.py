from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.gallery import Gallery
from app.schemas.gallery import GalleryCreate, GalleryUpdate


class CRUDGallery(CRUDBase[Gallery, GalleryCreate, GalleryUpdate]):
    
    def get_gallery_list(self, db: Session, skip: int, limit: int) -> List[Gallery]:
        return db.query(self.model).where(self.model.is_show == 1).offset(skip).limit(limit).all()

    def generate_image(self, db: Session, item_in:GalleryCreate):
        self.create(db, item_in)


gallery_crud = CRUDGallery(Gallery)
