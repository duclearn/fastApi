from fastapi import APIRouter, Depends, HTTPException, status
from .. import models, Units, schemas
from ..database import get_db
from sqlalchemy.orm import Session
from ..OAuth2 import OAuth2PasswordRequestForm, create_access_token


router = APIRouter(
    prefix="/users"
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(**user.dict())
    hash_password = Units.get_password_hash(new_user.password)
    new_user.password = hash_password
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {new_user}

@router.post("/login", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.Token)
def user_loging(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    filter_user = db.query(models.User).filter(user.username == models.User.email).first()
    if not filter_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Inactive User")
    if not Units.verify_password(user.password, filter_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Inactive User")

    access_token = create_access_token(data={"user_id": filter_user.id})

    return {"access_token": access_token,
            "token_type": "Bearer"}