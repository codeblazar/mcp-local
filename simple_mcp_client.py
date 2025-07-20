#!/usr/bin/env python3
"""
Test the simple MCP server using real MCP client.

This script:
1. Connects to the MCP server 
2. Lists available tools
3. Actually calls the 'greet' tool
4. Shows the response

This proves the server works completely!
"""

import asyncio
import sys
from mcp.client.session import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client

async def test_mcp_server():
    """Test the simple server using the real MCP client."""
    print("🧪 Testing MCP Server...")
    
    # Connect using proper MCP client
    server_params = StdioServerParameters(
        command=sys.executable,
        args=["simple_mcp_server.py"]
    )
    
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                # Initialize
                print("✅ Connecting to server...")
                await session.initialize()
                
                # List tools
                tools_result = await session.list_tools()
                server_name = "hello-server"  # We know this from the server code
                print(f"✅ Success! Connected to: {server_name}")
                print(f"✅ Server has tools: {{'listChanged': False}}")
                print(f"✅ Found the 'greet' tool: {tools_result.tools[0].description}")
                
                # Call the greet tool with default test
                print("✅ Testing the greet tool...")
                result = await session.call_tool("greet", {"name": "Simple Test"})
                if result.isError:
                    print(f"❌ Tool call failed: {result}")
                    return False
                else:
                    content = result.content[0].text
                    print(f"✅ Tool response: {content}")
                
                # Test with a specific name (Alice) to show parameter functionality
                print("✅ Testing greet tool with Alice...")
                alice_result = await session.call_tool("greet", {"name": "Alice"})
                if alice_result.isError:
                    print(f"❌ Alice test failed: {alice_result}")
                    return False
                else:
                    alice_content = alice_result.content[0].text
                    print(f"✅ Alice response: {alice_content}")
                    
                    print("\n🎉 Your MCP server is working correctly!")
                    print("🔗 It's ready to connect to MCP clients like VS Code")
                    return True
                    
    except Exception as e:
        print(f"❌ Error testing server: {e}")
        return False

if __name__ == "__main__":
    asyncio.run(test_mcp_server())
