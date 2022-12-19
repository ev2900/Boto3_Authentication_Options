# Credentials in File
An AWS user's access key id and secret value can configure a boto3 session **without** hard coding the values in the python script. Instead the boto3 session can be configured from the *credentials* file created as part of the AWS CLI configuration. 

1. [Install the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

2. Configure the AWS CLI. Run ```aws configure``` and follow the prompts

You now have a *.aws* folder that has *credentials* file. This file stores the aws_access_key_id and aws_secret_access_key which can be accessed via. boto3. 

The example [credentials_in_file.py](https://github.com/ev2900/Boto3_Authentication_Options/blob/main/Credentials_in_File/credentials_in_file.py) demonstrates
