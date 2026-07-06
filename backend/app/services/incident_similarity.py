import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

index = faiss.read_index(
    "incident_index.faiss"
)

with open(
    "incident_metadata.pkl",
    "rb"
) as f:
    df = pickle.load(f)


def find_similar_incidents(
    query: str,
    top_k: int = 5
):
    embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    distances, indices = index.search(
        np.array(
            embedding,
            dtype=np.float32
        ),
        top_k
    )

    results = []

    for idx in indices[0]:
        row = df.iloc[idx]

        results.append({
            "event": row["event"],
            "severity": row["severity"],
            "root_cause": row["root_cause"],
            "recommendation": row["recommendation"],
        })

    return results