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
                