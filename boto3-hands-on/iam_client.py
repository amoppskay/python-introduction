import boto3

iam_client = boto3.client("iam")

response = iam_client.list_users()

print(response)
print()

print(response["Users"])
