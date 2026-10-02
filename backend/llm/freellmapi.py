from backend.llm.base import BaseLLM


class FreeLLMAPI(BaseLLM):

    def __init__(self, model):
        self.model = model


    def chat(self, message):
        return "FreeLLMAPI provider is not connected yet."