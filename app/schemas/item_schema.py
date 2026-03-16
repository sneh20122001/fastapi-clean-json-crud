from pydantic import BaseModel, Field

class ItemBase(BaseModel):
    name : str = Field(..., min_length=2, max_length=50, description="The name of the item")
    description : str = Field(..., min_length=5, max_length=200, description="A brief description of the item")
    price : float = Field(..., gt=0, description="The price of the item, must be greater than 0")

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id : int
    