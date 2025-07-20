#!/usr/bin/env python3
"""
File Listing Example - Educational Code

This standalone script demonstrates how to list files in a directory.
Students can run this to understand the core functionality before
adding it to their MCP server.
"""

import os
from pathlib import Path
import datetime

def list_files_basic(directory_path):
    """Basic file listing using os.listdir()"""
    print(f"\n=== Basic Listing: {directory_path} ===")
    try:
        files = os.listdir(directory_path)
        for file in files:
            print(f"  {file}")
    except FileNotFoundError:
        print(f"  ❌ Directory not found: {directory_path}")
    except PermissionError:
        print(f"  ❌ Permission denied: {directory_path}")

def list_files_detailed(directory_path, include_hidden=False):
    """Detailed file listing using pathlib (modern approach)"""
    print(f"\n=== Detailed Listing: {directory_path} ===")
    try:
        path = Path(directory_path)
        if not path.exists():
            print(f"  ❌ Directory not found: {directory_path}")
            return
        
        if not path.is_dir():
            print(f"  ❌ Not a directory: {directory_path}")
            return
        
        files = []
        for item in path.iterdir():
            # Skip hidden files unless requested
            if not include_hidden and item.name.startswith('.'):
                continue
                
            # Get file info
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
        
        # Sort by name
        files.sort(key=lambda x: x['name'].lower())
        
        # Display results
        print(f"  {'Type':<6} {'Size':<10} {'Modified':<20} {'Name'}")
        print(f"  {'-'*6} {'-'*10} {'-'*20} {'-'*20}")
        
        for file in files:
            size_str = f"{file['size']:,}" if file['type'] == 'FILE' else ""
            print(f"  {file['type']:<6} {size_str:<10} {file['modified']:<20} {file['name']}")
            
        print(f"\n  📁 Total: {len(files)} items")
        
    except PermissionError:
        print(f"  ❌ Permission denied: {directory_path}")
    except Exception as e:
        print(f"  ❌ Error: {e}")

def list_files_for_mcp(directory_path, include_hidden=False):
    """
    File listing formatted for MCP server return value.
    This is what we'll adapt for the MCP server.
    """
    print(f"\n=== MCP Format: {directory_path} ===")
    try:
        path = Path(directory_path)
        if not path.exists():
            return f"❌ Directory not found: {directory_path}"
        
        if not path.is_dir():
            return f"❌ Not a directory: {directory_path}"
        
        files = []
        for item in path.iterdir():
            if not include_hidden and item.name.startswith('.'):
                continue
                
            stat = item.stat()
            files.append({
                'name': item.name,
                'type': 'directory' if item.is_dir() else 'file',
                'size': stat.st_size if item.is_file() else None,
                'modified': datetime.datetime.fromtimestamp(stat.st_mtime).isoformat()
            })
        
        # Sort by name
        files.sort(key=lambda x: x['name'].lower())
        
        # Format for return
        result = f"📁 Directory: {directory_path}\n"
        result += f"📊 Found {len(files)} items\n\n"
        
        for file in files:
            icon = "📁" if file['type'] == 'directory' else "📄"
            size_info = f" ({file['size']:,} bytes)" if file['size'] is not None else ""
            result += f"{icon} {file['name']}{size_info}\n"
        
        print(result)
        return result
        
    except PermissionError:
        error_msg = f"❌ Permission denied: {directory_path}"
        print(error_msg)
        return error_msg
    except Exception as e:
        error_msg = f"❌ Error listing directory: {e}"
        print(error_msg)
        return error_msg

def main():
    """Test the file listing functions"""
    print("🗂️  File Listing Example - Testing Different Approaches")
    print("=" * 60)
    
    # Test directory (current directory)
    test_dir = "."
    
    # Test basic listing
    list_files_basic(test_dir)
    
    # Test detailed listing
    list_files_detailed(test_dir, include_hidden=True)
    
    # Test MCP format (this is what we'll use in the server)
    list_files_for_mcp(test_dir, include_hidden=False)
    
    print("\n🎯 The 'list_files_for_mcp' function above shows what we'll")
    print("   adapt for our MCP server tool!")

if __name__ == "__main__":
    main()
