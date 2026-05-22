# Quick Deployment Reference

## Files Created for Heroku Deployment

✅ **Dockerfile.heroku** - Docker container with Azure SQL support (ODBC Driver 18)  
✅ **heroku.yml** - Heroku container deployment config  
✅ **deploy_heroku_azure.sh** - Automated deployment script  
✅ **DEPLOY_HEROKU.md** - Complete deployment guide  
✅ **runtime.txt** - Updated to Python 3.12.4  
✅ **requirements.txt** - Updated gunicorn to 21.2.0  

## Quick Start (5 Steps)

### 1. Login to Heroku
```bash
heroku login
```

### 2. Set Container Stack
```bash
heroku stack:set container --app custom-drone-ddeveloper72
```

### 3. Configure Environment Variables
```bash
bash deploy_heroku_azure.sh
```

### 4. Deploy
```bash
git add .
git commit -m "Configure for Heroku with Azure SQL"
git push heroku main
```

### 5. Run Migrations
```bash
heroku run python manage.py migrate --app custom-drone-ddeveloper72
heroku run python manage.py createsuperuser --app custom-drone-ddeveloper72
```

## Your Configuration

**App Name:** custom-drone-ddeveloper72  
**Database:** Azure SQL (`drone_app_v2` on `myfreesqldbserver72.database.windows.net`)  
**Storage:** AWS S3 (`custom-drone` bucket in `eu-west-1`)  
**Deployment:** Docker container (Python 3.12)  

## Estimated Monthly Cost

- Heroku Eco Dyno: **$5/month**
- Azure SQL Serverless: **Free tier** (within limits)
- AWS S3: **~$0.50/month**
- **Total: ~$5.50/month**

## Important URLs

**App:** https://custom-drone-ddeveloper72.herokuapp.com  
**Admin:** https://custom-drone-ddeveloper72.herokuapp.com/admin  
**Health Check:** https://custom-drone-ddeveloper72.herokuapp.com/_health/  

## Useful Commands

```bash
# View logs
heroku logs --tail --app custom-drone-ddeveloper72

# Check config
heroku config --app custom-drone-ddeveloper72

# Restart app
heroku restart --app custom-drone-ddeveloper72

# Open in browser
heroku open --app custom-drone-ddeveloper72
```

## Troubleshooting

**Slow first request?** Azure SQL serverless auto-pauses after 1 hour idle. First request resumes the database (30-60 seconds).

**Connection errors?** Check Azure SQL firewall allows Azure services (0.0.0.0-0.0.0.0).

**Build failures?** Check `heroku logs --tail` for detailed error messages.

---

📖 **Full guide:** [DEPLOY_HEROKU.md](DEPLOY_HEROKU.md)
