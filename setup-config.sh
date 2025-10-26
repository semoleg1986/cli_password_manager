#!/bin/bash

touch requirements.in
touch README.md
touch Makefile

cat > .gitignore <<EOF
# Python
.venv/
*.pyc
__pycache__/
*.pyo
*.pyd
.Python
*.egg-info/
dist/
build/
.pytest_cache/
*.sqlite3

# IDE and OS
.idea/
*.swp
.DS_Store
.env
.copy.env
EOF

cat > pyproject.toml <<EOF
[tool.black]
line-length = 88
target-version = ['py311']

[tool.isort]
profile = "black"
line_length = 88
multi_line_output = 3
include_trailing_comma = true
EOF


cat > .flake8 <<EOF
[flake8]
max-line-length = 88
extend-ignore = E203, W503
exclude =
    .venv,
    __pycache__,
    build,
    dist
EOF

cat > pytest.ini <<EOF
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
EOF

cat > .pre-commit-config.yaml <<EOF
repos:
  # --- Импорт и сортировка ---
  - repo: https://github.com/pre-commit/mirrors-isort
    rev: v5.10.1
    hooks:
      - id: isort
  # --- Автоформатирование кода ---
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black

  # --- Проверка стиля и ошибок ---
  - repo: https://github.com/pycqa/flake8
    rev: 7.0.0
    hooks:
      - id: flake8

  # --- Проверка типов ---
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.5.1
    hooks:
      - id: mypy
        args: [ "--install-types", "--non-interactive" ]

  # --- Локальный хук для тестов ---
  - repo: local
    hooks:
      - id: pytest
        name: pytest
        entry: pytest tests
        language: system
        pass_filenames: false
EOF

tree || ls -R