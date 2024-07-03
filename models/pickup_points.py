from sqlalchemy import Integer, \
    Column, DateTime, ForeignKey, VARCHAR, Boolean, Time
from datetime import datetime

from settings import Base


class PickUpPoint(Base):
    __tablename__ = 'pickup_points'

    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(Integer, ForeignKey('category.id'))
    name = Column(VARCHAR(256), nullable=False)
    open_at = Column(Time, nullable=False)
    closed_at = Column(Time, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    modified_at = Column(DateTime, default=datetime.now())
    is_active = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)
