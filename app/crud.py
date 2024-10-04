# from sqlalchemy.orm import Session
# from app.models import *
# from fastapi import HTTPException
#
#
# # Product CRUD
# def create_product(db: Session, name: str, description: str, price: float, stock_quantity: int):
#     product = Product(name=name, description=description, price=price, stock_quantity=stock_quantity)
#     db.add(product)
#     db.commit()
#     db.refresh(product)
#     return product
#
#
# def get_products(db: Session):
#     return db.query(Product).all()
#
#
# def get_product_by_id(db: Session, product_id: int):
#     return db.query(Product).filter(Product.id == product_id).first()
#
#
# def update_product(db: Session, product_id: int, name: str, description: str, price: float, stock_quantity: int):
#     product = get_product_by_id(db, product_id)
#     if not product:
#         raise HTTPException(status_code=404, detail="Product not found")
#     product.name = name
#     product.description = description
#     product.price = price
#     product.stock_quantity = stock_quantity
#     db.commit()
#     return product
#
#
# def delete_product(db: Session, product_id: int):
#     product = get_product_by_id(db, product_id)
#     if not product:
#         raise HTTPException(status_code=404, detail="Product not found")
#     db.delete(product)
#     db.commit()
#
#
# # Order CRUD
# def create_order(db: Session, order_items: list):
#     # Check stock for each product
#     for item in order_items:
#         product = get_product_by_id(db, item['product_id'])
#         if product.stock_quantity < item['quantity']:
#             raise HTTPException(status_code=400, detail=f"Insufficient stock for product {product.name}")
#
#     # Deduct stock
#     for item in order_items:
#         product = get_product_by_id(db, item['product_id'])
#         product.stock_quantity -= item['quantity']
#
#     # Create order
#     order = Order()
#     db.add(order)
#     db.commit()
#     db.refresh(order)
#
#     # Add order items
#     for item in order_items:
#         order_item = OrderItem(order_id=order.id, product_id=item['product_id'], quantity=item['quantity'])
#         db.add(order_item)
#     db.commit()
#
#     return order
#
#
# def get_orders(db: Session):
#     return db.query(Order).all()
#
#
# def update_order_status(db: Session, order_id: int, status: OrderStatusEnum):
#     order = db.query(Order).filter(Order.id == order_id).first()
#     if not order:
#         raise HTTPException(status_code=404, detail="Order not found")
#     order.status = status
#     db.commit()
#     return order

from sqlalchemy.orm import Session
from . import models, schemas
from typing import List


def create_product(db: Session, name: str, description: str, price: float, stock_quantity: int):
    new_product = models.Product(name=name, description=description, price=price, stock_quantity=stock_quantity)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product



def get_products(db: Session):
    return db.query(models.Product).all()



def get_product_by_id(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()



def update_product(db: Session, product_id: int, name: str, description: str, price: float, stock_quantity: int):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product:
        product.name = name
        product.description = description
        product.price = price
        product.stock_quantity = stock_quantity
        db.commit()
        db.refresh(product)
    return product



def delete_product(db: Session, product_id: int):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product:
        db.delete(product)
        db.commit()



def create_order(db: Session, items: List[schemas.OrderItemCreate]):
    new_order = models.Order()
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order



def get_orders(db: Session):
    return db.query(models.Order).all()



def update_order_status(db: Session, order_id: int, status: str):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if order:
        order.status = status
        db.commit()
        db.refresh(order)
    return order
