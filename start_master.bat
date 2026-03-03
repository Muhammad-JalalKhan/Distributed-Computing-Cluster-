@echo off
start cmd /k "python -m dask scheduler"
timeout /t 5
start cmd /k "python -m dask worker tcp://10.90.23.184:8786"
pause