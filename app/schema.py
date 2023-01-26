from typing import Any, Dict, Optional, Type
from errors import ApiError
from pydantic import BaseModel, ValidationError, validator


class CreateAdv(BaseModel):

    title: str
    descr: str
    user_id: int
    password: str

    @validator('title')
    def check_title(cls, value: str):
        if len(value) > 10:
            raise ValueError('too long title')
        return value

    @validator('descr')
    def check_descr(cls, value: str):
        if len(value) > 200:
            raise ValueError('too long descr')
        return value


class PatchDelAdv(BaseModel):

    title: Optional[str]
    descr: Optional[str]
    user_id: int
    password: str

    @validator('title')
    def check_title(cls, value: str):
        if len(value) > 10:
            raise ValueError('too long title')
        return value

    @validator('descr')
    def check_descr(cls, value: str):
        if len(value) > 200:
            raise ValueError('too long descr')
        return value


SCHEMA_TYPE = Type[CreateAdv] | Type[PatchDelAdv]


def validate(model_cls: SCHEMA_TYPE, data: Dict[str, Any], exclude_none: bool = True) -> dict:
    try:
        validated = model_cls(**data)
        return validated.dict(exclude_none=exclude_none)
    except ValidationError as er:
        raise ApiError(400, er.errors())
