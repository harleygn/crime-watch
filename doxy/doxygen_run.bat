Echo off

echo.
echo  Please enter Project Name
echo.

set /P user_input=Enter name:

set PROJNAME=%user_input%
set DOXYLOG=%PROJNAME%_Doxylog.txt

set DOT_PATH=%CD%\graphviz-2.38\release\bin
set path=%PATH%;%CD%\graphviz-2.38\release\bin
set SRCDIR=%CD%\Source
set PROJPATH=%CD%\%PROJNAME%


doxygen Doxyfile
pause
:exit
