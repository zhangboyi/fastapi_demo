#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2020/12/3 8:40 下午
# @Author:boyizhang

'''
status
msg
data
pageNum
pageSize
total
'''
from numbers import Number
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from app.db.base_class import Base

ModelType = TypeVar('ModelType', bound=Base)


# StatusType = TypeVar('StatusType',type=int)
class CustomResponseBase(Generic[ModelType]):
    def __init__(self, status: int = 200 ,msg="msg", model: List[Type[ModelType]] =None,pagenum: int = 0, pagesize = 10):
        self.model = model
        self.status = status
        self.pagesize = pagesize
        self.pagenum = pagenum
        self.msg = msg

    def returnData(self):
        return {"status": self.status, "model": self.model}

    def mulData(self):
        return {
            "status": self.status,
            "msg": self.msg,
            "model": self.model,
            "pagenum": self.pagenum,
            "pagesize": self.pagesize

        }
    def returnError(self):
        return {
            "status":self.status,
            "msg": self.msg
        }
