from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth # pip install opensearch-py
import boto3

host = 'xmpe2i0b2vtisb1ie8if.us-east-1.aoss.amazonaws.com'
region = 'us-east-1'

credentials = boto3.Session(profile_name='profile-2').get_credentials()

auth = AWSV4SignerAuth(credentials, region)

index_name = 'movies'

client = OpenSearch(
    hosts = [{'host': host, 'port': 443}],
    http_auth = auth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)

q = 'miller'

query = {
  'size': 5,
  'query': {
    'multi_match': {
      'query': q,
      'fields': ['title^2', 'director']
    }
  }
}

response = client.search(
    body = query,
    index = index_name
)

print(response)