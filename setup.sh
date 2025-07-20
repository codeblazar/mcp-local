#!/bin/bash

# Create virtual environment
python -m venv venv

# Activate virtual environment
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows
    source venv/Scripts/activate
else
    # Linux/macOS
    source venv/bin/activate
fi

# Install dependencies
pip install -r requirements.txt

echo "✅ Setup complete! Now you can run:"
echo "   Terminal 1: python simple_mcp_server.py"
echo "   Terminal 2: python simple_mcp_client.py"
