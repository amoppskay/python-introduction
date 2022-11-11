import boto3

session = boto3.session.Session(region_name="us-east-1", profile_name="default")

ec2 = session.client("ec2")

# print(dir(ec2)) #all possible fxns supported by ec2

def lambda_handler(event, context):
    volumes = ec2.describe_volumes(
        Filters=[ #go to docs, use the filter
            {
                'Name': "status", #filtering using status
                'Values': [
                    "available", #deleting available EBS vols
                ]
            },
        ],
    )

# print(volumes)
# print()
# print(volumes["Volumes"]) #data is stored in a key called 'Volumes' which is dict[]
# print()

    print("Available Volumes datat:", volumes)

    for v in volumes["Volumes"]: #iterating over each vol in the lsit
        print("EBS Volume:", v["VolumeId"]) #print available EBS vols in the ec2
        response = ec2.delete_volume(
        VolumeId = v["VolumeId"]
        )
        print("Volume delete operation response: ", response)
