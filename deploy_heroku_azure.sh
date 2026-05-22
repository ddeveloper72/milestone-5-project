#!/bin/bash
# Heroku Deployment Script for Custom Drone Django App with Azure SQL

echo "🚀 Deploying Custom Drone Django App to Heroku (Docker + Azure SQL)"

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

# App name (change this to your existing app name)
APP_NAME="ddeveloper72-custom-drone"

echo "📱 Configuring Heroku app: $APP_NAME"

# Set stack to container (for Docker deployment)
echo "🐳 Setting stack to container..."
heroku stack:set container --app $APP_NAME

# Load environment variables from .env file
if [ ! -f .env ]; then
    echo "❌ .env file not found. Please create one with your credentials."
    exit 1
fi

echo "⚙️  Setting environment variables from .env file..."

# Load .env
set -a
source .env
set +a

# Core Django settings
heroku config:set DEBUG=False --app $APP_NAME
heroku config:set SECRET_KEY="$SECRET_KEY" --app $APP_NAME
heroku config:set ALLOWED_HOSTS="$APP_NAME.herokuapp.com" --app $APP_NAME

# Azure SQL Configuration
echo "🗄️  Configuring Azure SQL Database..."
heroku config:set AZURE_SQL_HOST="$AZURE_SQL_HOST" --app $APP_NAME
heroku config:set AZURE_SQL_NAME="$AZURE_SQL_NAME" --app $APP_NAME
heroku config:set AZURE_SQL_USER="$AZURE_SQL_USER" --app $APP_NAME
heroku config:set AZURE_SQL_PASSWORD="$AZURE_SQL_PASSWORD" --app $APP_NAME
heroku config:set AZURE_SQL_PORT="$AZURE_SQL_PORT" --app $APP_NAME
heroku config:set AZURE_SQL_SCHEMA="$AZURE_SQL_SCHEMA" --app $APP_NAME

# AWS S3 Configuration
echo "📦 Configuring AWS S3 Storage..."
heroku config:set AWS_ACCESS_KEY_ID="$AWS_ACCESS_KEY_ID" --app $APP_NAME
heroku config:set AWS_SECRET_ACCESS_KEY="$AWS_SECRET_ACCESS_KEY" --app $APP_NAME
heroku config:set AWS_STORAGE_BUCKET_NAME="$AWS_STORAGE_BUCKET_NAME" --app $APP_NAME
heroku config:set AWS_S3_REGION_NAME="$AWS_S3_REGION_NAME" --app $APP_NAME

# Stripe Configuration (if you have it)
if [ ! -z "$STRIPE_PUBLISHABLE" ]; then
    echo "💳 Configuring Stripe..."
    heroku config:set STRIPE_PUBLISHABLE="$STRIPE_PUBLISHABLE" --app $APP_NAME
    heroku config:set STRIPE_SECRET="$STRIPE_SECRET" --app $APP_NAME
fi

echo "✅ Configuration complete!"
echo ""
echo "📋 Current configuration:"
heroku config --app $APP_NAME

echo ""
echo "🚀 Ready to deploy! Run the following commands:"
echo ""
echo "  git add ."
echo "  git commit -m 'Configure for Azure SQL and Docker deployment'"
echo "  git push heroku main"
echo ""
echo "After deployment, run:"
echo "  heroku run python manage.py migrate --app $APP_NAME"
echo "  heroku run python manage.py createsuperuser --app $APP_NAME"
