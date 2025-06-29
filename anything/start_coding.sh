#!/bin/bash

# 🧩 1. 프로젝트 폴더 위치 설정
PROJECT_DIR="$HOME/github/codingTest"
DATE=$(date +"%Y%m%d_%H%M%S")
FILENAME="problem_$DATE.py"

# 🧩 2. Cursor에 열 파일 생성
touch "$PROJECT_DIR/$FILENAME"

# 🧩 3. 템플릿 넣기 (원하는 코드 기본 삽입)
echo -e "# 🚀 코테 문제 템플릿\n\nimport sys\ninput = sys.stdin.readline\n\n" > "$PROJECT_DIR/$FILENAME"

# 🧩 4. Cursor에서 파일 열기
open -a "Cursor" "$PROJECT_DIR/$FILENAME"

# 🧩 5. Jupyter Notebook 커널 2개 실행 (tmux 또는 iTerm 등에서 실행)
osascript <<EOF
tell application "Terminal"
    do script "cd $PROJECT_DIR && source ~/venvs/jupyter/bin/activate && jupyter console"
    delay 0.5
    do script "cd $PROJECT_DIR && source ~/venvs/jupyter/bin/activate && jupyter console" in front window
end tell
EOF

echo "✅ 파일 생성 및 주피터 커널 2개 실행 완료: $FILENAME"