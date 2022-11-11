import boto3

session = boto3.session.Session(region_name="us-east-1")

dynamodb = session.resource("dynamodb")

table = dynamodb.Table("amopps-tech-students")

# print(table.creation_date_time)
# print()
# print(table.table_arn)

def lambda_handler(event, context):
    response = table.put_item( 
        Item = {
            "StudentId":"03",
            "StudentName":"Yomi",
            "Age": 23,
            "Country":"US"
        }
    )

    print("Response of item insertion: ", response)