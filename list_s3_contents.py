"""List contents of S3 bucket"""
import os
import boto3

# Read .env file manually
env_vars = {}
try:
    with open('.env', 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                env_vars[key.strip()] = value.strip()
except FileNotFoundError:
    print("No .env file found")

# Get AWS credentials
aws_access_key = env_vars.get('AWS_ACCESS_KEY_ID')
aws_secret_key = env_vars.get('AWS_SECRET_ACCESS_KEY')
bucket_name = env_vars.get('AWS_STORAGE_BUCKET_NAME')
region = env_vars.get('AWS_S3_REGION_NAME', 'eu-west-1')

print(f"Bucket: {bucket_name}")
print(f"Region: {region}\n")

# Create S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=region
)

print("Listing bucket contents...\n")

try:
    # List all objects in bucket
    response = s3.list_objects_v2(Bucket=bucket_name, MaxKeys=1000)
    
    if 'Contents' in response:
        print(f"Total objects: {len(response['Contents'])}\n")
        for obj in response['Contents']:
            key = obj['Key']
            size = obj['Size']
            print(f"  {key} ({size} bytes)")
    else:
        print("No objects found in bucket")
        
except Exception as e:
    print(f"Error listing bucket: {e}")
