# Set Azure SQL configuration on Heroku
Write-Host "Setting Azure SQL configuration on Heroku..." -ForegroundColor Green

heroku config:set AZURE_SQL_HOST=myfreesqldbserver72.database.windows.net -a ddeveloper72-custom-drone
heroku config:set AZURE_SQL_NAME=drone_app_v2 -a ddeveloper72-custom-drone
heroku config:set AZURE_SQL_USER=developer@myfreesqldbserver72 -a ddeveloper72-custom-drone
heroku config:set AZURE_SQL_PASSWORD=M2Dnaa@5036089 -a ddeveloper72-custom-drone
heroku config:set AZURE_SQL_PORT=1433 -a ddeveloper72-custom-drone

Write-Host "`nVerifying configuration..." -ForegroundColor Green
heroku config -a ddeveloper72-custom-drone | Select-String -Pattern "AZURE"

Write-Host "`nRestarting app..." -ForegroundColor Green
heroku restart -a ddeveloper72-custom-drone

Write-Host "`nDone! Wait 30 seconds then test: https://ddeveloper72-custom-drone.herokuapp.com/posts/" -ForegroundColor Green
