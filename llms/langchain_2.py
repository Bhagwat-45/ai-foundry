from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv

load_dotenv

llm = init_chat_model(
    model=os.getenv("AZURE_MODEL_NAME"),
    api_key=os.getenv("AZURE_KEY"),
    base_url=os.getenv("AZURE_ENDPOINT")
)

print(llm.invoke("What is the capital of France?"))