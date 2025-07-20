#!/usr/bin/env python3
"""
Simple MCP Server - Educational Example

This is a minimal Model Context Protocol server that provides one tool.
Students can see how MCP servers work without complex implementation details.

Built following the official MCP documentation patterns (2025).
"""

from mcp.server.fastmcp import FastMCP

# Create the MCP server using FastMCP (official 2025 pattern)
mcp = FastMCP("hello-server")

@mcp.tool()
async def greet(name: str) -> str:
    """Say hello to someone.
    
    Args:
        name: The name of the person to greet
        
    Returns:
        A friendly greeting message
    """
    return f"Hello, {name}! Welcome to MCP!"

# Main entry point - runs the server using stdio transport
if __name__ == "__main__":
    mcp.run(transport='stdio')
