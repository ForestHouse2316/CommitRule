@echo off
echo ⚠️ This script will replace git hook "prepare-commit-msg"
echo Close the window if you don't want to do this.
echo.
pause
del .git\hooks\prepare-commit-msg
del .git\hooks\prepare-commit-msg.sample
set "HOOK_FILE=.git/hooks/prepare-commit-msg"

(
echo #!/bin/sh
echo.
echo COMMIT_MSG_FILE=$1
echo TEMP_FILE=$(mktemp^)
echo.
echo # Define patterns
echo sed \
echo -e 's/:feat:/✨/g' \
echo -e 's/:fix:/🐛/g' \
echo -e 's/:patch:/🩹/g' \
echo -e 's/:refactor:/♻️/g' \
echo -e 's/:opt:/⚡/g' \
echo -e 's/:style:/🎨/g' \
echo -e 's/:test:/🧪/g' \
echo -e 's/:docs:/📝/g' \
echo -e 's/:res:/️📦/g' \
echo -e 's/:dep:/🔌/g' \
echo -e 's/:ci:/🔃/g' \
echo -e 's/:merge:/🔀/g' \
echo -e 's/:revert:/️⏪/g' \
echo -e 's/:cherry:/🍒/g' \
echo -e 's/:git:/🐈‍⬛/g' \
echo -e 's/:rename:/✏️/g' \
echo -e 's/:clean:/🧹/g' \
echo -e 's/:chore:/➿/g' $COMMIT_MSG_FILE ^> $TEMP_FILE
echo.
echo # Replace the original message to the modified one
echo mv $TEMP_FILE $COMMIT_MSG_FILE
) > %HOOK_FILE%

echo.
echo done
pause
