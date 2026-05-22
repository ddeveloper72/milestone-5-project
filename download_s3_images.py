"""Download error page images from S3 bucket"""
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
print(f"Region: {region}")

# Create S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=region
)

# Create img directory if it doesn't exist
img_dir = 'static/img'
os.makedirs(img_dir, exist_ok=True)

print(f"\nConnecting to S3 bucket: {bucket_name}")

# Download the error images from static/img/ path
files_to_download = [
    ('static/img/404error.jpeg', '404error.jpeg'),
    ('static/img/500error.jpg', '500error.jpg'),
]

for s3_key, filename in files_to_download:
    local_path = os.path.join(img_dir, filename)
    
    try:
        print(f"Downloading {s3_key} -> {local_path}")
        s3.download_file(bucket_name, s3_key, local_path)
        print(f"✓ Successfully downloaded {filename}")
    except Exception as e:
        print(f"✗ Failed to download {filename}: {e}")

print("\nDone!")
