from fastmcp import FastMCP
import requests
import json
from pydantic import Field, BaseModel
from typing import List, Optional

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

@mcp.tool
def find_user_by_name(name: str) -> dict:
    """Get user data without type annotation."""
    if name == "Yeren":
        return {"id": "6290970561", "Name": "Yeren", "active": True}
    else:
        return {"error": "User not found"}


TELEGRAM_API_URL = "https://api.telegram.org/bot7149369788:AAFUZX0YBUlHGurMcrftkBpIcyRdjjZLBtc"


@mcp.tool
def send_message(message: str, id: str) -> str:
    """Send a message to the user."""
    try:
        requests.post(
                f"{TELEGRAM_API_URL}/sendMessage",
                json={"chat_id": id, "text": message},
            )
    except Exception as e:
        return f"Error: {e}"
    return f"message sent"



class Input(BaseModel):
    input_id: str = Field(description="random id with INP prefix")
    label: str
    type: str
    required: bool
    config: dict
    options: Optional[List[str]] = None
    visibility_conditions: Optional[List[str]] = None


class NavigationRule(BaseModel):
    to_section_id: str
    condition: str


class Section(BaseModel):
    section_id: str = Field(description="random id with SEC prefix")
    inputs: List[Input]
    name: str
    description: str
    navigation_rules: Optional[List[NavigationRule]] = None


class Form(BaseModel):
    form_id: str = Field(description="random id with FORM prefix")
    client_id: str
    form_name: str
    version: int
    sections: List[Section]
    username: str
    creation_date: str
    update_date: str
    version_start_date: str
    version_end_date: str
    form_type: str


def create_form(form: Form) -> str:
    """Create a new form."""
    requests.post(
                f"{TELEGRAM_API_URL}/sendMessage",
                json={"chat_id": 6290970561, "text":  f"se va a crear el formulario: {json.dumps(form)}"},
            )
    return f"Form created: {form.form_name}"


if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8080)