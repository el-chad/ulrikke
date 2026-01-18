from .typings import Dataset
from clients.lang_smith import LangSmithClient


PROMPT_INTERPRETER_DATASET: Dataset = {
    "name": "prompt-interpreter-dataset",
    "description": "Test cases for prompt interpreter classification",
    "examples": [
        # JP category
        {
            "inputs": {"user_prompt": "この文章を英語に翻訳してください"},
            "outputs": {
                "category": "JP",
                "requires_search": False,
                "requires_reasoning": False,
            },
        },
        {
            "inputs": {
                "user_prompt": "What's the difference between は and が particles?"
            },
            "outputs": {
                "category": "JP",
                "requires_search": False,
                "requires_reasoning": False,
            },
        },
        {
            "inputs": {"user_prompt": "君の名は映画のあらすじを教えて"},
            "outputs": {
                "category": "JP",
                "requires_search": False,
                "requires_reasoning": False,
            },
        },
        {
            "inputs": {
                "user_prompt": "How do I conjugate する verbs in the past tense?"
            },
            "outputs": {
                "category": "JP",
                "requires_search": False,
                "requires_reasoning": False,
            },
        },
        {
            "inputs": {
                "user_prompt": "Is it rude to use お前 when talking to strangers in Japan?"
            },
            "outputs": {
                "category": "JP",
                "requires_search": False,
                "requires_reasoning": False,
            },
        },
        {
            "inputs": {
                "user_prompt": "What's the proper way to bow when meeting someone's parents?"
            },
            "outputs": {
                "category": "JP",
                "requires_search": False,
                "requires_reasoning": False,
            },
        },
        {
            "inputs": {
                "user_prompt": "Explain the nuances between 食べる and 召し上がる"
            },
            "outputs": {
                "category": "JP",
                "requires_search": False,
                "requires_reasoning": False,
            },
        },
        # TECH category
        {
            "inputs": {
                "user_prompt": "Explain the difference between TCP and UDP protocols"
            },
            "outputs": {
                "category": "TECH",
                "requires_search": False,
                "requires_reasoning": True,
            },
        },
        {
            "inputs": {
                "user_prompt": "Write a Python function to find the nth Fibonacci number using dynamic programming"
            },
            "outputs": {
                "category": "TECH",
                "requires_search": False,
                "requires_reasoning": True,
            },
        },
        {
            "inputs": {
                "user_prompt": "What's the time complexity of quicksort in the worst case and why?"
            },
            "outputs": {
                "category": "TECH",
                "requires_search": False,
                "requires_reasoning": True,
            },
        },
        {
            "inputs": {
                "user_prompt": "How do I set up a Kubernetes cluster with auto-scaling?"
            },
            "outputs": {
                "category": "TECH",
                "requires_search": False,
                "requires_reasoning": True,
            },
        },
        {
            "inputs": {
                "user_prompt": "Explain how gradient descent works in neural networks"
            },
            "outputs": {
                "category": "TECH",
                "requires_search": False,
                "requires_reasoning": True,
            },
        },
        {
            "inputs": {"user_prompt": "What are the latest features in Python 3.13?"},
            "outputs": {
                "category": "TECH",
                "requires_search": True,
                "requires_reasoning": True,
            },
        },
        {
            "inputs": {
                "user_prompt": "What are the current workflows that are being used to generate game assets with AI?"
            },
            "outputs": {
                "category": "TECH",
                "requires_search": True,
                "requires_reasoning": True,
            },
        },
        # GENERAL category
        {
            "inputs": {"user_prompt": "Write me a short poem about autumn leaves"},
            "outputs": {
                "category": "GENERAL",
                "requires_search": False,
                "requires_reasoning": False,
            },
        },
        {
            "inputs": {"user_prompt": "What's the capital of France?"},
            "outputs": {
                "category": "GENERAL",
                "requires_search": False,
                "requires_reasoning": False,
            },
        },
        {
            "inputs": {
                "user_prompt": "Help me draft a professional email declining a job offer"
            },
            "outputs": {
                "category": "GENERAL",
                "requires_search": False,
                "requires_reasoning": False,
            },
        },
        {
            "inputs": {"user_prompt": "Who won the FIFA World Cup in 2026?"},
            "outputs": {
                "category": "GENERAL",
                "requires_search": True,
                "requires_reasoning": False,
            },
        },
        {
            "inputs": {
                "user_prompt": "Summarize the main themes of Pride and Prejudice"
            },
            "outputs": {
                "category": "GENERAL",
                "requires_search": True,
                "requires_reasoning": False,
            },
        },
        {
            "inputs": {
                "user_prompt": "What's the weather forecast for Tokyo tomorrow?"
            },
            "outputs": {
                "category": "GENERAL",
                "requires_search": True,
                "requires_reasoning": False,
            },
        },
        {
            "inputs": {
                "user_prompt": "Give me book recommendations that have grief as the main theme"
            },
            "outputs": {
                "category": "GENERAL",
                "requires_search": True,
                "requires_reasoning": False,
            },
        },
    ],
}


def create_interpreter_dataset(dataset: Dataset):
    langsmith_client = LangSmithClient()
    langsmith_client.create_dataset(dataset=dataset)


if __name__ == "__main__":
    create_interpreter_dataset(PROMPT_INTERPRETER_DATASET)
