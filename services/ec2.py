## This is for ec2 instance Inventory i.e. instance ID, IP, state, type

import boto3

def ec2_instance_info():
    ec2_client = boto3.client("ec2", region_name='ap-south-1')
    response = ec2_client.describe_instances()
    
    instance_info = []
    
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            data= {
                    "InstanceId" : instance["InstanceId"],
                    "Name" : instance["Tags"][0]["Value"],
                    "InstanceType" : instance["InstanceType"],
                    "State" : instance["State"]["Name"],
                    "Public IP" : instance.get("PublicIpAddress"),
                    "Availability Zone" : instance["Placement"]["AvailabilityZone"],
                    "Key Name" : instance.get("KeyName")
                    }
            instance_info.append(data)

    return {
            "Total instances": len(instance_info),
            "Instance_info" : instance_info}
