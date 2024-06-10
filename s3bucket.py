#%%
import boto3
from dotenv import load_dotenv
import os
import datetime

#%%
# constants
load_file = 'logs/logfile.txt'
time_format = '%Y-%m-%d %H:%M:%S'
bucket_name = 'financial-pipeline'
files_to_upload = [
    ('Dataset/Fraudulent_E-Commerce_Transaction_Data_2.csv', 'Fraudulent_E-Commerce_Transaction_Data_2.csv'),
    ('Dataset/Fraudulent_E-Commerce_Transaction_Data.csv', 'Fraudulent_E-Commerce_Transaction_Data.csv')
]
#%%
# Load environment variables from .env file
load_dotenv()
#%%
# implementing logging

def logging(message):
    now = datetime.datetime.now()
    timestamp = now.strftime(time_format)
    with open(load_file, 'a') as f:
        f.write(f"{timestamp} {message}\n")
#%%
# S3 bucket login credentials
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
#%%
# Check if AWS credentials are set
if not aws_access_key_id or not aws_secret_access_key:
    logging("AWS credentials are not set in the environment variables.")
    raise SystemExit("AWS credentials are required to proceed.")
#%%
# Connect to S3
try:
    s3_client = boto3.client('s3',
                             region_name='eu-north-1',
                             aws_access_key_id=aws_access_key_id,
                             aws_secret_access_key=aws_secret_access_key)
    logging('Connection to S3 made successfully.')
except Exception as e:
    logging(f"Error connecting to S3: {e}")
    raise
#%%
# Create a new bucket for the project
try:
    s3_client.create_bucket(Bucket=bucket_name,
                            CreateBucketConfiguration={'LocationConstraint': 'eu-north-1'})
    logging(f"Bucket '{bucket_name}' created successfully.")
except s3_client.exceptions.BucketAlreadyOwnedByYou:
    logging(f"Bucket '{bucket_name}' already exists and is owned by you.")
except s3_client.exceptions.BucketAlreadyExists:
    logging(f"Bucket '{bucket_name}' already exists and cannot be created.")
    raise
except Exception as e:
    logging(f"Error creating bucket: {e}")
    raise
#%%
# upload files to s3 bucket
for local_path, s3_key in files_to_upload:
    try:
        s3_client.upload_file(Filename=local_path, Bucket=bucket_name, Key=s3_key)
        logging(f"File '{local_path}' uploaded to bucket '{bucket_name}' as '{s3_key}'.")
    except Exception as e:
        logging(f"Error uploading file '{local_path}' to bucket '{bucket_name}': {e}")
        raise
#%%
# List objects in the bucket
try:
    response = s3_client.list_objects_v2(Bucket=bucket_name, MaxKeys=3)
    logging(f"List of objects in bucket '{bucket_name}': {response.get('Contents', [])}")
except Exception as e:
    logging(f"Error listing objects in bucket '{bucket_name}': {e}")
    raise
