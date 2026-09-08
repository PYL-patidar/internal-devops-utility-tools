# This is the endpoint for ebs service\

from services.ebs import get_unattach_volume
from fastapi import APIRouter

router = APIRouter()

@router.get("/ebs/unattached")
def unattached_volume():
    
    volumes = get_unattach_volume()
    
    return volumes

