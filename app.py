from fastapi import FastAPI
from router import blog_get, blog_post, user, article, product, file
from db import models
from db.database import engine
from exception import StoryException
from fastapi import Request
from fastapi.responses import JSONResponse
from auth import authentication
from fastapi.staticfiles import StaticFiles
from templates import templates

# from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(templates.router)
app.include_router(authentication.router)
app.include_router(file.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(product.router)


@app.exception_handler(StoryException)
def StoryException_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={"message": exc.name}
    )


models.Base.metadata.create_all(engine)

origins = ['http://127.0.0.1:3000']
# app.add_middleware(
#     CORSMiddleware,
#     allow_origin=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_header=["*"]
# )

app.mount('/file', StaticFiles(directory='file'), name='file')
