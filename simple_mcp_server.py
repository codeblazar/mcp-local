#!/usr/bin/env python3
"""
Simple MCP Server - Educational Example

This is a minimal Model Context Protocol server that provides one tool.
Students can see how MCP servers work without complex implementation details.

Built following the official MCP documentation patterns (2025).
"""

from mcp.server.fastmcp import FastMCP
from pathlib import Path
import os # Add this line for basic file operations
import datetime

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

@mcp.tool()
async def list_files_basic(directory_path: str) -> str:
    """
    List files in a directory (basic version).
    cle
    Args:
        directory_path: Path to the directory to list
        
    Returns:
        String with file names, one per line
    """
    try:
        files = os.listdir(directory_path)
        result = f"Files in {directory_path}:\n"
        for file in files:
            result += f"  {file}\n"
        return result
        
    except FileNotFoundError:
        return f"❌ Directory not found: {directory_path}"
        
    except PermissionError:
        return f"❌ Permission denied: {directory_path}"
    
@mcp.tool()
async def list_files_detailed(directory_path, include_hidden=False):
    """
    Detailed file listing using pathlib (modern approach)
    
    Args:
        directory_path: Path to the directory to list
        include_hidden: Whether to include hidden files (starting with .)
        
    Returns:
        String with detailed file information
    """
    try:
        path = Path(directory_path)
        
        # Check if directory exists
        if not path.exists():
            error_msg = f"❌ Directory not found: {directory_path}"
            return error_msg
        
        # Check if it's actually a directory
        if not path.is_dir():
            error_msg = f"❌ Not a directory: {directory_path}"
            return error_msg
        
        # Collect file information
        files = []
        for item in path.iterdir():
            # Skip hidden files unless requested
            if not include_hidden and item.name.startswith('.'):
                continue
                
            # Get file statistics
            stat = item.stat()
            size = stat.st_size
            modified = datetime.datetime.fromtimestamp(stat.st_mtime)
            file_type = "DIR" if item.is_dir() else "FILE"
            
            files.append({
                'name': item.name,
                'type': file_type,
                'size': size,
                'modified': modified.strftime('%Y-%m-%d %H:%M:%S')
            })
        
        # Sort files by name (case-insensitive)
        files.sort(key=lambda x: x['name'].lower())
        
        # Build formatted result
        result = f"Detailed listing of {directory_path}:\n"
        result += f"{'Type':<6} {'Size':<10} {'Modified':<20} {'Name'}\n"
        result += f"{'-'*6} {'-'*10} {'-'*20} {'-'*20}\n"
        
        for file in files:
            size_str = f"{file['size']:,}" if file['type'] == 'FILE' else ""
            result += f"{file['type']:<6} {size_str:<10} {file['modified']:<20} {file['name']}\n"
            
        result += f"\nTotal: {len(files)} items"
        
        return result
        
    except PermissionError:
        error_msg = f"❌ Permission denied: {directory_path}"
        return error_msg
        
    except Exception as e:
        error_msg = f"❌ Error: {e}"
        return error_msg

@mcp.tool()
async def list_files_mcp_ready(directory_path: str, include_hidden: bool = False) -> str:
    """
    File listing formatted for MCP server return value
    
    Args:
        directory_path: Path to the directory to list
        include_hidden: Whether to include hidden files (starting with .)
        
    Returns:
        String formatted for MCP tool response with clean layout
    """
    try:
        path = Path(directory_path)
        
        # Validation checks
        if not path.exists():
            return f"❌ Directory not found: {directory_path}"
        
        if not path.is_dir():
            return f"❌ Not a directory: {directory_path}"
        
        # Collect file information
        files = []
        for item in path.iterdir():
            # Skip hidden files unless requested
            if not include_hidden and item.name.startswith('.'):
                continue
                
            stat = item.stat()
            files.append({
                'name': item.name,
                'type': 'directory' if item.is_dir() else 'file',
                'size': stat.st_size if item.is_file() else None,
                'modified': datetime.datetime.fromtimestamp(stat.st_mtime).isoformat()
            })
        
        # Sort by name (case-insensitive)
        files.sort(key=lambda x: x['name'].lower())
        
        # Format for MCP response - user-friendly without problematic emojis
        result = f"Directory: {directory_path}\n"
        result += f"Found {len(files)} items\n\n"
        
        for file in files:
            icon = "[DIR]" if file['type'] == 'directory' else "[FILE]"
            size_info = f" ({file['size']:,} bytes)" if file['size'] is not None else ""
            result += f"{icon} {file['name']}{size_info}\n"
        
        return result
        
    except PermissionError:
        return f"❌ Permission denied: {directory_path}"
        
    except Exception as e:
        return f"❌ Error listing directory: {e}"

# Main entry point - runs the server using stdio transport
if __name__ == "__main__":
    mcp.run(transport='stdio')