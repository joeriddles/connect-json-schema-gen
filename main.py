import os

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

import model

ollama_model = OpenAIModel(
    model_name="llama3.2",
    base_url="http://localhost:11434/v1",
    api_key=os.environ["OPENAI_API_KEY"],
)
agent = Agent(ollama_model, result_type=model.SynadiaConnectComponent)

if __name__ == "__main__":
    result = agent.run_sync("Populate this JSON Schema")
    print(result.data)
    # print(result.usage())
