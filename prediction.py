# Standard library
import os

# Data processing
import pandas as pd
import numpy as np

# Machine learning
from sklearn.neighbors import NearestNeighbors
from joblib import load

df = pd.read_csv("ucla_orgs_cleaned_unique.csv")
vectorizer = load("model/vectorizer.joblib")
descs = df['description'].fillna("")       
X = vectorizer.transform(descs)


def predict(dict_values):
    neighbors = int(dict_values.get("neighbors", 5))
    top = int(dict_values.get("top", neighbors))
    query = str(dict_values.get("query", "")).strip()

    if not query:
        raise ValueError("Please enter a non-empty query.")

    knn = NearestNeighbors(
        n_neighbors=neighbors,
        metric="cosine",
        algorithm="brute"
    )
    knn.fit(X)

    q_vec = vectorizer.transform([query])

    try:
        distances, indices = knn.kneighbors(q_vec, n_neighbors=top)
    except ValueError:
        raise ValueError(f"'top' must be an integer between 1 and {df.shape[0]}")

    sims = (1 - distances).flatten()
    if np.allclose(sims, 0.0):
        print("No similar clubs found. Your query may contain rare or misspelled words—try simpler keywords.")
        return pd.DataFrame(columns=['name','category','detail_url','similarity'])

    recs = df.iloc[indices.flatten()].copy()
    recs['similarity'] = sims
    return recs[['name','category','detail_url','similarity']].to_dict(orient='records')
