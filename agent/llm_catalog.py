from typing import TypedDict


class ModelConfig:
    def __init__(self, trainingCutOffDate: str, name: str):
        self.trainingCutOffDate = trainingCutOffDate
        self.name = name


class TierModels(TypedDict):
    GENERAL: ModelConfig
    CLASSIFICATION: ModelConfig
    TRANSLATION: ModelConfig


class LLMCatalog(TypedDict):
    FREE: TierModels


LLM_CATALOG: LLMCatalog = {
    "FREE": {
        "GENERAL": ModelConfig(
            "31, December, 2021", "meta-llama/llama-3.1-405b-instruct:free"
        ),
        "CLASSIFICATION": ModelConfig(
            "31, December, 2021", "meta-llama/llama-3.1-405b-instruct:free"
        ),
        "TRANSLATION": ModelConfig(
            "01, August, 2024", "google/gemini-2.0-flash-exp:free"
        ),
    }
}
