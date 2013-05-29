@echo off
echo Diese Eingabeforderung nicht waehrend des Running beenden
echo Bitte erst bei einem gewollten Shutdown schliessen
echo Please close this command only for Shutdown
set PYTHONHOME=\xampp\python
echo Apache 2 is starting with PYTHONHOME=%PYTHONHOME%
apache\bin\apache.exe
