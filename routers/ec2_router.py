from services.ec2_service import ec2_instance_info
from fastapi import APIRouter
#from schemas.ec2_schema import EC2InstanceResponse

router = APIRouter()

@router.get("/ec2/inventory")

def get_instance_inventory():
    instance_inventory = ec2_instance_info()
    return instance_inventory


