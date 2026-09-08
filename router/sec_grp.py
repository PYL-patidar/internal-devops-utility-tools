## This is the router or endpoint for security group

from services.security_group import security_group_audit
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/security_group/risky", status_code=200)
def security_group():
    sec_grp_info = security_group_audit()
    return sec_grp_info

#except:
#    raise HTTPException(
#                status_code=500,
#                detail= "Internal Server Error")

