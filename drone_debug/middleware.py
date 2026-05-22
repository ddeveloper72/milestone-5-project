"""
Middleware to handle Azure SQL Database serverless auto-pause/resume.
Retries database connections with exponential backoff when database is waking up.
"""
import time
import logging
from django.db import connection, OperationalError
from django.http import JsonResponse

logger = logging.getLogger(__name__)


class DatabaseRetryMiddleware:
    """
    Middleware to retry database connections when Azure SQL is waking from sleep.
    Implements exponential backoff with configurable max retries.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
        self.max_retries = 5
        self.initial_delay = 1  # seconds
        self.max_delay = 30  # seconds
    
    def __call__(self, request):
        retries = 0
        delay = self.initial_delay
        
        while retries < self.max_retries:
            try:
                # Test database connection before processing request
                connection.ensure_connection()
                
                # Process the request normally
                response = self.get_response(request)
                return response
                
            except OperationalError as e:
                error_msg = str(e).lower()
                
                # Check if it's a database waking/connection error
                if any(keyword in error_msg for keyword in [
                    'timeout', 'connection', 'server', 'database', 
                    'unavailable', 'connect', 'unreachable'
                ]):
                    retries += 1
                    
                    if retries >= self.max_retries:
                        logger.error(
                            f"Database connection failed after {self.max_retries} retries: {e}"
                        )
                        return JsonResponse({
                            'error': 'Database temporarily unavailable. Please try again in a moment.',
                            'status': 503
                        }, status=503)
                    
                    logger.warning(
                        f"Database connection attempt {retries}/{self.max_retries} failed. "
                        f"Retrying in {delay}s... Error: {e}"
                    )
                    
                    # Close the old connection
                    connection.close()
                    
                    # Wait with exponential backoff
                    time.sleep(delay)
                    delay = min(delay * 2, self.max_delay)
                else:
                    # Different error - re-raise
                    raise
        
        # Should never reach here, but just in case
        return JsonResponse({
            'error': 'Database connection failed',
            'status': 503
        }, status=503)


class DatabaseHealthCheckMiddleware:
    """
    Adds a health check endpoint that tests database connectivity.
    Access at /_health/ to verify database is awake.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if request.path == '/_health/':
            return self.health_check(request)
        return self.get_response(request)
    
    def health_check(self, request):
        try:
            # Test database connection
            from django.db import connection
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            
            return JsonResponse({
                'status': 'healthy',
                'database': 'connected'
            })
        except Exception as e:
            return JsonResponse({
                'status': 'unhealthy',
                'database': 'disconnected',
                'error': str(e)
            }, status=503)
