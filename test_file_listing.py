#!/usr/bin/env python3
"""
Test file listing using the MCP server.

This script:
1. Connects to the MCP server 
2. Lists available tools
3. Calls the file listing tools to show directory contents
4. Demonstrates both basic and detailed file listing
"""

import asyncio
import sys
import os
from mcp.client.session import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client

async def test_file_listing():
    """Test the file listing tools using the MCP server."""
    print("📁 Testing MCP File Listing Tools...")
    
    # Connect using proper MCP client
    server_params = StdioServerParameters(
        command=sys.executable,
        args=["simple_mcp_server.py"]
    )
    
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                # Initialize
                print("✅ Connecting to MCP server...")
                await session.initialize()
                
                # List tools
                tools_result = await session.list_tools()
                print(f"✅ Connected! Server has {len(tools_result.tools)} tools available:")
                
                # Show all available tools
                for i, tool in enumerate(tools_result.tools):
                    print(f"  {i+1}. '{tool.name}': {tool.description}")
                
                # Get current directory for testing
                current_dir = os.getcwd()
                print(f"\n📂 Testing with current directory: {current_dir}")
                
                # Test basic file listing
                print("\n=== BASIC FILE LISTING ===")
                basic_result = await session.call_tool("list_files_basic", {"directory_path": current_dir})
                if basic_result.isError:
                    print(f"❌ Basic listing failed: {basic_result}")
                else:
                    content = basic_result.content[0].text
                    print(content)
                
                # Test detailed file listing
                print("\n=== DETAILED FILE LISTING ===")
                detailed_result = await session.call_tool("list_files_detailed", {"directory_path": current_dir, "include_hidden": False})
                if detailed_result.isError:
                    print(f"❌ Detailed listing failed: {detailed_result}")
                else:
                    content = detailed_result.content[0].text
                    print(content)
                
                # Test detailed file listing with hidden files
                print("\n=== DETAILED FILE LISTING (including hidden files) ===")
                detailed_hidden_result = await session.call_tool("list_files_detailed", {"directory_path": current_dir, "include_hidden": True})
                if detailed_hidden_result.isError:
                    print(f"❌ Detailed listing with hidden files failed: {detailed_hidden_result}")
                else:
                    content = detailed_hidden_result.content[0].text
                    print(content)
                    
                print("\n🎉 File listing tests completed successfully!")
                return True
                    
    except Exception as e:
        print(f"❌ Error testing file listing: {e}")
        return False

if __name__ == "__main__":
    asyncio.run(test_file_listing())