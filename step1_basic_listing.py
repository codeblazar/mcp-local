#!/usr/bin/env python3
"""
Step 1: Basic File Listing

This is the simplest way to list files in Python.
Students will learn basic file operations and error handling.
"""

import os

def list_files_basic(directory_path):
    """
    Basic file listing using os.listdir()
    
    Args:
        directory_path: Path to the directory to list
        
    Returns:
        String with file names, one per line
    """
    print(f"📁 Listing files in: {directory_path}")
    
    try:
        # Get list of files and directories
        files = os.listdir(directory_path)
        
        # Create result string
        result = f"Files in {directory_path}:\n"
        for file in files:
            result += f"  {file}\n"
        
        print(result)
        return result
        
    except FileNotFoundError:
        error_msg = f"❌ Directory not found: {directory_path}"
        print(error_msg)
        return error_msg
        
    except PermissionError:
        error_msg = f"❌ Permission denied: {directory_path}"
        print(error_msg)
        return error_msg

def main():
    """Test the basic file listing function"""
    print("🚀 Step 1: Basic File Listing")
    print("=" * 40)
    
    # Test with current directory
    list_files_basic(".")
    
    # Test with a directory that doesn't exist
    print("\nTesting error handling:")
    list_files_basic("nonexistent_directory")

if __name__ == "__main__":
    main()
