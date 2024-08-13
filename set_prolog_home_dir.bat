@echo off

SETLOCAL enabledelayedexpansion
SETLOCAL enableextensions

set KEY_NAME="HKEY_LOCAL_MACHINE\SOFTWARE\SWI\Prolog"
set VALUE_NAME=home

FOR /F "usebackq skip=2 tokens=1-2,*" %%A IN (`REG QUERY %KEY_NAME% /v %VALUE_NAME% 2^>nul`) DO (
    set ValueName=%%A
    set ValueType=%%B
    set ValueValue=%%C
)

if defined ValueName (
    echo Found SWIPL home at: %ValueValue%
	SETX SWI_HOME_DIR "%ValueValue%"
	echo SWI_HOME_DIR is set to: %ValueValue%
	echo You can now use the program.
	exit /b 0
) else (
    echo %KEY_NAME%\%VALUE_NAME% not found.
)

REM Find the path containing swipl\bin in the system PATH
SET "SWI_BIN_PATH="
FOR %%A IN ("%PATH:;=" "%") DO (
	Set "aux=%%~A"
    Set "aux=!aux:~-10!"
	
	IF !aux! == \swipl\bin (
        SET "SWI_BIN_PATH=%%~A"
	)
)

IF NOT DEFINED SWI_BIN_PATH (
    echo swipl\bin was not found in the system PATH.
    exit /b 1
) ELSE (
    echo Found swipl\bin at: %SWI_BIN_PATH%
)

IF NOT DEFINED SWI_HOME_DIR (
    echo SWI_HOME_DIR is not set in the system PATH.
	SET "aux=%SWI_BIN_PATH%"
	SET "aux=!aux:~0,-4!"
	SETX SWI_HOME_DIR "!aux!"
	echo SWI_HOME_DIR is set to: !aux!
	echo You can now use the program.
) ELSE (
    echo SWI_HOME_DIR is already set to: %SWI_HOME_DIR%
)