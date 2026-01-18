from clients import OpenRouter
from agent import render_prompt, LLM_CATALOG, ModelConfig, QueryRouterModelOutput
from config import PromptIntent


class IntentRouter:
    client: OpenRouter

    def __init__(self, client: OpenRouter, user_prompt: str):
        self.client = client
        self.user_prompt = user_prompt
        self.system_prompt = render_prompt(
            "prompt_interpreter", prompt=self.user_prompt
        )

    async def determine_prompt_intent(self) -> QueryRouterModelOutput:
        ## should cache this response for the same conversation to decrease response latency, and token usage.
        prompt_intent = await self.client.determine_prompt_type(
            self.system_prompt,
            ModelConfig(
                LLM_CATALOG["FREE"]["CLASSIFICATION"].trainingCutOffDate,
                LLM_CATALOG["FREE"]["CLASSIFICATION"].trainingCutOffDate,
            ),
        )
        if prompt_intent is None:
            return QueryRouterModelOutput(
                thought_process="",
                category=PromptIntent.GENERAL,
                requires_reasoning=False,
                requires_search=False,
            )
        return prompt_intent

    async def route_by_intent(self, intent: str):
        match intent:
            case PromptIntent.JAPANESE:
                return await self.client.translate_japanese(
                    self.user_prompt,
                    "English",
                    ModelConfig(
                        LLM_CATALOG["FREE"]["TRANSLATION"].trainingCutOffDate,
                        LLM_CATALOG["FREE"]["TRANSLATION"].name,
                    ),
                )
            case _:
                return await self.client.solve_general_task(
                    self.user_prompt,
                    ModelConfig(
                        LLM_CATALOG["FREE"]["GENERAL"].trainingCutOffDate,
                        LLM_CATALOG["FREE"]["GENERAL"].name,
                    ),
                )
