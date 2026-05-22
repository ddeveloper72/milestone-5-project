# Dockerfile for Heroku deployment with Azure SQL
FROM python:3.12-slim

# Install system dependencies and Microsoft ODBC Driver for SQL Server
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    unixodbc-dev \
    gcc \
    g++ \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir gunicorn

# Copy application code
COPY . .

# Collect static files (will use S3 in production)
RUN python manage.py collectstatic --noinput --clear || echo "Static files skipped"

# Expose port (Heroku assigns PORT dynamically)
EXPOSE $PORT

# Start gunicorn
CMD gunicorn --bind 0.0.0.0:$PORT --workers 3 --timeout 120 drone_debug.wsgi:application
