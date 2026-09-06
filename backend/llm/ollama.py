from backend.llm.base import BaseLLM
import ollama


class OllamaLLM(BaseLLM):

    def __init__(self, model="qwen3:14b"):
        self.model = model


    def chat(self, message: str) -> str:

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return response["message"]["content"]