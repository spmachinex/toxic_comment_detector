from fastapi import  APIRouter, Depends
from ..schemas import Comment
from ..dependencies import check_toxicity

router = APIRouter(prefix=
                   "/comments", tags=["comments"])

@router.post("/")
async def check_toxic_comment(comment: Comment):
    return  check_toxicity(comment)