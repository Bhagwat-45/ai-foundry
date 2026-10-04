from openai import OpenAI
from config.config import settings

print(settings.model_name)

client = OpenAI(
    base_url=settings.endpoint,
    api_key=settings.key
)

response = client.responses.create(
    model=settings.model_name,
    input="What is the capital of France?",
)

print(f"answer: {response.output[0]}")
