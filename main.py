from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

@mcp.tool
def get_user_data() -> dict:
    """Get user data without type annotation."""
    return {"name": "Alice", "age": 30, "active": True}

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8080)