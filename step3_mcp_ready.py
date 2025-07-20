#!/usr/bin/env python3
"""
Step 3: MCP-Ready File Listing

This version formats output for MCP server integration.
Students learn how to format data for use in distributed systems.
"""

from pathlib import Path
import datetime

def list_files_mcp_ready(directory_path, include_hidden=False):
    """
    File listing formatted for MCP server return value
    
    Args:
        directory_path: Path to the directory to list
        include_hidden: Whether to include hidden files (starting with .)
        
    Returns:
        String formatted for MCP tool response with emojis and clean layout
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
        
        # Format for MCP response - user-friendly with emojis
        result = f"📁 Directory: {directory_path}\n"
        result += f"Found {len(files)} items\n\n"
        
        for file in files:
            icon = "📁" if file['type'] == 'directory' else "📄"
            size_info = f" ({file['size']:,} bytes)" if file['size'] is not None else ""
            result += f"{icon} {file['name']}{size_info}\n"
        
        return result
        
    except PermissionError:
        return f"❌ Permission denied: {directory_path}"
        
    except Exception as e:
        return f"❌ Error listing directory: {e}"

def main():
    """Test the MCP-ready file listing function"""
    print("🚀 Step 3: MCP-Ready File Listing")
    print("=" * 40)
    
    # Test with current directory
    result = list_files_mcp_ready(".")
    print("MCP Tool Response:")
    print(result)
    
    print("\n" + "="*50)
    print("Testing with non-existent directory:")
    error_result = list_files_mcp_ready("does_not_exist")
    print(error_result)

if __name__ == "__main__":
    main()
