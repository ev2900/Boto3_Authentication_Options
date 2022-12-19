import boto3

credentials = boto3.Session().get_credentials()

# Optional - use credentials from a specific profile
# credentials = boto3.Session(profile_name='<profile-name>').get_credentials() # ex. credentials = boto3.Session(profile_name='profile-2').get_credentials()

# print(credentials.access_key)
# print(credentials.secret_key)

session = boto3.Session(
	aws_access_key_id=credentials.access_key,
    aws_secret_access_key=credentials.secret_key
)

# Example S3 client to check if the session auth is working
client = session.client('s3')