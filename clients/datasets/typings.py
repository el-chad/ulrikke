from typing import List, Dict, Any, TypedDict

Example = Dict[str, Any]


class Dataset(TypedDict):
    name: str
    description: str
    examples: List[Example]
