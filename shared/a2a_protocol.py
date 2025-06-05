# Simplified A2A message format (based on Google's protocol)
from typing import Dict
import uuid
import datetime

def create_a2a_message(sender: str, receiver: str, content: str) -> Dict:
    return {
        "id": str(uuid.uuid4()),
        "sender": sender,
        "receiver": receiver,
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "content": content,
    }

def parse_a2a_message(message: Dict) -> str:
    return message.get("content", "")
