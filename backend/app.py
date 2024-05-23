from typing import Dict, List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# CORS middleware for handling Cross-Origin Resource Sharing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

STORAGE_FILE = 'messages.json'


def load_messages() -> List[str]:
    """Load messages from storage file."""
    try:
        with open(STORAGE_FILE, 'r') as f:
            messages = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        messages = []
    return messages


def save_messages(messages: List[str]):
    """Save messages to storage file."""
    with open(STORAGE_FILE, 'w') as f:
        json.dump(messages, f)


def add_message(text: str):
    """Add a new message to storage."""
    messages = load_messages()
    messages.append(text)
    save_messages(messages)


def get_messages() -> List[str]:
    """Get all messages from storage."""
    return load_messages()


class Message(BaseModel):
    """Message model."""
    text: str


@app.post("/slack/events")
async def handle_slack_event(payload: Dict):
    """Handle incoming Slack events."""
    if not isinstance(payload, dict):
        raise HTTPException(status_code=400, detail="Invalid request format")

    if payload.get("type") == "url_verification":
        return {"challenge": payload.get("challenge")}

    event = payload.get("event")
    if not event or event.get("type") != "message":
        return {"message": "Unsupported event type"}

    message = event.get("text")
    if message and "Support" not in message:
        # Do something with the message, for example, store it
        return {"message": f"Received message: {message}"}
    else:
        return {"message": "No message found in the event"}


@app.get("/slack/messages")
async def fetch_messages():
    """Fetch all messages."""
    messages = get_messages()
    return {"messages": messages}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8080)