@echo off
echo Setting up MCP Tutorial...

REM Create virtual environment
python -m venv venv

REM Activate virtual environment
call venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

echo.
echo ✅ Setup complete! Now you can run:
echo    Terminal 1: python simple_mcp_server.py
echo    Terminal 2: python simple_mcp_client.py
pause
