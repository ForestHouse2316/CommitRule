def make_hook():
    with open('prepare-commit-msg', 'w', encoding='utf-8') as f:
        def wp(tag, emoji):
            f.writelines(f"-e 's/:{tag}:/{emoji}/g'")
        f.writelines('''#!/bin/sh

COMMIT_MSG_FILE=$1
TEMP_FILE=$(mktemp)

# Define patterns
sed''')
        with open('pattern.txt', 'r', encoding='utf-8') as p:
            while True:
                line = p.readline().replace('\uFEFF', '') # remove [ZWNBSP]
                if not line:
                    break
                elif line == '\n':
                    continue
                f.writelines(" \\\n")
                args = line.replace('\n', '').split('>')
                if len(args) != 2:
                    SyntaxError(f"Wrong syntax : {line}")
                wp(args[0].strip(), args[1].strip())
    
        f.writelines(''' $COMMIT_MSG_FILE > $TEMP_FILE

# Replace the original message to the modified one
mv $TEMP_FILE $COMMIT_MSG_FILE
''')

def make_installer():
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
