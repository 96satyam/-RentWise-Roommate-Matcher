import os
import logging
from functools import lru_cache
from jinja2 import Template
from llm_engine.llm_utils import call_llm

def compare_profiles(profile1, profile2, prompt_path=None):
    if prompt_path is None:
        current_dir = os.path.dirname(__file__)
        prompt_path = os.path.join(current_dir, "prompts", "compatibility_score.txt")

    with open(prompt_path, "r", encoding="utf-8") as f:
        template = Template(f.read())
    prompt = template.render(profile1=profile1, profile2=profile2)

    return call_llm(prompt)

import re

def parse_compatibility_response(response_text):
    """
    Parse LLM string response like:
    "Score: 70 Reason: Blah blah" into dict.
    """
    score_match = re.search(r"Score:\s*(\d+)", response_text)
    reason_match = re.search(r"Reason:\s*(.*)", response_text, re.DOTALL)

    score = int(score_match.group(1)) if score_match else None
    reason = reason_match.group(1).strip() if reason_match else response_text.strip()

    return {"Score": score, "Reason": reason}



logger = logging.getLogger(__name__)

REQUIRED_KEYS = [
    "Name", "Age", "Gender", "City", "Food_Preference",
    "Sleep_Schedule", "Cleanliness_Level", "Smoking_Drinking",
    "Personality_Description", "Ideal_Roommate"
]

@lru_cache(maxsize=1)
def load_prompt_template(prompt_path):
    if not os.path.exists(prompt_path):
        raise FileNotFoundError(f"Prompt file not found at {prompt_path}")
    with open(prompt_path, "r", encoding="utf-8") as f:
        return Template(f.read())

def validate_profile(profile, profile_name="profile"):
    for key in REQUIRED_KEYS:
        if key not in profile:
            raise ValueError(f"Missing key '{key}' in {profile_name}")

def score_compatibility(profile_a, profile_b, prompt_path="llm_engine/prompts/compatibility_score.txt"):
    # Validate both profiles
    validate_profile(profile_a, "profile_a")
    validate_profile(profile_b, "profile_b")

    # Load prompt template
    template = load_prompt_template(prompt_path)

    # Render prompt
    prompt = template.render(
        name_a=profile_a["Name"], age_a=profile_a["Age"], gender_a=profile_a["Gender"], city_a=profile_a["City"],
        food_a=profile_a["Food_Preference"], sleep_a=profile_a["Sleep_Schedule"], clean_a=profile_a["Cleanliness_Level"],
        smoke_a=profile_a["Smoking_Drinking"], personality_a=profile_a["Personality_Description"], ideal_a=profile_a["Ideal_Roommate"],

        name_b=profile_b["Name"], age_b=profile_b["Age"], gender_b=profile_b["Gender"], city_b=profile_b["City"],
        food_b=profile_b["Food_Preference"], sleep_b=profile_b["Sleep_Schedule"], clean_b=profile_b["Cleanliness_Level"],
        smoke_b=profile_b["Smoking_Drinking"], personality_b=profile_b["Personality_Description"], ideal_b=profile_b["Ideal_Roommate"],
    )

    try:
        response = call_llm(prompt)
    except Exception as e:
        logger.error(f"Error during LLM call: {e}")
        raise RuntimeError("Failed to get a response from LLM")

    logger.info("✅ matcher.py loaded and score_compatibility executed successfully")
    return response

    

