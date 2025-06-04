@echo off
REM Update dependencies inside the virtual environment
if exist venv (
    call venv\Scripts\activate
    pip install --upgrade -r requirements.txt
) else (
    echo Virtual environment not found. Run start.bat first.
)
