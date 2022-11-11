import boto3

session = boto3.session.Session(region_name="us-east-1", profile_name="default")

# print(dir(boto3)) # fxns supported by boto3

# Let's use Amazon S3
s3_resource = session.resource("s3") # called s3 resource from boto3 and stored it in 's3' variable

# Print out bucket names
# for bucket in s3.buckets.all():
#     print(bucket.name)

# Upload a new file
# data = open("aws-course-details.txt", "rb")
# s3.Bucket("amps-state-files").put_object(Key="aws-course-details.txt", Body=data)

print(dir(s3_resource))

buckets_list = s3_resource.buckets.all()
print(buckets_list)
print()
# print(dir(buckets_list))
for x in buckets_list:
    # print(x) # all buckets on my console are listed
    # print(dir(x)) # all attributes that are supported
    print(x.name)
