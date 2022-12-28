from fastapi import APIRouter, Depends, HTTPException, status
from .. import models, Units, schemas
from ..database import get_db
from sqlalchemy.orm import Session
from ..OAuth2 import get_current_user
from typing import Optional, List

router = APIRouter(
    prefix="/posts"
)

@router.post("/", status_code=status.HTTP_202_ACCEPTED)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db),
                current_user=Depends(get_current_user)):
    print(current_user.id)
    print(current_user.email)
    post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

@router.get("/", status_code=status.HTTP_202_ACCEPTED, response_model=List[schemas.Post])
def get_post(db: Session = Depends(get_db), limit: int = 10, skip: int = 0, search: Optional[str] = " "):

    posts = db.query(models.Post).filter(models.Post.item.contains(search)).limit(limit).offset(skip).all()
    return posts

@router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED,  )
def delete_post(id: int ,db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    print(post)

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"id {id} not in database")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorised to perform the task")

    post_query.delete(synchronize_session=False)
    db.commit()
    return {"delete": "success"}

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_post(id: int, update_post: schemas.PostBase, db: Session = Depends(get_db),
current_user: int = Depends(get_current_user)):

    post_query = db.query(models.Post).filter(models.Post.id == id) #lenh tuong tu sql
    post_update = post_query.first() # data cua post luu lai trong bo nho
    print(post_update.owner_id) # lay cot owner_id trong data da duoc loc qua lenh post_query
    print(current_user.id) #là id ma cau lenh tren login vao
    if post_update == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"id {id} not in database")
    if post_update.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="user not authorize to do the task")
    post_query.update(update_post.dict(), synchronize_session=False)
    db.commit()
    return {"update": "finish"}



