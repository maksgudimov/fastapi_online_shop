from fastapi import APIRouter, HTTPException, status, Response
from models.orders import Order
from models.products import Product
from .models import CreateOrder
from order_processing.send import send_order
from settings import session


router = APIRouter()


@router.post("/api/orders")
async def create_order(order: CreateOrder, status_code=status.HTTP_201_CREATED):
    send_order(order=dict(order))
    return Response(status_code=status.HTTP_201_CREATED)
