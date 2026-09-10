## This service audit risky security gorups 

import boto3

def security_group_audit():

    ec2_client= boto3.client("ec2", region_name="ap-south-1")
    response = ec2_client.describe_security_groups()["SecurityGroups"]
    risky = []

    for data in response:
        for info in data.get( "IpPermissions"):
            protocol = info.get("IpProtocol")
            from_port = info.get("FromPort")
            to_port = info.get("ToPort")


            for ip in info.get("IpRanges"):   
                if ip.get("CidrIp") == "0.0.0.0/0":

                    if from_port == 22:
                        risk = "SSH publicly exposed to the internet"
                    elif from_port == 80:
                        risk = "HTTP publicly exposed to the internet"
                    elif from_port == 443:
                        risk = "HTTPS publicly exposed to the internet"
                    elif from_port == 3306:
                        risk = "RDS publicly exposed to the internet"
                    else:
                        risk = f"{from_port} is publlicly exposed to internet"

                    risky.append({
                        "GroupName": data["GroupName"],
                        "PortRange" : f"{from_port}-{to_port}",
                        "Protocol": protocol,
                        "Source" : ip,
                        "Risk": risk
                        })

    return { "risky inbound rules": risky }
 
