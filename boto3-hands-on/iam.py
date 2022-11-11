import boto3

iam = boto3.resource("iam")

all_users = iam.users.all()
for each_user in all_users:
    print(each_user)
    print(each_user.create_date, each_user.name, each_user.arn, each_user.user_id, each_user.path, each_user.user_name)
print()

iam_user = iam.create_user(
    UserName = "yellow-flower",
    PermissionsBoundary="arn:aws:iam::aws:policy/AmazonEC2FullAccess",
    Tags = [
        {
            'Key': "team",
            'Value': "dev"
        },
    ]
)
print(iam_user)
