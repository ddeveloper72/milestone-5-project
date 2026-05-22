# Deploying to Heroku with Azure SQL Database

This guide explains how to deploy your Custom Drone Django app to Heroku using **Docker containers** with **Azure SQL Database**.

## Prerequisites

- ✅ Heroku CLI installed ([Download](https://devcenter.heroku.com/articles/heroku-cli))
- ✅ Git repository initialized
- ✅ Azure SQL Database configured (already done: `drone_app_v2` on `myfreesqldbserver72`)
- ✅ AWS S3 bucket configured (already done: `custom-drone` in `eu-west-1`)

## Deployment Architecture

```
┌──────────────────┐
│  Heroku (Docker) │
│  Django App      │
│  Python 3.12     │
└────────┬─────────┘
         │
         ├─────────► Azure SQL Database (myfreesqldbserver72)
         │           • serverless tier (auto-pause/resume)
         │           • Database: drone_app_v2
         │
         └─────────► AWS S3 (custom-drone)
                     • Media files (images, uploads)
                     • Region: eu-west-1
```

## Step-by-Step Deployment

### 1. Login to Heroku

```bash
heroku login
```

### 2. Configure Your App for Container Deployment

```bash
# Set your app to use Docker containers
heroku stack:set container --app custom-drone-ddeveloper72

# Or create a new app if needed
# heroku create your-app-name --region us
```

### 3. Configure Environment Variables

Run the automated configuration script:

```bash
bash deploy_heroku_azure.sh
```

**Or configure manually:**

```bash
APP_NAME="custom-drone-ddeveloper72"

# Django Core Settings
heroku config:set DEBUG=False --app $APP_NAME
heroku config:set SECRET_KEY="your-secret-key-here" --app $APP_NAME

# Azure SQL Database
heroku config:set AZURE_SQL_HOST="myfreesqldbserver72.database.windows.net" --app $APP_NAME
heroku config:set AZURE_SQL_NAME="drone_app_v2" --app $APP_NAME
heroku config:set AZURE_SQL_USER="developer@myfreesqldbserver72" --app $APP_NAME
heroku config:set AZURE_SQL_PASSWORD="your-password-here" --app $APP_NAME
heroku config:set AZURE_SQL_PORT="1433" --app $APP_NAME
heroku config:set AZURE_SQL_SCHEMA="dbo" --app $APP_NAME

# AWS S3 Storage
heroku config:set AWS_ACCESS_KEY_ID="your-access-key" --app $APP_NAME
heroku config:set AWS_SECRET_ACCESS_KEY="your-secret-key" --app $APP_NAME
heroku config:set AWS_STORAGE_BUCKET_NAME="custom-drone" --app $APP_NAME
heroku config:set AWS_S3_REGION_NAME="eu-west-1" --app $APP_NAME

# Stripe (if applicable)
heroku config:set STRIPE_PUBLISHABLE="pk_test_..." --app $APP_NAME
heroku config:set STRIPE_SECRET="sk_test_..." --app $APP_NAME
```

### 4. Verify Configuration

```bash
heroku config --app custom-drone-ddeveloper72
```

### 5. Deploy to Heroku

```bash
# Add all files
git add .

# Commit changes
git commit -m "Configure for Heroku with Azure SQL and Docker"

# Push to Heroku (triggers container build)
git push heroku main

# Or if you're on a different branch:
# git push heroku your-branch:main
```

### 6. Run Database Migrations

After deployment completes:

```bash
heroku run python manage.py migrate --app custom-drone-ddeveloper72
```

### 7. Create Superuser

```bash
heroku run python manage.py createsuperuser --app custom-drone-ddeveloper72
```

### 8. Open Your App

```bash
heroku open --app custom-drone-ddeveloper72
```

## Files Created for Deployment

| File | Purpose |
|------|---------|
| `Dockerfile.heroku` | Docker container definition with ODBC Driver 18 for SQL Server |
| `heroku.yml` | Heroku container deployment configuration |
| `deploy_heroku_azure.sh` | Automated deployment script |
| `runtime.txt` | Python version specification (3.12.4) |
| `Procfile` | Process definition (gunicorn) |

## Important Notes

### Azure SQL Serverless Auto-Pause

Your Azure SQL database uses **serverless tier** which automatically pauses after 1 hour of inactivity. The app includes:

- ✅ **DatabaseRetryMiddleware**: Automatically retries connections with exponential backoff
- ✅ **Connection Timeout**: 120 seconds to allow time for database to resume
- ✅ **Health Check Endpoint**: `/_health/` for monitoring

**First request after pause may take 30-60 seconds** while the database resumes.

### Static Files

- **Static files** (CSS, JS): Served via Heroku (collected during build)
- **Media files** (user uploads): Stored in AWS S3 bucket `custom-drone`

### Environment-Specific Behavior

The app automatically detects the environment:

```python
# Local Development (DEBUG=True)
- Database: Azure SQL or Local MySQL (via .env)
- Static files: Local filesystem
- Media files: AWS S3

# Production (DEBUG=False)
- Database: Azure SQL (via Heroku config vars)
- Static files: Collected and served via whitenoise
- Media files: AWS S3
```

## Troubleshooting

### Database Connection Issues

```bash
# Check logs
heroku logs --tail --app custom-drone-ddeveloper72

# Test database connection
heroku run python manage.py check --database default --app custom-drone-ddeveloper72

# Check config vars
heroku config --app custom-drone-ddeveloper72
```

### Application Not Starting

```bash
# Check build logs
heroku logs --tail --app custom-drone-ddeveloper72

# Verify container build
heroku container:release web --app custom-drone-ddeveloper72
```

### Azure SQL Firewall

Ensure Azure SQL Server firewall rules allow:
1. Your local IP (for development)
2. Azure services (0.0.0.0-0.0.0.0)
3. **No specific Heroku IPs needed** - Azure services setting covers Heroku

In Azure Portal:
- Go to: SQL Server → Networking → Firewall rules
- Enable: "Allow Azure services and resources to access this server"

## Monitoring

### View Logs

```bash
heroku logs --tail --app custom-drone-ddeveloper72
```

### Check Health

```bash
# Health check endpoint
curl https://custom-drone-ddeveloper72.herokuapp.com/_health/

# Application status
heroku ps --app custom-drone-ddeveloper72
```

### Scale Dynos

```bash
# Check current dyno status
heroku ps --app custom-drone-ddeveloper72

# Scale up (if needed)
heroku ps:scale web=1 --app custom-drone-ddeveloper72
```

## Cost Optimization

### Current Setup (Minimal Cost)

| Service | Tier | Monthly Cost |
|---------|------|--------------|
| Heroku | Eco Dyno | $5/month |
| Azure SQL | Serverless Free Tier | $0/month (within limits) |
| AWS S3 | Standard | ~$0.50/month (low usage) |
| **Total** | | **~$5.50/month** |

### Azure SQL Free Tier Limits

- **Storage**: 32 GB (maximum)
- **vCores**: 2 (Gen5)
- **Auto-pause**: After 1 hour idle (resumes automatically on first request)

⚠️ **If you exceed free tier limits, charges may apply.**

## Next Steps After Deployment

1. ✅ Test the application at: https://custom-drone-ddeveloper72.herokuapp.com
2. ✅ Login to admin panel: https://custom-drone-ddeveloper72.herokuapp.com/admin
3. ✅ Create blog posts with S3 images
4. ✅ Monitor database usage in Azure Portal
5. ✅ Set up custom domain (optional)

## Useful Commands

```bash
# View config
heroku config --app custom-drone-ddeveloper72

# Run Django shell
heroku run python manage.py shell --app custom-drone-ddeveloper72

# Run custom management command
heroku run python manage.py <command> --app custom-drone-ddeveloper72

# Restart application
heroku restart --app custom-drone-ddeveloper72

# Open app in browser
heroku open --app custom-drone-ddeveloper72
```

## Rollback (if needed)

```bash
# View releases
heroku releases --app custom-drone-ddeveloper72

# Rollback to previous version
heroku rollback v<version-number> --app custom-drone-ddeveloper72
```

---

**Ready to deploy!** 🚀 Run `bash deploy_heroku_azure.sh` to get started.
