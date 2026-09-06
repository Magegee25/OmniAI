from backend.llm.base import BaseLLM


class FakeLLM(BaseLLM):

    def chat(self, message: str) -> str:

        return f"Fake AI received: {message}"