## This contains all the initializing code like api creation

from fastapi import FastAPI
from routers import hello_router, metrics_router, s3_router, ec2_router, ebs_router, sec_grp_router

app = FastAPI(
        title= "Internal DevOps Utility API",
        description="This is an Internal API Utility for monitoring System Metrics, AWS usage and log analysis",
        version="1.0.0",
        doc_url="/docs",
        redoc="/redoc"
        )


app.include_router(hello_router.router)
app.include_router(metrics_router.router)
app.include_router(s3_router.router, prefix="/aws")
app.include_router(ec2_router.router, prefix="/aws")
app.include_router(ebs_router.router, prefix="/aws")
app.include_router(sec_grp_router.router, prefix="/aws")
