import sys
import os
import streamlit as st
import pandas as pd
import torch

# Fix import path issues first
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from llm_engine.matcher import score_compatibility, parse_compatibility_response
from utils.profile_embeddings import load_profiles, compute_embeddings, compute_similarity_matrix
from utils.display_dataframe import safe_display_dataframe

# Streamlit UI setup
st.set_page_config(page_title="RentWise Matcher", layout="centered")
st.title("🏠 RentWise Roommate Matcher")

# Load and process data
@st.cache_data
def load_data():
    df, profile_texts = load_profiles("data/processed/profiles_with_summaries.csv")
    df = df.convert_dtypes()
    embeddings = compute_embeddings(profile_texts)
    similarity_matrix = compute_similarity_matrix(embeddings)
    return df, embeddings, similarity_matrix

df, embeddings, similarity_matrix = load_data()

# Sidebar for profile selection
profile_names = df["Name"].astype(str).tolist()
selected_profile = st.sidebar.selectbox("Select your profile", profile_names)

# Find selected index
selected_idx = df.index[df["Name"].astype(str) == selected_profile][0]

# Display selected profile
st.subheader(f"👤 Profile: {selected_profile}")
st.dataframe(safe_display_dataframe(df.iloc[[selected_idx]]), use_container_width=True)

# Top-k matches excluding self
top_k = 3
sim_scores = similarity_matrix[selected_idx]
top_indices = torch.topk(sim_scores, top_k + 1).indices.tolist()
top_indices = [i for i in top_indices if i != selected_idx][:top_k]

st.subheader(f"🔍 Top {top_k} Compatible Roommates")

for idx in top_indices:
    profile_a = df.iloc[selected_idx].to_dict()
    profile_b = df.iloc[idx].to_dict()

    st.markdown(f"### {profile_b['Name']}")
    st.dataframe(safe_display_dataframe(df.iloc[[idx]]), use_container_width=True)

    try:
        raw_result = score_compatibility(profile_a, profile_b)
        result = parse_compatibility_response(raw_result)
        st.markdown(f"**Compatibility Score:** {result.get('Score', 'N/A')}")
        st.markdown(f"**Reason:** {result.get('Reason', 'N/A')}")
    except Exception as e:
        st.error("Error computing compatibility score.")
        st.exception(e)

    st.markdown("---")

# Footer note
st.info("✅ Run this app with `streamlit run main.py` to explore full functionality.")
