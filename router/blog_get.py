from fastapi import APIRouter
from enum import Enum
from typing import Optional

router = APIRouter(prefix='/blog', tags=['blog'])


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@router.get("/all",
            summary="This will retrieve all blogs",
            description="This api call simulates fetching all blogs",
            response_description="The list of all available blogs")
def get_all_blog():
    return {"details": "All blogs are provided"}


@router.get("/{id}", tags=['blog'])
def getBlog(identity: int):  # Type validation
    return {"details": f" hi your blog id is {identity}"}


# predefined path

@router.get("/type/{types}")
def get_blog_type(types: BlogType):
    return {"message": f"Blog type {types}"}


@router.get('/{id}/comments/{comment_id}', tags=['comments'])
def get_comment(identity: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    simulates retrieving a comment of blog

    - **id** mandatory parameter
    - **comment_id** mandatory parameter
    - **valid** Optional query parameter
    - **username** Optional query parameter

    """
    return {"message": f"blog_id {identity} , comment {comment_id},valid {valid}, username {username}"}
