# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, SmallInteger, String, text
from sqlalchemy.ext.declarative import declarative_base

from app.db.base_class import Base

class Gallery(Base):
    __tablename__ = 'gallery'

    id = Column(Integer, primary_key=True, server_default=text("nextval('gallery_id_seq'::regclass)"))
    user_id = Column(Integer, nullable=False, index=True, server_default=text("0"))
    img_url = Column(String(255), nullable=False, server_default=text("''::character varying"))
    prompt = Column(String(4096), nullable=False, server_default=text("''::character varying"))
    size = Column(String(16), nullable=False, server_default=text("''::character varying"))
    artist = Column(String(255), nullable=False, server_default=text("''::character varying"))
    style = Column(String(256), nullable=False, server_default=text("''::character varying"))
    stat = Column(SmallInteger, nullable=False, server_default=text("0"))
    is_show = Column(SmallInteger, nullable=False, server_default=text("0"))
    model_name = Column(String(64), nullable=False, server_default=text("''::character varying"))
    created_at = Column(DateTime, nullable=False, server_default=text("now()"))