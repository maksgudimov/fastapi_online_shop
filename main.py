from fastapi import FastAPI
from api.orders.views import router as orders_router


app = FastAPI()


app.include_router(orders_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
