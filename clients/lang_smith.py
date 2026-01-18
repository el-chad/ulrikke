from langsmith import Client
from langchain_core.prompts import ChatPromptTemplate
from .client_types import Prompt
from .datasets.typings import Dataset
from dotenv import load_dotenv

load_dotenv()


class LangSmithClient:
    def __init__(self):
        self.client = Client()

    def create_prompt_template(
        self, template_title: str, system_prompt: str, prompt: Prompt
    ):
        prompt_template = ChatPromptTemplate(
            [("system", system_prompt), (prompt.get("role"), prompt.get("prompt"))]
        )
        self.client.push_prompt(template_title, object=prompt_template)

    def create_dataset(self, dataset: Dataset):
        langsmith_dataset = self.client.create_dataset(
            dataset_name=dataset["name"], description=dataset["description"]
        )

        self.client.create_examples(
            dataset_id=langsmith_dataset.id,
            examples=dataset["examples"],
        )
