## This is for endpoint or router for aws service

from services.s3_service import get_buckets
from fastapi import APIRouter, HTTPException


router = APIRouter()

@router.get("/s3/old-buckets", status_code=200)
def show_buckets():
    try:
        buckets=get_buckets()
        return buckets
    except:
        raise HTTPException(
                status_code=500,
                detail="Internal Server Error")

    


