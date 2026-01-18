from typing import NamedTuple


class PromptTemplateTitles(NamedTuple):
    japanese: str = "japanese_translation"
    general: str = "general_task_prompt"
    prompt_interpreter: str = "prompt_interpreter_template"


PROMPT_TEMPLATE_TITLES = PromptTemplateTitles()
