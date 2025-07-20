#!/usr/bin/env python3
"""
Step 2: Detailed File Listing

This version adds file details like size, type, and modification time.
Students learn modern Python pathlib and data formatting.
"""

from pathlib import Path
import datetime

def list_files_detailed(directory_path, include_hidden=False):
    """
    Detailed file listing using pathlib (modern approach)
    
    Args:
        directory_path: Path to the directory to list
        include_hidden: Whether to include hidden files (starting with .)
        
    Returns:
        String with detailed file information
    """
    print(f"📁 Detailed listing of: {directory_path}")
    
    try:
        path = Path(directory_path)
        
        # Check if directory exists
        if not path.exists():
            error_msg = f"❌ Directory not found: {directory_path}"
            print(error_msg)
            return error_msg
        
        # Check if it's actually a directory
        if not path.is_dir():
            error_msg = f"❌ Not a directory: {directory_path}"
            print(error_msg)
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
        
        print(result)
        return result
        
    except PermissionError:
        error_msg = f"❌ Permission denied: {directory_path}"
        print(error_msg)
        return error_msg
        
    except Exception as e:
        error_msg = f"❌ Error: {e}"
        print(error_msg)
        return error_msg

def main():
    """Test the detailed file listing function"""
    print("🚀 Step 2: Detailed File Listing")
    print("=" * 40)
    
    # Test with current directory
    list_files_detailed(".")
    
    print("\n" + "="*50)
    print("Including hidden files:")
    list_files_detailed(".", include_hidden=True)

if __name__ == "__main__":
    main()
