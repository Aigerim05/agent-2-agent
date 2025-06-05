from llama_index.llms.openai import OpenAI
from llama_index.core.base.llms.types import ChatMessage, MessageRole
import os
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def handle_message(content: str) -> str:
    messages = [
        ChatMessage(role=MessageRole.USER, content=content)
    ]
    response = llm.chat(messages)
    return response.message.content
