# MCP File System Tools - Building Practical MCP Tools

## Overview
This guide shows you how to extend your simple MCP server with practical file system tools. You'll learn to add real-world functionality that makes your MCP server genuinely useful for development workflows.

## What You'll Build
By the end of this tutorial, your MCP server will have these new tools:
- **`list_files`** - List files and directories with details
- **`read_file_content`** - Read and display file contents  
- **`create_file`** - Create new files with content
- **`search_files`** - Find files by name patterns

## Prerequisites
✅ Complete the basic MCP setup from `VSCODE_MCP_SETUP.md`
✅ Have your `simple_mcp_server.py` working with the `greet` tool
✅ VS Code MCP extension connected and working

## Learning Approach
We'll use a **step-by-step progression**:
1. **Understand the code** - Run standalone Python examples
2. **Add to MCP server** - Integrate one tool at a time
3. **Test each tool** - Verify it works in VS Code Copilot
4. **Build complexity** - Add more sophisticated features

---

## Step 1: Basic File Listing (Learning Phase)

We'll learn file operations through three progressive examples. Each builds on the previous one, teaching you new concepts step by step.

### 1.1 Run the Basic Example

First, let's understand the simplest approach to listing files:

```bash
# In your C:\mcp directory
python step1_basic_listing.py
```

**What you'll see:**
- Simple file listing using `os.listdir()`
- Basic error handling for missing directories
- Clean, readable output format

**Study the code in `step1_basic_listing.py`:**
- How `os.listdir()` works
- Try/except blocks for error handling
- String formatting for user-friendly output

### 1.2 Understanding the Basic Code

Open `step1_basic_listing.py` and examine:

**Key Python concepts:**
```python
import os  # Built-in module for operating system interface

# Basic file listing
files = os.listdir(directory_path)

# Error handling
try:
    # File operation here
except FileNotFoundError:
    return "Directory not found"
except PermissionError:
    return "Permission denied"
```

**Why this approach:**
- ✅ Simple and easy to understand
- ✅ Uses basic Python built-ins
- ✅ Good error handling foundation
- ❌ Limited information (names only)
- ❌ No file details or filtering

---

### 1.3 Adding Basic Listing to Your MCP Server

Now let's integrate the basic file listing into your MCP server. We'll do this step-by-step so you understand every part.

**Step A: Backup Your Current Server**
```bash
copy simple_mcp_server.py simple_mcp_server_backup.py
```

**Step B: Add Required Imports**
Open `simple_mcp_server.py` and add this import at the top (after the existing imports):

```python
import os  # Add this line for basic file operations
```

**Step C: Add the Basic Listing Tool**
Add this new tool function after your existing `greet` tool:

```python
@mcp.tool()
async def list_files_basic(directory_path: str) -> str:
    """
    List files in a directory (basic version).
    
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
```

**Step D: Test Your Enhanced Server**

1. **Test with the client:**
   ```bash
   python simple_mcp_client.py
   ```
   You should see both `greet` and `list_files_basic` tools available.

2. **Test in VS Code:**
   - Restart VS Code if needed (to refresh the MCP connection)
   - In Copilot Chat, try: "List the files in the current directory using the basic method"

**Step E: Verify It Works**
Your MCP server now has TWO tools:
- ✅ `greet` - Your original greeting tool
- ✅ `list_files_basic` - Your new file listing tool

---

## Step 2: Detailed File Listing (Advancing Skills)

Now let's learn the modern, more powerful approach using `pathlib`.

### 2.1 Run the Detailed Example

```bash
python step2_detailed_listing.py
```

**What's new here:**
- Modern `pathlib.Path` instead of `os.listdir()`
- File details: size, type (file/directory), modification time
- Better formatting with columns
- Option to include/exclude hidden files

### 2.2 Study the Advanced Code

Open `step2_detailed_listing.py` and examine:

**Key improvements:**
```python
from pathlib import Path  # Modern file handling
import datetime           # For formatting timestamps

# Modern path handling
path = Path(directory_path)
if path.exists() and path.is_dir():
    for item in path.iterdir():
        stat = item.stat()  # Get file details
        size = stat.st_size
        is_dir = item.is_dir()
```

**Why this is better:**
- ✅ More file information (size, type, date)
- ✅ Cross-platform path handling
- ✅ Better control over what to include
- ✅ Professional formatting
- ✅ Modern Python best practices

### 2.3 Your Challenge: Add Detailed Listing to MCP Server

**Your task:** Following the same pattern as Step 1, add the detailed listing function to your MCP server.

**Hints:**
1. Add the required imports (`from pathlib import Path` and `import datetime`)
2. Copy the `list_files_detailed` function
3. Convert it to an `@mcp.tool()` with proper async signature
4. Test it with both the client and VS Code

**Expected result:** Your MCP server will have THREE tools:
- `greet`
- `list_files_basic` 
- `list_files_detailed`

---

## Step 3: MCP-Ready Listing (Production Quality)

The final step creates a tool optimized for MCP responses.

### 3.1 Run the MCP-Ready Example

```bash
python step3_mcp_ready.py
```

**What makes this "MCP-ready":**
- Clean, user-friendly output with emojis
- Optimized for chat interface display
- Consistent error message format
- No debug print statements
- Ready for production use

### 3.2 Study the Production Code

Open `step3_mcp_ready.py` and notice:

**Professional touches:**
```python
# User-friendly formatting
result = f"📁 Directory: {directory_path}\n"
result += f"📊 Found {len(files)} items\n\n"

# Clean emoji-based display
icon = "📁" if file['type'] == 'directory' else "📄"
result += f"{icon} {file['name']}{size_info}\n"

# No print statements - just return values
return result  # Not print(result)
```

### 3.3 Your Final Challenge: Complete the MCP Integration

**Your task:** Add the MCP-ready listing tool to your server.

**Success criteria:**
1. ✅ Add all three file listing tools to your MCP server
2. ✅ All tools work in VS Code Copilot Chat
3. ✅ You understand the progression from basic → detailed → production
4. ✅ You can test each tool independently

**Expected final result:** Your MCP server will have FOUR tools:
- `greet` (original)
- `list_files_basic` (Step 1)
- `list_files_detailed` (Step 2) 
- `list_files_mcp_ready` (Step 3)

---

## Step 5: Real-World Usage Examples

Once all tools are working, students can use them for:

### Development Workflows
- **"List all Python files in my src directory"**
- **"Show me the contents of my config file"**  
- **"Create a new module file with basic structure"**
- **"Find all files modified today"**

### Project Management
- **"List all markdown files for documentation"**
- **"Show me the project README"**
- **"Create a TODO file with my task list"**

---

## Educational Benefits

### Python Skills Students Learn
- ✅ **Modern file handling** with `pathlib`
- ✅ **Error handling** with try/catch blocks
- ✅ **JSON formatting** for structured returns
- ✅ **Cross-platform** path handling
- ✅ **File metadata** access and formatting

### MCP Development Skills
- ✅ **Adding tools incrementally** to existing servers
- ✅ **Tool parameter design** (required vs optional)
- ✅ **Return value formatting** for user-friendly output
- ✅ **Error handling** in distributed systems

### Real-World Applications
- ✅ **Development automation** tools
- ✅ **File management** utilities  
- ✅ **Build system** helpers
- ✅ **Documentation** generators

---

## Troubleshooting Guide

### Common Issues

**Tool not appearing in VS Code:**
- Restart the MCP server
- Check VS Code Output panel for errors
- Verify tool syntax is correct

**Permission errors:**
- Use relative paths when possible
- Test with accessible directories first
- Handle errors gracefully in tool code

**Path issues on Windows:**
- Use `pathlib.Path` for cross-platform compatibility
- Avoid hardcoded path separators
- Use forward slashes or `Path.joinpath()`

---

## Next Steps

After completing this tutorial:
1. **Experiment** with your file tools in real projects
2. **Add more tools** like file copying, moving, or analysis
3. **Integrate with other systems** like Git or build tools
4. **Share your server** with classmates or colleagues

---

## Success Criteria

You'll know you've succeeded when:
- [ ] All file tools work reliably in VS Code Copilot
- [ ] You can perform real file operations through chat
- [ ] The tools handle errors gracefully
- [ ] You understand how to add new tools independently

**Ready to start building?** Let's begin with Step 1!
