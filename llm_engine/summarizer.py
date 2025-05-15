import os
from jinja2 import Template
from llm_engine.llm_utils import call_llm

def summarize_profile(profile, prompt_path=None):
    # Dynamically resolve path relative to current script
    if prompt_path is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        prompt_path = os.path.join(current_dir, "prompts", "personality_summary.txt")

    # Debug: print resolved prompt path
    print("🛠️  Loading prompt from:", prompt_path)

    # File check to help debug missing prompt
    if not os.path.isfile(prompt_path):
        raise FileNotFoundError(f"Prompt file not found at: {prompt_path}")

    with open(prompt_path, "r", encoding="utf-8") as f:
        template = Template(f.read())

    prompt = template.render(**profile)

    return call_llm(prompt)
