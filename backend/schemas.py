from pydantic import BaseModel
from typing import List, Optional

class ProductionMediaSchema(BaseModel):
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
    media: List[ProductionMediaSchema]
    primary_image: Optional[str]