import pandas as pd

def load_profiles(path="data/raw/roommate_profiles.csv"):
    """
    Loads roommate profiles from the CSV file.
    Drops incomplete rows and prepares profile summaries (texts) for embeddings.
    Returns:
      - df: cleaned DataFrame
      - profile_texts: list of concatenated profile description strings
    """
    df = pd.read_csv(path)
    df = df.dropna(how='any').reset_index(drop=True)  # Remove incomplete rows and reset index

    # Create textual summaries for each profile by concatenating relevant columns
    profile_texts = (
        df["Name"].astype(str) + " " +
        df["Age"].astype(str) + " " +
        df["Gender"].astype(str) + " " +
        df["City"].astype(str) + " " +
        df["Food_Preference"].astype(str) + " " +
        df["Sleep_Schedule"].astype(str) + " " +
        df["Cleanliness_Level"].astype(str) + " " +
        df["Smoking_Drinking"].astype(str) + " " +
        df["Personality_Description"].astype(str) + " " +
        df["Ideal_Roommate"].astype(str)
    ).tolist()

    return df, profile_texts
