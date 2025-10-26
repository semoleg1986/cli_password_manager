#!/bin/bash

mkdir -p utils tests

touch main.py
touch utils/__init__.py
touch tests/__init__.py

cat > main.py <<EOF
def main():
    print("Hello from $PROJECT_NAME!")


if __name__ == "__main__":
    main()
EOF

#cat > .gitignore <<EOF
## Python
#.venv/
#*.pyc
#__pycache__/
#*.pyo
#*.pyd
#.Python
#*.egg-info/
#dist/
#build/
#.pytest_cache/
#*.sqlite3
#
## IDE and OS
#.idea/
#*.swp
#.DS_Store
#.env
#.copy.env
#EOF

#cat > pyproject.toml <<EOF
#[tool.black]
#line-length = 88
#target-version = ['py311']
#
#[tool.isort]
#profile = "black"
#line_length = 88
#multi_line_output = 3
#include_trailing_comma = true
#EOF

tree || ls -R