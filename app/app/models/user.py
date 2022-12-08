from typing import TYPE_CHECKING

from sqlalchemy import Column, DateTime, Integer, SmallInteger, String, text
from sqlalchemy.ext.declarative import declarative_base

from app.db.base_class import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, server_default=text("nextval('users_id_seq'::regclass)"))
    name = Column(String(255), nullable=False)
    profile_url = Column(String(255), nullable=False)
    credits = Column(Integer, nullable=False, server_default=text("0"), comment='信用分')
    gender = Column(SmallInteger, nullable=False, server_default=text("1"))
    city = Column(String(64), nullable=False, server_default=text("''::character varying"))
    province = Column(String(64), nullable=False, server_default=text("''::character varying"))
    country = Column(String(64), nullable=False, server_default=text("''::character varying"))
    openid = Column(String(256), nullable=False, server_default=text("''::character varying"))
    unionid = Column(String(256), nullable=False, index=True, server_default=text("''::character varying"))
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))