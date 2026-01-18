from typing import TypedDict


class Prompt(TypedDict):
    role: str
    prompt: str


class Model(TypedDict):
    name: str
    trainingCutOffDate: str
