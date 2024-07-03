from sqlalchemy import Integer, String, \
    Column, DateTime, VARCHAR, Boolean
from datetime import datetime

from settings import Base


class Shop(Base):
    __tablename__ = 'shops'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(128), nullable=False)
    description = Column(String, nullable=False)
    address = Column(String, nullable=True)
    inn = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.now())
    modified_at = Column(DateTime, default=datetime.now())
    is_active = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)
    is_confirmed = Column(Boolean, default=False)
