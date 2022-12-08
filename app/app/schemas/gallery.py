from typing import Optional

from pydantic import BaseModel


# Shared properties
class GalleryBase(BaseModel):
    img_url: Optional[str] = None
    prompt: str
    user_id: Optional[int] = None
    size: Optional[str] = None
    artist: Optional[str] = None
    style: Optional[str] = None
    stat: int = 0
    is_show: int = 0
    model_name: Optional[str] = None


# Properties to receive on item creation
class GalleryCreate(GalleryBase):
    pass


# Properties to receive on item update
class GalleryUpdate(GalleryBase):
    pass

