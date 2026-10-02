import yaml

from backend.llm.ollama import OllamaLLM
from backend.llm.freellmapi import FreeLLMAPI


class LLMManager:

    def __init__(self):

        with open("config.yaml", "r") as file:
            config = yaml.safe_load(file)

        llm_config = config["llm"]

        provider = llm_config["provider"]
        model = llm_config["model"]

        providers = {
            "ollama": OllamaLLM,
            "freellmapi": FreeLLMAPI
        }

        if provider in providers:
            self.llm = providers[provider](model)

        else:
            raise ValueError(
                f"Unsupported LLM provider: {provider}"
            )


    def chat(self, message):

        response = self.llm.chat(message)

        if not isinstance(response, str):
            raise TypeError(
                "LLM provider must return a string"
            )

        return response