import boto3

session = boto3.session.Session(region_name="us-east-1", profile_name="default")

s3 = session.client("s3")

# Example to copy a file path (single object at a time)
# response = s3.copy_object(
#     Bucket = "amps-boto3-02",  # destination bucket
#     CopySource = "amps-boto3-01/Monisola Ogunsina Resume.docx",  # use the path of the object
#     Key = "Monisola Ogunsina Resume.docx" # put a name for the object copied into the other bucket, use the original name or rename it

# )
# print(response)

# Example to copy a folder path (single object at a time)
# response = s3.copy_object(
#     Bucket = "amps-boto3-01",  # destination bucket
#     CopySource = "amps-boto3-02/k8s/data.txt",  # use the path of the object
#     Key = "amopps.txt" # put a name for the object copied into the other bucket, use the original name or rename it

# )
# print(response)

# Example to copy objects with multiple folders/files at a time

bucket_objects = s3.list_objects_v2( #listing all the objects in the bucket
    Bucket = "amps-boto3-02"  # destination bucket
    )

for b in bucket_objects["Contents"]: #iterating the bucket content one after the other
    # print("S3 Obejct:", b["Key"])

    print("Source to copy: ", "amps-boto3-01/" + b["Key"])

    response = s3.copy_object(
        Bucket = "amps-boto3-02",  # destination bucket
        CopySource = "amps-boto3-01/" + b["Key"],  # use the path of the object
        Key = b["Key"]) # put a name for the object copied into the other bucket, use the original name or rename it
    print(response)
    