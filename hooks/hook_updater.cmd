@echo off
echo.
echo.
echo.
echo Hook updater - by ForestHouse
echo ------------------------------
echo.
echo This task will overwrite your ".git\hooks\prepare-commit-msg" file.
echo.

:check
set /p res="Would you like to start the batch job? (y/n): "
if /i "%res%" == "y" goto update
if /i "%res%" == "n" exit /b
goto check

:dirError
cls
echo.
echo.
echo.
echo Directory ".git\hooks" does not exist.
echo Place this batch file to the top of the project directory,
echo where the .git folder exist.
echo.
echo.
echo.
echo Press any key to exit...
pause >nul
exit /b


:update
cls
echo.
echo.
echo.
echo Checking directory. . .
if not exist .git\hooks goto dirError

echo.
echo Remove original file. . .
echo.
timeout 1
del .git\hooks\prepare-commit-msg
del .git\hooks\prepare-commit-msg.sample

echo.
echo Start downloading. . .
echo. 
timeout 1
curl https://raw.githubusercontent.com/ForestHouse2316/CommitRule/main/hooks/prepare-commit-msg > .git\hooks\prepare-commit-msg

echo.
echo Done
timeout 3