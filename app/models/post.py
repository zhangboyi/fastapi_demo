#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2020/12/2 8:58 下午
# @Author:boyizhang
from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String


from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401

class posts(Base):
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(223))