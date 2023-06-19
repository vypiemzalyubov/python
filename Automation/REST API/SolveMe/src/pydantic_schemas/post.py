from pydantic import BaseModel, validator, Field
from typing import List

class PostData(BaseModel):
    author: str
    content: str
    date: str
    id: str
    imageUrl: str
    readMoreUrl: str
    time: str
    title: str
    url: str

class Post(BaseModel):
    category: str
    data: List[PostData]
    success: bool

    @validator("category")
    def check_category(cls, category):
        if category != "startup":
            raise ValueError("Category is not equal startup")
        else:
            return category