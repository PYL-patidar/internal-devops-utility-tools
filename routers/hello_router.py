from services.greet_service import hello
from fastapi import APIRouter

router = APIRouter()
@router.get("/hello")
def greeting():

    message = hello()
    return message
