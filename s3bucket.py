#%%
import boto3
from dotenv import load_dotenv
import os
#%%
# Load environment variables from .env file
load_dotenv()
#%%
# S3 bucket login credentials
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
#%%
# Check if AWS credentials are set
if not aws_access_key_id or not aws_secret_access_key:
    print("AWS credentials are not set in the environment variables.")
    raise SystemExit("AWS credentials are required to proceed.")
#%%
# Connect to S3
try:
    s3_client = boto3.client('s3',
                             region_name='eu-north-1',
                             aws_access_key_id=aws_access_key_id,
                             aws_secret_access_key=aws_secret_access_key)
    print('Connection to S3 made successfully.')
except Exception as e:
    print(f"Error connecting to S3: {e}")
    raise
#%%
# Create a new bucket for the project
bucket_name = 'financial-pipeline'
try:
    s3_client.create_bucket(Bucket=bucket_name,
                            CreateBucketConfiguration={'LocationConstraint': 'eu-north-1'})
    print(f"Bucket '{bucket_name}' created successfully.")
except s3_client.exceptions.BucketAlreadyOwnedByYou:
    print(f"Bucket '{bucket_name}' already exists and is owned by you.")
except s3_client.exceptions.BucketAlreadyExists:
    print(f"Bucket '{bucket_name}' already exists and cannot be created.")
    raise
except Exception as e:
    print(f"Error creating bucket: {e}")
    raise
#%%
# Upload files to the bucket
files_to_upload = [
    ('Dataset/Fraudulent_E-Commerce_Transaction_Data_2.csv', 'Fraudulent_E-Commerce_Transaction_Data_2.csv'),
    ('Dataset/Fraudulent_E-Commerce_Transaction_Data.csv', 'Fraudulent_E-Commerce_Transaction_Data.csv')
]
#%%
for local_path, s3_key in files_to_upload:
    try:
        s3_client.upload_file(Filename=local_path, Bucket=bucket_name, Key=s3_key)
        print(f"File '{local_path}' uploaded to bucket '{bucket_name}' as '{s3_key}'.")
    except Exception as e:
        print(f"Error uploading file '{local_path}' to bucket '{bucket_name}': {e}")
        raise
#%%

