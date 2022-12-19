import boto3

session = boto3.Session(
    aws_access_key_id="<access_key_id>",
    aws_secret_access_key="<secret_access_key>"
)

# Example S3 client to check if the session auth is working
s3 = session.client('s3')