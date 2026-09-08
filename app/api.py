## This contains all the initializing code like api creation

from fastapi import FastAPI
from router import hello_endpoint, metrics_endpoint, s3_endpoint, ec2_endpoint, ebs_endpoint, sec_grp

app = FastAPI(
        title= "Internal DevOps Utility API",
        description="This is an Internal API Utility for monitoring System Metrics, AWS usage and log analysis",
        version="1.0.0",
        doc_url="/docs",
        redoc="/redoc"
        )


app.include_router(hello_endpoint.router)
app.include_router(metrics_endpoint.router)
app.include_router(s3_endpoint.router, prefix="/aws")
app.include_router(ec2_endpoint.router, prefix="/aws")
app.include_router(ebs_endpoint.router, prefix="/aws")
app.include_router(sec_grp.router, prefix="/aws")
