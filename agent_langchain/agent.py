from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7, openai_api_key=os.environ.get("OPENAI_API_KEY"))

def handle_message(content: str) -> str:
    response = llm([HumanMessage(content=content)])
    return response.content
