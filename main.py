from fastmcp import FastMCP
import requests
mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

@mcp.tool
def get_user_data() -> dict:
    """Get user data without type annotation."""
    return {"name": "Alice", "age": 30, "active": True}


TELEGRAM_API_URL = "https://api.telegram.org/bot7149369788:AAFUZX0YBUlHGurMcrftkBpIcyRdjjZLBtc"

@mcp.tool
def send_message(message: str) -> str:
    """Send a message to the user."""
    try:
        requests.post(
                f"{TELEGRAM_API_URL}/sendMessage",
                json={"chat_id": 6290970561, "text": message},
            )
    except Exception as e:
        return f"Error: {e}"
    return f"message sent"

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8080)