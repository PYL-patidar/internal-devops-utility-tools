## This service for aws cli monitoring logic hold

import boto3
from datetime import datetime, timezone, timedelta

def get_buckets():
    s3_client = boto3.client("s3")

    buckets = s3_client.list_buckets()["Buckets"]
    
    new_buckets = []
    old_buckets = []
    current_date = datetime.now(timezone.utc).astimezone()
    days_ago_90 = current_date - timedelta(days=90) 

    print(current_date)
    print(days_ago_90)

    for bucket in buckets:
        bucket_name = bucket["Name"]
        creation_date = bucket["CreationDate"]

        if creation_date < days_ago_90:
            old_buckets.append(bucket_na00me)
        else:
            new_buckets.append(bucket_name)

    return {
            "Total_buckets":len(buckets),
            "new_buckets" : len(new_buckets),
            "old_buckets" : len(old_buckets),
            "new_buckets_name" : new_buckets,
            "old_buckets_name" : old_buckets
            }
