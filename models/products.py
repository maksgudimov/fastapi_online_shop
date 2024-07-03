from sqlalchemy import Integer, String, \
    Column, ForeignKey, VARCHAR, DECIMAL

from settings import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    shop_id = Column(Integer, ForeignKey('shops.id'))
    name = Column(VARCHAR(256), nullable=False)
    description = Column(String, nullable=True)
    price = Column(DECIMAL, nullable=False)
    discount = Column(Integer, default=0)
    image_url = Column(String, nullable=True)
