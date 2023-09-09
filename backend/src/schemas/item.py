from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ItemModel(BaseModel):
    name: str
    created_at: Optional[datetime]


class ItemGet(BaseModel):
    id: str
    name: str
    created_at: Optional[datetime]


class ItemList(BaseModel):
    items: list[ItemGet]
