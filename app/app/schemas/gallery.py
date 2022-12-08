from typing import Optional

from pydantic import BaseModel


# Shared properties
class GalleryBase(BaseModel):
    img_url: Optional[str] = ""
    prompt: str
    user_id: Optional[int] = 0
    size: Optional[str] = ""
    artist: Optional[str] = ""
    style: Optional[str] = ""
    stat: Optional[int] = 0
    is_show: Optional[int] = 0
    model_name: Optional[str] = ""


# Properties to receive on item creation
class GalleryCreate(GalleryBase):
    pass


# Properties to receive on item update
class GalleryUpdate(GalleryBase):
    pass

