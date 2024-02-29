from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app = FastAPI()


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@app.get('/')
def welcome():
    return "welcome to fast-api "


@app.get("/welcome/{name}")  # path parameter
def getId(name):
    d = {"name": name, 'age': 23}
    return d


@app.get("/blog/all",
         tags=['blog'],
         summary="This will retrieve all blogs",
         description="This api call simulates fetching all blogs",
         response_description="The list of all available blogs")
def get_all_blog():
    return {"details": "All blogs are provided"}


@app.get("/blog/{id}", tags=['blog'])
def getBlog(identity: int):  # Type validation
    return {"details": f" hi your blog id is {identity}"}


# predefined path

@app.get("/blog/type/{type}", tags=['blog'])
def get_blog_type(types: BlogType):
    return {"message": f"Blog type {types}"}


# query parameter: http://127.0.0.1:8000/page?page=1&page_size=10

@app.get("/page")
def get_pages(page=1, page_size: Optional[int] = None):
    return {"message": f" All  {page_size} blogs On page {page}"}


@app.get('/blog/{id}/comments/{comment_id}', tags=['comments'])
def get_comment(identity: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    simulates retrieving a comment of blog

    - **id** mandatory parameter
    - **comment_id** mandatory parameter
    - **valid** Optional query parameter
    - **username** Optional query parameter

    """
    return {"message": f"blog_id {identity} , comment {comment_id},valid {valid}, username {username}"}


# status code

@app.get("/status/{id}", status_code=status.HTTP_404_NOT_FOUND)
def get_status(identity: int, response: Response):
    if identity < 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f" blog  id {identity} not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f" blog with id {identity}"}


"""
Router : 
from fastapi import ApiRouter
router = ApiRouter(prefix='/blog' ,tags=['/blog'])
@router.get("/")


from router import blog
app = FastAPI()
app.include_router(blog.router)
"""


"""
import uvicorn
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def index():
   return {"message": "Hello World"}
if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
"""
