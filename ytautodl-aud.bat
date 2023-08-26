@echo off
title YTAutoDL v1 ^| by eltrevi_

set LF=^


cls

:path
echo Enter the path to download the files to without quotes. If you don't enter anything, the files will be downloaded to the current directory: "%cd%"
set "_path=%cd%"
set /p "_path=> "

cls

echo Enter the YouTube videos' URLs to download
:input
set "_url.new="
set /p "_url.new=> "
if not ["%_url.new%"]==[""] (
	set "_url=%_url% "%_url.new%""
	goto input
)

cls

setlocal EnableDelayedExpansion
set "_url=%_url: =!LF!%"
for /F %%i in ("!_url!") do (
	<nul set /p "=Downloading %%i..."
	yt-dlp --no-warnings -qx -o "%_path%\%%(title)s.%%(ext)s" %%i --no-playlist 2>%temp%\yt-dlp.log || (
		echo. err
		type %temp%\yt-dlp.log
		goto next
	)
	echo. ok

	:next
	rem continue
)
endlocal

echo.
<nul set /p "=Done! Press any key to exit or close this window."
pause >nul

exit /b