import boto3
import requests
from requests_aws4auth import AWS4Auth

credentials = boto3.Session().get_credentials()

awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, 'us-east-1', 's3')

response = requests.get("http://s3-us-east-1.amazonaws.com", auth=awsauth)

#print(response.text)