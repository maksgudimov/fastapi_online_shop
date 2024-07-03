from sqlalchemy import Integer, \
    Column, DateTime, VARCHAR, Boolean
from datetime import datetime

from settings import Base


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(128), nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    is_active = Column(Boolean, default=False)
