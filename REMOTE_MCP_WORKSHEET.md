# Connect to Weather MCP Server - Quick Worksheet

## Overview
Learn how to connect VS Code to a public weather MCP server in just 5 minutes.

## Prerequisites
- ✅ VS Code with MCP extension installed
- ✅ Internet connection
- ✅ Node.js installed (for npx command)

## Exercise: Add Weather MCP Server

### Step 1: Open VS Code Settings
1. Open VS Code
2. Press `Ctrl+,` (or `Cmd+,` on Mac) to open Settings
3. Click the `{}` icon (top-right) to open `settings.json`

### Step 2: Add Weather Server Configuration
Add this to your `settings.json`:

```json
{
  "mcp.servers": {
    "weather": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-weather"
      ]
    }
  }
}
```

### Step 3: Restart VS Code
- Close VS Code completely
- Reopen VS Code
- Wait for MCP to initialize (look for MCP status in status bar)

### Step 4: Test the Weather Server
1. Open GitHub Copilot Chat (Ctrl+Shift+I)
2. Ask: **"What's the weather like in New York?"**
3. You should get current weather data!

## ✅ Verification
You should see:
- MCP indicator in VS Code status bar
- Weather data in Copilot Chat response
- Real-time temperature, conditions, etc.

## Try These Queries
- "What's the weather in London?"
- "Is it raining in Seattle?"
- "What's the temperature in Tokyo?"
- "Tell me about the weather in Paris"

## Troubleshooting

**Server not working?**
- Restart VS Code completely
- Check you have Node.js installed: `node --version`
- Look for errors in VS Code Output panel (MCP logs)

**No weather data?**
- Make sure you have internet connection
- Try a different city name
- Check MCP extension is enabled

## Summary
🎉 **You did it!** You've successfully:
- ✅ Connected to a public MCP server
- ✅ Used external weather tools in VS Code
- ✅ Experienced MCP's power with real data

**Time to complete:** ~5 minutes

**What's next?** Explore other public MCP servers in the official registry!
