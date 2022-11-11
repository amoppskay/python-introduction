import boto3

session = boto3.session.Session(region_name="us-east-1", profile_name="default")

ec2 = session.resource("ec2")

response = ec2.create_instances(
    ImageId = "ami-026b57f3c383c2eec",
    InstanceType = "t2.micro",
    MaxCount = 2,
    MinCount = 2
)

print(response)

# client = session.client('ec2')
#
# response = client.describe_instances(
#     Filters=[ #filter for specific matches eg tags, instance type, ami, etc
#         {
#             'Name': 'tag:env',
#             'Values': [
#                 'prod',
#             ]
#         },
#     ]
#
# )
# # print(response)
#
# # print(response ["Reservations"])
#
# # print(response ["Reservations"][0]["Instances"][0])
#
# # print()
#
# # print(response ["Reservations"][0]["Instances"][0] ["InstanceId"])
# # print()
#
# # print(response ["Reservations"][0]["Instances"][1] ["InstanceId"])
#
# # instance_id = (response ["Reservations"][0]["Instances"][0] ["InstanceId"])
# # instance_id = (response ["Reservations"][0]["Instances"][1] ["InstanceId"])
# # print(instance_id)
# # print()
#
# # stop_response = client.stop_instances(
# #     InstanceIds = [
# #         instance_id
# #     ]
#
# # )
#
# # print(stop_response)
#
# instance_id = (response ["Reservations"][0]["Instances"][0] ["InstanceId"])
# instance_id = (response ["Reservations"][0]["Instances"][1] ["InstanceId"])
# print(instance_id)
# print()
#
# terminate_response = client.terminate_instances(
#     InstanceIds = [
#         instance_id
#     ]
#
# )
#
# print(terminate_response)

