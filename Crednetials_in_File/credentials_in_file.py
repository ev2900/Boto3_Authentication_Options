import boto3

credentials = boto3.Session().get_credentials()

# access_key = credentials.access_key
# secret_key = credentials.secret_key

# print(access_key)
# print(secret_key)

session = boto3.Session(
	aws_access_key_id=credentials.access_key,
    aws_secret_access_key=credentials.secret_key
)

# Example S3 client to check if the session auth is working
client = boto3.client('s3')