from pydantic import BaseModel
from typing import Literal


class Message(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str


class ChatCompletionRequest(BaseModel):
    model: str
    messages: list[Message]
    stream: bool = False
    temperature: float | None = None
    max_tokens: int | None = None
    top_p: float | None = None
    frequency_penalty: float | None = None
    presence_penalty: float | None = None
    activatedCharacterID: str | None = None

    class Config:
        extra = "ignore"


class QueryRouterModelOutput(BaseModel):
    thought_process: str
    category: Literal["JP", "TECH", "GENERAL", "PROJECT"]
    requires_search: bool
    requires_reasoning: bool
