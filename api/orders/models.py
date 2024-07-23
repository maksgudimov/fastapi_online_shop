from pydantic import BaseModel, field_validator


class CreateOrder(BaseModel):

    user_id: int
    shop_id: int
    product_id: int
    payed: bool = False
    is_active: bool = True
    status: str = 'New'
    accept: bool = False

    @field_validator('status')
    @classmethod
    def validate_status(cls, value):
        if value != 'New':
            raise ValueError("Order must be New")
        return value
