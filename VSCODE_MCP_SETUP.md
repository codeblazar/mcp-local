# VS Code MCP Server Setup Worksheet

## Overview
This worksheet provides step-by-step instructions to connect your `simple_mcp_server.py` to VS Code using the Copilot MCP extension.

## Prerequisites Checklist
- [ ] VS Code installed
- [ ] Python virtual environment set up (`venv/` folder exists)
- [ ] MCP package installed (`pip install mcp`)
- [ ] Your `simple_mcp_server.py` file is working
- [ ] Copilot MCP extension installed in VS Code

## Step 1: Install Copilot MCP Extension
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "Copilot MCP" or "Model Context Protocol"
4. Install the official Microsoft Copilot MCP extension
5. Restart VS Code if prompted

## Step 2: Test Your MCP Server
Before connecting to VS Code, verify your server works:

1. Open terminal in your project directory (`c:\mcp`)
2. Activate virtual environment:
   ```bash
   .\venv\Scripts\Activate.ps1
   ```
3. Test the server with the client:
   ```bash
   python simple_mcp_client.py
   ```
4. Verify you see success messages with greetings

## Step 2.1: Understanding MCP Server Types
Before adding your server, it's helpful to understand the different server types available:

- **Command (stdio)**: Run a local command that implements the MCP protocol
- **HTTP (HTTP or Server-Sent Events)**: Connect to a remote HTTP server that implements the MCP protocol
- **NPM Package**: Install from an NPM package name
- **Pip Package**: Install from a Pip package name
- **Docker Image**: Install from a Docker image
- **Browse MCP Servers...**: Browse available MCP servers online

**For this tutorial, you'll use "Command (stdio)" since you're running your local Python script.**

## Step 3: Add MCP Server in VS Code
1. Open VS Code Command Palette (Ctrl+Shift+P)
2. Type "MCP: Add Server"
3. Select the "MCP: Add Server" command
4. Choose server type: **Command (stdio)** - "Run a local command that implements the MCP protocol"

## Step 4: Server Configuration
When you select "Command (stdio)", you'll see a command input field:

**Enter Command:** Type the full command with arguments
```
C:\mcp\venv\Scripts\python.exe C:\mcp\simple_mcp_server.py
```

**Important:** Enter the complete command in a single line with the Python executable path followed by your script path.

## Step 4.1: Server ID Confirmation
After entering the command, VS Code will ask you to confirm a **Server ID**. You might see something like:
- `my-mcp-server-81989332`

**About the Random Numbers:** The extension automatically generates random numbers (like `81989332`) to ensure unique server identifiers. This prevents conflicts if multiple servers have similar names.

**You CAN change this ID!** Replace the auto-generated name with something more meaningful like:
- `hello-server`
- `simple-mcp-server` 
- `my-local-server`
- `greet-tool-server`

The server ID is just a friendly name for your configuration - use whatever makes sense to you!

## Step 4.2: Choose Installation Location
After confirming your server ID, VS Code will ask **where to install** the MCP server configuration:

**Recommended: Choose "Workspace"**
- **Workspace**: Installs the server only for this specific project (`c:\mcp`)
- **User**: Installs the server globally for all VS Code instances

For this tutorial, select **Workspace** to keep your setup contained to this project.

## Step 4.3: Configuration Saved and Tools Detected
After choosing "Workspace", VS Code will:
1. **Save the configuration** to `.vscode/mcp.json` in your project
2. **Start your MCP server** automatically
3. **Detect available tools** (like your `greet` tool)
4. **Show a notification**: "New tools available" with a refresh button

**Click the refresh button** when you see this notification - this activates your tools for Copilot Chat!

## Step 4.4: Understanding the Command Format
The command input expects the full command line as you would type it in a terminal:
- **Format**: `[executable] [script] [arguments]`
- **Example**: `C:\mcp\venv\Scripts\python.exe C:\mcp\simple_mcp_server.py`
- **Note**: Use absolute paths to avoid path resolution issues

## Step 4.4: Server ID Naming
When prompted for a server ID, you can choose a meaningful name instead of accepting the auto-generated one with random numbers.

## Step 5: Alternative Server Types (Reference)
For reference, here are the other server types available:

- **Command (stdio)**: Run a local command that implements the MCP protocol (use this for your Python server)
- **HTTP (HTTP or Server-Sent Events)**: Connect to a remote HTTP server that implements the MCP protocol
- **NPM Package**: Install from an NPM package name - for Node.js MCP servers
- **Pip Package**: Install from a Pip package name - for Python MCP packages
- **Docker Image**: Install from a Docker image - for containerized MCP servers
- **Browse MCP Servers...**: Browse and discover available MCP servers online

## Step 6: Alternative Configuration Methods

### Manual JSON Configuration (Advanced)
If you need to manually edit settings, you can add this to your VS Code `settings.json`:

```json
{
  "mcp.servers": [
    {
      "name": "hello-server",
      "command": "C:\\mcp\\venv\\Scripts\\python.exe",
      "args": ["C:\\mcp\\simple_mcp_server.py"]
    }
  ]
}
```

## Step 7: Complete the Setup
1. After entering the command, press **Enter** to confirm
2. VS Code will add the server to your configuration
3. The server should start automatically

## Step 8: Test the Connection
1. Open Copilot Chat in VS Code
2. Try using the `greet` tool from your server
3. Example prompt: "Use the greet tool to say hello to Alice"
4. You should see the response: "Hello, Alice! Welcome to MCP!"

## Troubleshooting Checklist

### If connection fails:
- [ ] Check Python path is correct (use absolute paths)
- [ ] Verify virtual environment is activated
- [ ] Ensure `mcp` package is installed in the venv
- [ ] Check VS Code Output panel for MCP logs
- [ ] Restart VS Code completely
- [ ] Test server independently with `simple_mcp_client.py`

### Common Issues:
- **Path separators:** Use `\\` or `/` in JSON, not single `\`
- **Virtual environment:** Make sure to use the Python from your venv
- **Working directory:** Set to your project folder
- **Permissions:** Ensure VS Code can execute your Python script

## Step 9: Verify Tools Are Available
1. In Copilot Chat, check if your tools are listed
2. Try calling: "What tools do you have available?"
3. Look for the `greet` tool in the response

## Success Indicators
- [ ] MCP server shows as "Connected" in VS Code
- [ ] Copilot can see and use your `greet` tool
- [ ] Tool calls return expected responses
- [ ] No error messages in VS Code Output panel

## Next Steps
Once connected successfully:
- [ ] Test different prompts using your tool
- [ ] Monitor VS Code Output panel for MCP logs
- [ ] Consider adding more tools to your server
- [ ] Document your working configuration

## Configuration Backup
Save your working configuration details here for future reference:

**Python Path Used:**
```
_________________________________
```

**Server Arguments:**
```
_________________________________
```

**VS Code MCP Settings Location:**
```
_________________________________
```

---

**Note:** The exact steps may vary slightly depending on the Copilot MCP extension version. Refer to the extension's documentation for the most current setup process.
