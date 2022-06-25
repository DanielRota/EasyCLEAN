set NAME=EasyCLEAN

set VERSION=1.0
SET MYDATE=%DATE:~6,4%%DATE:~3,2%%DATE:~0,2%

"C:\Program Files\DdxProg\DdxUtils\DdxUtils64.exe" P .\ ".\%NAME%_%VERSION%@%MYDATE%.zpakp" --base-path %~dp0 --exclude *.zpakp --exclude build.bat --exclude .vscode* --exclude __pycache__*
