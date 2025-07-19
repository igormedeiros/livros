REM Navigate to the script's directory
cd /d "%~dp0"

REM Activate the uv virtual environment
call ..\.venv\Scripts\activate

REM Execute the Python script
python exercicio_1.py
