#!/bin/bash
# Heroku Deployment Script for Custom Drone Django App

echo "🚀 Deploying Custom Drone Django App to Heroku"

# Check if Heroku CLI is installed
if ! command -v heroku &> /dev/null; then
    echo "❌ Heroku CLI not found. Please install Heroku CLI first."
    echo "Download from: https://devcenter.heroku.com/articles/heroku-cli"
    exit 1
fi

# Check if user is logged in to Heroku
if ! heroku auth:whoami &> /dev/null; then
    echo "🔑 Please log in to Heroku first:"
    heroku login
fi

# App name (change this to your desired app name)
APP_NAME="custom-drone-ddeveloper72"

echo "📱 Creating Heroku app: $APP_NAME"

# Create Heroku app (if it doesn't exist)
heroku create $APP_NAME --region us || echo "App might already exist, continuing..."

# Add PostgreSQL addon
echo "🐘 Adding PostgreSQL database..."
heroku addons:create heroku-postgresql:essential-0 --app $APP_NAME || echo "PostgreSQL might already be added"

# Set environment variables from .env file
echo "⚙️  Setting environment variables from .env file..."

if [ ! -f .env ]; then
    echo "❌ .env file not found. Please create one with your credentials."
    exit 1
fi

# Load environment variables
set -a
source .env
set +a

heroku config:set DEBUG=False --app $APP_NAME
heroku config:set SECRET_KEY="$SECRET_KEY" --app $APP_NAME

# AWS Configuration
heroku config:set AWS_ACCESS_KEY_ID="$AWS_ACCESS_KEY_ID" --app $APP_NAME
heroku config:set AWS_SECRET_ACCESS_KEY="$AWS_SECRET_ACCESS_KEY" --app $APP_NAME
heroku config:set AWS_STORAGE_BUCKET_NAME="$AWS_STORAGE_BUCKET_NAME" --app $APP_NAME
heroku config:set AWS_S3_REGION_NAME="$AWS_S3_REGION_NAME" --app $APP_NAME
heroku config:set USE_S3=True --app $APP_NAME

# Azure SQL Configuration (backup database)
heroku config:set AZURE_SQL_HOST="$AZURE_SQL_HOST" --app $APP_NAME
heroku config:set AZURE_SQL_NAME="$AZURE_SQL_NAME" --app $APP_NAME
heroku config:set AZURE_SQL_USER="$AZURE_SQL_USER" --app $APP_NAME
heroku config:set AZURE_SQL_PASSWORD="$AZURE_SQL_PASSWORD" --app $APP_NAME
heroku config:set AZURE_SQL_PORT="$AZURE_SQL_PORT" --app $APP_NAME
heroku config:set AZURE_SQL_SCHEMA="$AZURE_SQL_SCHEMA" --app $APP_NAME

# Stripe Configuration
heroku config:set STRIPE_PUBLISHABLE="$STRIPE_PUBLISHABLE" --app $APP_NAME
heroku config:set STRIPE_SECRET="$STRIPE_SECRET" --app $APP_NAME

# Email Configuration
heroku config:set EMAIL_ADDRESS="$EMAIL_ADDRESS" --app $APP_NAME
heroku config:set EMAIL_PASSWORD="$EMAIL_PASSWORD" --app $APP_NAME

# Disable collectstatic during build (we'll use S3)
heroku config:set DISABLE_COLLECTSTATIC=1 --app $APP_NAME

echo "🔧 Environment variables set successfully!"

# Add git remote (if not already added)
git remote add heroku https://git.heroku.com/$APP_NAME.git 2>/dev/null || echo "Heroku remote already exists"

echo "✅ Heroku app setup complete!"
echo "📋 Next steps:"
echo "1. git add ."
echo "2. git commit -m 'Deploy to Heroku'"
echo "3. git push heroku master"
echo "4. heroku run python manage.py migrate --app $APP_NAME"
echo "5. heroku run python manage.py createsuperuser --app $APP_NAME"
echo ""
echo "🌐 Your app will be available at: https://$APP_NAME.herokuapp.com"