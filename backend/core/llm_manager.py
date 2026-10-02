import yaml

from backend.llm.ollama import OllamaLLM


class LLMManager:

    def __init__(self):

        with open("config.yaml", "r") as file:
            config = yaml.safe_load(file)

        llm_config = config["llm"]

        provider = llm_config["provider"]
        model = llm_config["model"]

        if provider == "ollama":
            self.llm = OllamaLLM(model)

        else:
            raise ValueError(
                f"Unsupported LLM provider: {provider}"
            )


    def chat(self, message):

        return self.llm.chat(message)