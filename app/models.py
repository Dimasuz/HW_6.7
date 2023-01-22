import atexit
import uuid
from typing import Type

import config
# from cachetools import cached
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy_utils import EmailType

from config import PG_DSN

engine = create_engine(PG_DSN)
Base = declarative_base(bind=engine)


class User(Base):

    __tablename__ = "ads_users"

    id = Column(Integer, primary_key=True)
    email = Column(EmailType, unique=True, index=True)
    password = Column(String(60), nullable=False)


class Adv(Base):

    __tablename__ = "advertisements"

    id = Column(Integer(), primary_key=True)
    title = Column(String(50), nullable=False)
    descr = Column(String(200),  nullable=False)
    creat_time = Column(DateTime, server_default=func.now())
    user_id = Column(Integer, ForeignKey("ads_users.id", ondelete="CASCADE"))


Base.metadata.create_all()
Session = sessionmaker(bind=engine)

atexit.register(engine.dispose)
