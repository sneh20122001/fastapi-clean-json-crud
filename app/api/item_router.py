from fastapi import APIRouter
from typing import List

from app.services.item_service import *
from app.schemas.item_schema import *

router = APIRouter(prefix="/items", tags=["Items"])

service = ItemService()

@router.get("/", response_model=List[ItemResponse])
def get_items():
    return service.get_items()

@router.get("/{id}", response_model=ItemResponse)
def get_item(id: int):
    return service.get_item(id)

@router.post("/", response_model=ItemResponse, status_code=201)
def create_item(item: ItemCreate):
    return service.create_item(item.dict())

@router.put("/{id}", response_model=ItemResponse)
def update_item(id: int, item: ItemUpdate):
    return service.update_item(id, item.dict())

@router.delete("/{id}", response_model=ItemResponse)
def delete_item(id: int):
    return service.delete_item(id)