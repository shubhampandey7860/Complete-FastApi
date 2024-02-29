from db.models import DbArticle
from schema import ArticleBase
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status
from exception import StoryException

def create_article(db: Session, request: ArticleBase):
    if request.content.startswith("Once Upon a time"):
        raise StoryException("No story Please !")
    new_article = DbArticle(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.creator_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def get_article(db: Session, id: int):
    article = db.query(DbArticle).filter(DbArticle.id == id).first()

    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article with id {id} not found")
    return article


def get_all_articles(db: Session):
    return db.query(DbArticle).all()
