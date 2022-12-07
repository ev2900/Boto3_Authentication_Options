import boto3

session = boto3.Session(
    aws_access_key_id="<access_key_id>",
    aws_secret_access_key="<secret_access_key>"
)

client = boto3.client('s3')