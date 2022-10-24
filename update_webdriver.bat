@echo off
cd /d %~dp0

set CHROME_PATH=C:\Program Files\Google\Chrome\Application\chrome.exe

powershell Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process; (Get-Item '%CHROME_PATH%').VersionInfo.ProductVersion > chrome.ver

call venv\Scripts\activate.bat & py update_webdriver.py ".."

pause