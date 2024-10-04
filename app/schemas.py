# from pydantic import BaseModel
# from typing import List, Optional
# from datetime import datetime
# from enum import Enum
#
#
#
# # Order status Enum
# class OrderStatusEnum(str, Enum):
#     in_progress = "in_progress"
#     shipped = "shipped"
#     delivered = "delivered"
#
# # Product schemas
# class ProductBase(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     stock_quantity: int
#
# class ProductCreate(ProductBase):
#     pass
#
# class ProductUpdate(ProductBase):
#     pass
#
# class ProductResponse(ProductBase):
#     id: int
#
#     class Config:
#         orm_mode = True
#
# # OrderItem schemas
# class OrderItemBase(BaseModel):
#     product_id: int
#     quantity: int
#
# class OrderItemCreate(OrderItemBase):
#     pass
#
# class OrderItemResponse(OrderItemBase):
#     id: int
#
#     class Config:
#         orm_mode = True
#
# # Order schemas
# class OrderBase(BaseModel):
#     status: OrderStatusEnum
#
# class OrderCreate(BaseModel):
#     items: List[OrderItemCreate]
#
# class OrderResponse(OrderBase):
#     id: int
#     created_at: datetime
#     items: List[OrderItemResponse]
#
#     class Config:
#         orm_mode = True
#
# class OrderStatusUpdate(BaseModel):
#     status: OrderStatusEnum

from pydantic import BaseModel
from typing import List



class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock_quantity: int


class ProductUpdate(ProductCreate):
    pass


class ProductResponse(ProductCreate):
    id: int

    class Config:
        from_attributes = True
        #orm_mode = True



class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int


class OrderCreate(BaseModel):
    items: List[OrderItemCreate]


class OrderResponse(BaseModel):
    id: int
    items: List[OrderItemCreate]
    status: str

    class Config:
        from_attributes = True
        #orm_mode = True

class OrderStatusUpdate(BaseModel):
    status: str
