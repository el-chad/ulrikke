import instructor
from openai import AsyncOpenAI
from functools import lru_cache
from typing import TypedDict
from config import get_settings
from agent import render_prompt, ModelConfig, QueryRouterModelOutput


class Model(TypedDict):
    name: str
    trainingCutOffDate: str


class OpenRouter:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url
        self.raw_client = AsyncOpenAI(base_url=base_url, api_key=api_key)
        self.strict_client = instructor.from_openai(
            self.raw_client, mode=instructor.Mode.JSON
        )

    async def translate_japanese(
        self,
        text: str,
        output_language: str,
        model: ModelConfig,
    ):
        return await self.raw_client.chat.completions.create(
            model=model.name,
            messages=[
                {
                    "role": "system",
                    "content": render_prompt(
                        "japanese_translation", language=output_language
                    ),
                },
                {
                    "role": "user",
                    "content": f"<input_text>\n{text}\n</input_text>",
                },
            ],
        )

    async def determine_prompt_type(self, user_prompt: str, model: ModelConfig):
        return await self.strict_client.chat.completions.create(
            model=model.name,
            messages=[
                {
                    "role": "system",
                    "content": render_prompt(
                        "prompt_interpreter",
                        modelTrainingCutOff=model.trainingCutOffDate,
                    ),
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
            temperature=0,
            response_model=QueryRouterModelOutput,
        )

    async def solve_general_task(self, prompt: str, model: ModelConfig):
        return await self.raw_client.chat.completions.create(
            model=model.name,
            messages=[
                {"role": "system", "content": render_prompt("general_prompt")},
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0,
        )


@lru_cache
def get_open_router_client() -> OpenRouter:
    settings = get_settings()
    return OpenRouter(settings.OPEN_ROUTER_API_KEY, settings.OPEN_ROUTER_BASE_URL)
