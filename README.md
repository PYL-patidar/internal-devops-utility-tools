# Internal DevOps Utility API
A Python-based internal DevOps utility API for system monitoring and AWS resource analysis.  

The Project converts common DevOps tasks into simple REST API endpoints using Python, `psutil`, and `boto3`.

## Aims
This project aims to provide useful internal DevOps utilities through simple REST APIs.

* 🖥️ System Monitoring — CPU, memory, disk usage and system status
* ☁️ S3 Analysis — Identify buckets older than 90 days
* 🖥️ EC2 Inventory — Retrieve important EC2 instance details
* 💾 EBS Analysis — Analyze attached and unattached volumes
* 🔐 Security Group Audit — Identify publicly exposed inbound rules

## 🏗️ Project Structure
```
internal-devops-utility-tools/
│
├── app/ │
    └── api.py 
├── routers/ 
│   ├── metrics_router.py 
│   ├── s3_router.py 
│   ├── ec2_router.py  
│   ├── ebs_router.py    
│   └── sec_grp_router.py  
├── services/   
│   ├── metrics_service.py 
│   ├── s3_service.py  
│   ├── ec2_service.py 
│   ├── ebs_service.py 
│   └── sec_grp_service.py 
├── main.py 
├── requirements.txt 
└── README.md
```

## 🛠️ Tech Stack
* Python
* FastAPI
* Uvicorn
* psutil
* boto3

## Usage

### Clone the repository

git clone <https://github.com/PYL-patidar/internal-devops-utility-tools.git cd internal-devops-utility-tools>  

### Create virtual environment  

python3.14 -m venv venv  

#### Activate it:

source venv/bin/activate  

### install the requirements  

pip install -r requirements.txt  

### run the application  

python main.py  

#### The API will be available at 

http://localhost:8000

## 📌 Project Status

Future improvements may include better testing, logging, authentication, and additional AWS automation.

