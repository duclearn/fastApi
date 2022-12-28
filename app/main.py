from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from .router import user, post, vote
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins=["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def get_hello():
    return {"message": "hello"}

app.include_router(user.router)
app.include_router(post.router)
app.include_router(vote.router)




