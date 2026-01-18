from pathlib import Path

from jinja2 import Environment, FileSystemLoader

PROMPTS_DIR = Path(__file__).parent / "prompts"

_env = Environment(
    loader=FileSystemLoader(PROMPTS_DIR),
    trim_blocks=True,
    lstrip_blocks=True,
)


def render_prompt(name: str, **kwargs) -> str:
    """Render a prompt template with the given variables.

    Args:
        name: Template name without extension (e.g., "summarize" for "summarize.md.j2")
        **kwargs: Variables to pass to the template

    Returns:
        The rendered prompt string
    """
    return _env.get_template(f"{name}.md.j2").render(**kwargs)
