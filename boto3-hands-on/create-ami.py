# file to create AMI and copy to other region
import time

from urllib import response

import boto3

session = boto3.session.Session(profile_name = "default", region_name="us-east-1")

client = session.client('ec2')

instances = client.describe_instances(
     Filters=[
        {
            'Name': 'tag:Env',
            'Values': [
                'Prod',
            ]
        },
    ]
)
images_list = []
for i in instances['Reservations']:
    for j in i['Instances']:
        print(j['InstanceId'], j['Tags'][0]['Value'])
        response = client.create_image(
            InstanceId= j['InstanceId'],
            Name=j['Tags'][0]['Value']
        )
        print(response)
        images_list.append(response['ImageId'])

time.sleep(280)

for image in images_list:
    copy_response = client.copy_image(
            Description='Copy example',
            Name=image,
            SourceImageId=image,
            SourceRegion='us-west-1',
            )

    print(copy_response)