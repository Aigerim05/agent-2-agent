from flask import Flask, request, jsonify
from agent_llama.agent import handle_message
from shared.a2a_protocol import create_a2a_message, parse_a2a_message
import requests

app = Flask(__name__)

AGENT_ID = "LlamaAgent"
RECEIVER_URL = "http://localhost:5000/receive"  # langchain's endpoint

@app.route("/receive", methods=["POST"])
def receive():
    message = request.json
    print(f"[LlamaAgent] Received:", message)

    response_text = handle_message(parse_a2a_message(message))
    response_msg = create_a2a_message(AGENT_ID, "LangChainAgent", response_text)

    requests.post(RECEIVER_URL, json=response_msg)
    return jsonify({"status": "ok", "response_sent": response_text})

if __name__ == "__main__":
    app.run(port=5001)
