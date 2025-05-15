def clean_text(text):
    if not isinstance(text, str):
        return ""
    return text.strip().replace('\n', ' ').replace('\r', '')

def preprocess_profile(profile_dict):
    """
    Prepares a profile dict for prompt formatting.
    Cleans text fields.
    """
    return {k: clean_text(v) if isinstance(v, str) else v for k, v in profile_dict.items()}
