import boto3

aws_resource = boto3.resource("s3")
bucket = aws_resource.Bucket("rustam-z-bucket")
response = bucket.create(
    ACL='private',
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-central-1'
    },

)

print(response)

"""
ACL='private' means that the bucket can only be accessed by the owner.
ACL='public-read' means that the bucket can be accessed by anyone. But not the files inside.
"""