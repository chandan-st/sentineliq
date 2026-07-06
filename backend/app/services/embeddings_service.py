from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
import faiss
import pickle
from pathlib import Path

# Lightweight embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def build_vector_database():

    dataset_path = Path(
        "../data/incident_knowledge_base.csv"
    )

    df = pd.read_csv(dataset_path)

    texts = []

    for _, row in df.iterrows():
        text = (
            f"{row['event']} "
            f"{row['root_cause']} "
            f"{row['tags']}"
        )
        texts.append(text)

    embeddings = model.encode(
        texts,
        convert_to_numpy=True
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(
        np.array(
            embeddings,
            dtype=np.float32
        )
    )

    faiss.write_index(
        index,
        "incident_index.faiss"
    )

    with open(
        "incident_metadata.pkl",
        "wb"
    ) as f:
        pickle.dump(df, f)

    print(
        f"Indexed {len(df)} incidents."
    )