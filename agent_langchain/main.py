from flask import Flask, request, jsonify
from agent_langchain.agent import handle_message
from shared.a2a_protocol import create_a2a_message, parse_a2a_message
import requests

app = Flask(__name__)

AGENT_ID = "LangChainAgent"
RECEIVER_URL = "http://localhost:5001/receive"  # llama's endpoint

@app.route("/receive", methods=["POST"])
def receive():
    message = request.json
    print(f"[LangChainAgent] Received:", message)

    response_text = handle_message(parse_a2a_message(message))
    response_msg = create_a2a_message(AGENT_ID, "LlamaAgent", response_text)

    requests.post(RECEIVER_URL, json=response_msg)
    return jsonify({"status": "ok", "response_sent": response_text})

if __name__ == "__main__":
    app.run(port=5000)
