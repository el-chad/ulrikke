from enum import StrEnum


class PromptIntent(StrEnum):
    JAPANESE = "JP"
    GENERAL = "GENERAL"
    JAPANESE_GRAMMAR = "JP_GRAMMAR"
    PROJECT = "PROJECT"
