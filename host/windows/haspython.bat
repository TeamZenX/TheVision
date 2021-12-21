@echo off & title %~nx0 & color 5F

goto :DOES_PYTHON_EXIST

:DOES_PYTHON_EXIST
python -V | find /v "Python" >NUL 2>NUL && (goto :PYTHON_DOES_NOT_EXIST)
python -V | find "Python"    >NUL 2>NUL && (goto :PYTHON_DOES_EXIST)
goto :EOF

:PYTHON_DOES_NOT_EXIST
echo Python is not installed on your system.
set /p ans="Do You want to install?: "
if not %ans%=="q" ( Powershell.exe -File host\windows\python.ps1) else :EXIT0
goto :EOF

:PYTHON_DOES_EXIST
for /f "delims=" %%V in ('python -V') do @set ver=%%V
echo Python %ver%  Is Installed Starting Userbot...
python -m vision
goto :EOFw
