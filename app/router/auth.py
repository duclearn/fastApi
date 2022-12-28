from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, models, Units
from sqlalchemy.orm import Session
from ..database import get_db
from ..OAuth2 import create_access_token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm


router = APIRouter(tags=["Authentication"])


@router.post("/login")
#def user_login(user_credential: schemas.UserLogin, db: Session = Depends(get_db)):
def user_login(user_credential: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#    user = db.query(models.User).filter(models.User.email == user_credential.email).first()

    user = db.query(models.User).filter(models.User.email == user_credential.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credential")
    if not Units.verify(user_credential.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credential")
    print(user.id)

    access_token = create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "beare"}

    #return {"token": "example token"}


