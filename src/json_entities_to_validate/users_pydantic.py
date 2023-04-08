from pydantic import BaseModel, validator, Field
from typing import Dict, Any


class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class SupportData(BaseModel):
    url: str
    text: str


class ResponseGetUserValidator(BaseModel):
    data: UserData
    support: SupportData

    class Config:
        """
        Запрещаем дополнительные поля
        """
        extra = "forbid"


    # @validator("id")
    # def check_that_id_is_less_than_two(cls, v):
    #     if v > 2:
    #         raise ValueError('Id is not less than two')
    #     else:
    #         return v

