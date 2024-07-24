import uuid
from sqlalchemy import Table, Integer, \
    Column, DateTime, ForeignKey, Boolean, UUID
from datetime import datetime

from sqlalchemy.orm import relationship

from settings import Base


order_product = Table('order_product', Base.metadata,
                      Column('order_id', Integer(), ForeignKey("orders.id")),
                      Column('product_id', Integer(), ForeignKey("products.id"))
                      )


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    unique_id = Column(UUID, unique=True, default=uuid.uuid4, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    shop_id = Column(Integer, ForeignKey('shops.id'))
    product = relationship("Product", secondary=order_product, backref="orders")
    payed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now())
    modified_at = Column(DateTime, default=datetime.now())
    is_active = Column(Boolean, default=False)
