from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List
from fastapi import Query, Body

router = APIRouter(prefix='/blog',
                   tags=['blog'])


class BlogModel(BaseModel):
    title: str
    content: str
    number_of_comments: int
    published: Optional[bool] = True


@router.post("/new")
def create_blog(blog: BlogModel):
    return {"data": blog}


@router.post("/new/{id}")
def create_blog1(blog: BlogModel, ide: int, version: int = 1):
    return {"data": blog, 'version': version, 'id': ide}


@router.post("/new/{id}/comment")
def create_comment(blog: BlogModel, ide: int,
                   comment_id: int = Query(None, title='id of comment',
                                           description="Some description for comment_id ",
                                           alias='commentId',
                                           deprecated=True),
                   content: str = Body('Hi how are you'),
                   v: Optional[List[str]] = Query(None)):
    return {'blog': blog, 'id': ide, 'comment_id': comment_id, 'content': content, 'v': v}

    # content : str = Body(...,min_length = 10,regex = 'pattern') or Body(Ellipsis)
    # number validater Path(None , gt = 5,le = 15)
