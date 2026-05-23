from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from django.conf import settings
import time
import os

# Create your views here.


def index(request):
    """
    Display and index page
    """
    return render(request, "index.html")


def health_check(request):
    """
    Health check endpoint to test database connectivity
    Used to wake up serverless databases before user navigation
    
    Query params:
    - simulate_delay: Number of seconds to delay (for testing, default 0)
    """
    start_time = time.time()
    
    # Simulate delay if requested (for testing loading overlay)
    simulate_delay = request.GET.get('simulate_delay', '0')
    try:
        delay = float(simulate_delay)
        if delay > 0:
            time.sleep(min(delay, 30))  # Cap at 30 seconds
    except ValueError:
        delay = 0
    
    try:
        # Test database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
        
        elapsed = time.time() - start_time
        
        return JsonResponse({
            'status': 'healthy',
            'database': 'connected',
            'response_time_ms': round(elapsed * 1000, 2),
            'simulated_delay_s': delay if delay > 0 else None
        })
    
    except Exception as e:
        elapsed = time.time() - start_time
        
        return JsonResponse({
            'status': 'degraded',
            'database': 'error',
            'error': str(e),
            'response_time_ms': round(elapsed * 1000, 2)
        }, status=503)


def keep_alive(request):
    """
    Keep-alive endpoint to prevent database auto-pause
    Should be called periodically (e.g., every 45 minutes)
    """
    try:
        # Quick database ping
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
        
        return JsonResponse({
            'status': 'ok',
            'message': 'Database connection maintained',
            'timestamp': time.time()
        })
    
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
            'timestamp': time.time()
        }, status=500)


def test_loading(request):
    """
    Test page for database loading overlay and delay simulation
    """
    return render(request, "test_loading.html")
