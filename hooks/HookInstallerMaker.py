with open("sethook.bat", 'w') as bat:
    def w(s=''):
        bat.writelines(s + '\n')
    w('''@echo off
echo ⚠️ This script will replace git hook "prepare-commit-msg"
echo Close the window if you don't want to do this.
echo.
pause
del .git\hooks\prepare-commit-msg
del .git\hooks\prepare-commit-msg.sample
set "HOOK_FILE=.git/hooks/prepare-commit-msg"

(''')

    # prepare-commit-msg
    with open("prepare-commit-msg", 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break

            if line == "\n":
                w('echo.')
            else:
                w(f'echo {line[:-1].replace(">", "^>").replace(")", "^)")}')
    w(r') > %HOOK_FILE%')
    w()
    # w(r'move /Y %TEMP_FILE% %COMMIT_MSG_FILE% >nul')
    w('echo.')
    w('echo done')
    w('pause')
