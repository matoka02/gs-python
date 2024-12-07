import uuid
from pydantic import BaseModel, Field
from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass


class ImageProcessingOptions(BaseModel):
    resize: Optional[str] = Field(None, description="Example: 1980x1200")
    convert_to: Optional[str] = Field(None, description="png, jpg, webp")
    grayscale: Optional[str] = Field(None, description="Convert to grayscale")
    flip: Optional[str] = Field(None, description="horizontal or vertical")


