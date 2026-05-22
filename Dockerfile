# Dockerfile for Heroku deployment with Azure SQL
FROM python:3.12-slim

# Install system dependencies and Microsoft ODBC Driver for SQL Server
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    unixodbc-dev \
    gcc \
    g++ \
    ca-certificates \
    libjpeg-dev \
    zlib1g-dev \
    && curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg \
    && curl -fsSL https://packages.microsoft.com/config/debian/12/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft-prod.gpg] https://packages.microsoft.com/debian/12/prod bookworm main" > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements-heroku.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir gunicorn

# Copy application code
COPY . .

# Set minimal environment for collectstatic (dummy values, real ones set via Heroku config)
ENV DJANGO_SETTINGS_MODULE=drone_debug.settings \
    SECRET_KEY=temp-build-key-for-collectstatic-only \
    DATABASE_URL=sqlite:///dummy.db \
    DEBUG=False \
    AWS_ACCESS_KEY_ID=dummy-key \
    AWS_SECRET_ACCESS_KEY=dummy-secret \
    AWS_STORAGE_BUCKET_NAME=dummy-bucket \
    AWS_S3_REGION_NAME=us-east-1 \
    STRIPE_PUBLISHABLE=pk_test_dummy \
    STRIPE_SECRET=sk_test_dummy \
    EMAIL_ADDRESS=build@dummy.com \
    EMAIL_PASSWORD=dummy

# Collect static files for WhiteNoise
RUN python manage.py collectstatic --noinput --clear

# Expose port (Heroku assigns PORT dynamically)
EXPOSE $PORT

# Start gunicorn
CMD gunicorn --bind 0.0.0.0:$PORT --workers 3 --timeout 120 drone_debug.wsgi:application
