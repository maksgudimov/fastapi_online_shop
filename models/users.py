import uuid
from sqlalchemy import Integer, String, \
    Column, DateTime, VARCHAR, Boolean, UUID
from datetime import datetime

from settings import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    unique_id = Column(UUID, unique=True, default=uuid.uuid4, nullable=False)
    username = Column(VARCHAR(256), nullable=False)
    first_name = Column(VARCHAR(128), nullable=False)
    last_name = Column(VARCHAR(128), nullable=False)
    middle_name = Column(VARCHAR(128), nullable=True)
    phone = Column(VARCHAR(10), unique=True, nullable=False)
    email = Column(String, unique=True, nullable=True)
    birthday_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    modified_at = Column(DateTime, default=datetime.now())
    is_active = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)
