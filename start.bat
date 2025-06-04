@echo off
REM Setup virtual environment and start the Flask server
if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate
pip install -r requirements.txt
flask run --app app
