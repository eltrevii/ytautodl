@echo off
title YTAutoDL v1 ^| by eltrevi_
setlocal EnableExtensions EnableDelayedExpansion

set LF=^



cls

:path
echo Enter the path to download the files to without quotes. If you don't enter anything, the files will be downloaded to the current directory: "%cd%".
set "_path=%cd%"
set /p "_path=> "

cls

:input
set "_url.new="
set /p "_url.new=> "
if not ["%_url.new%"]==[""] (
	set "_url=%_url% "%_url.new%""
	goto input
)

cls

set "_url=%_url: =!LF!%"
for /F %%i in ("!_url!") do (  
  yt-dlp -o '%_path%\%%^(title^)s.%%^(ext^)s' %%i
)

endlocal
exit /b