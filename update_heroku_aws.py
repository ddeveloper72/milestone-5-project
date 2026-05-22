"""Update Heroku config with new AWS credentials from .env"""
import os
import subprocess

# Read .env file
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
    exit(1)

# Get AWS credentials
aws_access_key = env_vars.get('AWS_ACCESS_KEY_ID')
aws_secret_key = env_vars.get('AWS_SECRET_ACCESS_KEY')

if not aws_access_key or not aws_secret_key:
    print("AWS credentials not found in .env")
    exit(1)

print("Updating Heroku config with new AWS credentials...")

# Update Heroku config
app_name = "ddeveloper72-custom-drone"

commands = [
    f'heroku config:set AWS_ACCESS_KEY_ID={aws_access_key} -a {app_name}',
    f'heroku config:set AWS_SECRET_ACCESS_KEY={aws_secret_key} -a {app_name}',
]

for cmd in commands:
    print(f"\nRunning: {cmd.split('=')[0]}=***")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("✓ Success")
        else:
            print(f"✗ Error: {result.stderr}")
    except Exception as e:
        print(f"✗ Exception: {e}")

print("\nDone!")
