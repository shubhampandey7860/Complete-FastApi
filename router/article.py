from fastapi import APIRouter, Depends
from schema import ArticleDisplay, ArticleBase
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article
from auth.Oauth2 import *
from schema import UserBase

router = APIRouter(prefix="/article", tags=["article"])


# Create article
@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_article.create_article(db, request)


# Get specific article
@router.get('/{id}')  # response_model=ArticleDisplay
def get_article(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return {
        'data': db_article.get_article(db, id),
        'current_user': current_user
    }


@router.get("/all", response_model=ArticleDisplay)
def get_all_article(db: Session = Depends(get_db)):
    return db_article.get_all_articles(db)
