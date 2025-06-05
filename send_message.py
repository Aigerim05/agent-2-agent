# send_message.py
import requests
from shared.a2a_protocol import create_a2a_message

message = create_a2a_message(
    sender="Tester",
    receiver="LangChainAgent",
    content="Hi LangChain! Can you greet Llama for me?"
)

response = requests.post("http://localhost:5000/receive", json=message)
print("Sent message. LangChain's response:", response.json())
