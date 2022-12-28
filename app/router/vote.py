from fastapi import APIRouter, Depends, HTTPException, status
from .. import models, Units, schemas
from ..database import get_db
from sqlalchemy.orm import Session
from ..OAuth2 import OAuth2PasswordRequestForm, create_access_token, get_current_user

router = APIRouter(
    prefix="/vote"
)

@router.post("/", status_code=status.HTTP_202_ACCEPTED)
def vote(vote: schemas.Votes, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    vote_query = db.query(models.Votes).filter(models.Votes.post_id == vote.post_id, models.Votes.user_id == current_user.id)
    found_vote = vote_query.first()
    if vote.dir == 1:
        if not found_vote:
            new_votes = models.Votes(post_id=vote.post_id, user_id=current_user.id)
            db.add(new_votes)
            db.commit()
            return{"new vote": "success"}
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"User already vote for {vote.post_id}")

    if vote.dir == 0:
        vote_query.delete(synchronize_session=False)
        db.commit()
    return {"title": "vote delete success"}