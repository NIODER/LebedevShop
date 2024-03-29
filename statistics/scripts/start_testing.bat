@echo off

CALL :StartTesting full %~1
CALL :StartTesting one_pg %~1
CALL :StartTesting onepgpool %~1
CALL :StartTesting oneweb %~1

py ./statistics/summary.py %~1

./statistics/scripts/clear_nginx_logs.bat

EXIT /B %ERROR_LEVEL%

:StartTesting
docker compose -f ./docker/%~1/docker-compose.yml build
start cmd /C docker compose -f ./docker/%~1/docker-compose.yml up
echo "Press enter when docker will be ready"
pause
echo "Starting statistics script for %~1 configuration"
py ./statistics/main.py %~2 %~1
echo "Cleaning docker compose"
docker compose -f ./docker/%~1/docker-compose.yml down -v
EXIT /B 0

