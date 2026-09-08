# This service is for identify uattached volume

import boto3 

def get_unattach_volume():
    ec2_client = boto3.client("ec2", region_name="ap-south-1")

    response = ec2_client.describe_volumes()

    attached_volume_list = []
    unattached_volume_list = []
    total_volume_list = []
    
    for vol_data in response["Volumes"]:
        volume = {
                "volumeId": vol_data["VolumeId"],
                "Size": vol_data["Size"],
                "State": vol_data["State"],
                "CreateTime": vol_data["CreateTime"],
                "AvailabilityZone" : vol_data["AvailabilityZone"]
                }

        total_volume_list.append(volume)
        
        if volume["State"] == "in-use":
            attached_volume_list.append(volume)
        elif volume["State"] == "available":
            unattached_volume_list.append(volume)
        else:
            pass

    return { "Total volume": len(total_volume_list),
            "Total attached_volumes": len(attached_volume_list),
            "Total unattached_volumes": len(unattached_volume_list),
            "Attached volumes" : attached_volume_list,
            "Unattached volumes" : unattached_volume_list
            }




    
