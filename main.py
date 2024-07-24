from fastapi import FastAPI
from api.orders.views import router as orders_router
from order_processing.rbmq import connect_rabbit

app = FastAPI()


app.include_router(orders_router)


connection, channel = connect_rabbit()


@app.get("/")
async def root():
    return {"message": "Hello World"}
