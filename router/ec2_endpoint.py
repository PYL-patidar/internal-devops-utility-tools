from services.ec2 import ec2_instance_info
from fastapi import APIRouter

router = APIRouter()

@router.get("/ec2/inventory")
def get_instance_inventory():
    instance_inventory = ec2_instance_info()
    return instance_inventory


