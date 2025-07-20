# MCP Server Tutorial

A simple, educational Model Context Protocol (MCP) server that demonstrates the core concepts in just 2 files.

Perfect for learning how MCP works before building more complex servers!

## Quick Start

### Option 1: Automatic Setup
```bash
# Clone the repository
git clone https://github.com/codeblazar/mcp-local.git
cd mcp-local

# Run setup script
# Windows:
setup.bat
# Linux/macOS:
chmod +x setup.sh && ./setup.sh
```

### Option 2: Manual Setup
```bash
# Clone and setup
git clone https://github.com/codeblazar/mcp-local.git
cd mcp-local

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## What You'll Learn
- How to create an MCP server in Python (24 lines!)
- How to define tools that clients can call
- How MCP uses JSON-RPC 2.0 over stdio for communication
- How to test your MCP server
- Modern MCP patterns (2025 official documentation)

## Files
- **`simple_mcp_server.py`** - The main MCP server (24 lines, modern patterns)
- **`simple_mcp_client.py`** - Test client that shows how to interact with the server
- **`README.md`** - This documentation

## The Server
The server provides one simple tool:
- **`greet`** - Takes a name and returns a friendly greeting

## How to Run (Requires 2 Terminals)

### Terminal 1 - Start the Server:
```bash
cd mcp-local
python simple_mcp_server.py
```
- Server starts and waits for connections
- **No output is normal!** The server runs silently
- Leave this terminal running

### Terminal 2 - Test with the Client:
```bash
cd mcp-local
python simple_mcp_client.py
```

**Expected output:**
```
🧪 Testing MCP Server...
✅ Connecting to server...
✅ Success! Connected to: hello-server
✅ Server has tools: {'listChanged': False}
✅ Found the 'greet' tool: Say hello to someone.
    Args:
        name: The name of the person to greet
    Returns:
        A friendly greeting message
✅ Testing the greet tool...
✅ Tool response: Hello, Simple Test! Welcome to MCP!
✅ Testing greet tool with Alice...
✅ Alice response: Hello, Alice! Welcome to MCP!

🎉 Your MCP server is working correctly!
🔗 It's ready to connect to MCP clients like VS Code
```

**Now the test shows parameter functionality!** It calls the greet tool twice with different names, proving the server correctly processes the `name` parameter.

## How MCP Works (Simplified)

1. **Client connects** to server using JSON-RPC
2. **Server lists its tools** (the `greet` tool)
3. **Client calls the tool** with parameters
4. **Server returns results**

The `simple_mcp_client.py` demonstrates all these steps in action!

## Next Steps

Once your server works:
- Connect it to VS Code
- Add more tools
- Build real applications

## What You Learn

- ✅ **Modern:** Uses 2025 official MCP patterns with FastMCP
- ✅ **Simple:** Just 24 lines for the complete server
- ✅ **Educational:** Shows core MCP concepts clearly
- ✅ **Working:** Actually functional MCP server
- ✅ **Focused:** One clear purpose per file

## Requirements

- Python 3.10 or higher
- `mcp` package (installed via requirements.txt)

## Repository Structure

```
mcp-local/
├── README.md                 # This documentation
├── simple_mcp_server.py      # 24-line MCP server
├── simple_mcp_client.py      # Test client
├── requirements.txt          # Python dependencies
├── setup.bat                 # Windows setup script
├── setup.sh                  # Linux/macOS setup script
├── LICENSE                   # MIT License
└── .gitignore               # Git ignore rules
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with both server and client
5. Submit a pull request

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Support

- For MCP questions: [MCP Documentation](https://modelcontextprotocol.io/)
- For issues with this tutorial: [Create an issue](https://github.com/codeblazar/mcp-local/issues)
