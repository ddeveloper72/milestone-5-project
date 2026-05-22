@echo off
echo ========================================
echo FORCE REBUILD AND DEPLOY TO HEROKU
echo ========================================

echo Step 1: Pruning Docker build cache...
docker builder prune -f
docker system prune -f

echo.
echo Step 2: Building container for Heroku (without cache)...
echo This may take several minutes...
heroku container:push web -a ddeveloper72-custom-drone

if %ERRORLEVEL% EQU 0 (
    echo.
    echo Step 3: Build successful! Releasing to production...
    heroku container:release web -a ddeveloper72-custom-drone
    
    if %ERRORLEVEL% EQU 0 (
        echo.
        echo ========================================
        echo DEPLOYMENT COMPLETE!
        echo ========================================
        echo.
        echo Checking recent releases...
        heroku releases -a ddeveloper72-custom-drone -n 3
        echo.
        echo Your app is now running at:
        echo https://ddeveloper72-custom-drone.herokuapp.com/posts/
        echo.
        echo Opening in browser in 5 seconds...
        timeout /t 5 /nobreak
        start https://ddeveloper72-custom-drone.herokuapp.com/posts/
    ) else (
        echo.
        echo ERROR: Release failed!
        echo Check the logs with: heroku logs --tail -a ddeveloper72-custom-drone
    )
) else (
    echo.
    echo ERROR: Build failed!
    echo Check Docker is running and you're logged in to Heroku.
)

echo.
pause
