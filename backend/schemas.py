from pydantic import BaseModel
from typing import List, Optional

class ProductMediaSchema(BaseModel):
    media_url: str
    is_primary: bool
    position: int

class CategorySchema(BaseModel):
    id: int
    name: str

class ProductSchema(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str]
    categories: List[str]
    media: List[ProductMediaSchema]
    primary_image: Optional[str]