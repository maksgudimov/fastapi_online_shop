from fastapi import APIRouter, HTTPException
from .models import CreateOrder
from order_processing.send import create_order


router = APIRouter()


@router.post("/api/orders")
async def create_order(order: CreateOrder):
    print(order)

