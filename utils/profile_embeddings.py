from sentence_transformers import SentenceTransformer, util
import pandas as pd
import torch

model = SentenceTransformer('all-MiniLM-L6-v2')

def load_profiles(csv_path):
    df = pd.read_csv(csv_path)
    if "Summary" not in df.columns:
        raise ValueError("Expected 'Summary' column not found in CSV.")
    df = df.dropna(subset=["Summary"]).reset_index(drop=True)  # drop empty summaries if any
    profile_texts = df["Summary"].tolist()
    return df, profile_texts

def compute_embeddings(texts):
    if not texts:
        raise ValueError("Input text list is empty.")
    return model.encode(texts, convert_to_tensor=True)

def compute_similarity_matrix(embeddings):
    """
    Compute cosine similarity matrix from embeddings.
    """
    if embeddings is None or len(embeddings) == 0:
        raise ValueError("Embeddings tensor is empty or None.")
    return util.pytorch_cos_sim(embeddings, embeddings)

def get_top_matches(df, embeddings, top_k=3):
    similarity_matrix = compute_similarity_matrix(embeddings)
    matches = []
    n = len(df)
    k = min(top_k, n-1)  # Ensure top_k doesn't exceed number of other profiles
    
    for i in range(n):
        sim_scores = similarity_matrix[i]
        # Get top k+1 indices, skip self (the first)
        top_indices = torch.topk(sim_scores, k + 1).indices.tolist()
        top_indices = [idx for idx in top_indices if idx != i][:k]
        
        profile_name = df.iloc[i]["Name"]
        top_matches = [(df.iloc[j]["Name"], float(sim_scores[j])) for j in top_indices]
        matches.append((profile_name, top_matches))
    
    return matches, similarity_matrix
