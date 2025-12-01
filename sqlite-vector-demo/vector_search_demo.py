import sqlite3
import numpy as np

# ------------------------------
# SETUP: sample table + vectors
# ------------------------------
conn = sqlite3.connect(":memory:")

conn.execute("""
CREATE TABLE books_vectors (
    id        INTEGER PRIMARY KEY,
    title     TEXT NOT NULL,
    embedding BLOB NOT NULL
);
""")

# Helper to create a fake 384-dim embedding
def make_vec(value: float) -> bytes:
    return np.array([value] * 384, dtype=np.float32).tobytes()

# Fake vectors
book1_emb = make_vec(0.10)
book2_emb = make_vec(0.80)
book3_emb = make_vec(0.14)

conn.executemany(
    "INSERT INTO books_vectors (id, title, embedding) VALUES (?, ?, ?)",
    [
        (1, "Book 1: Intro to AI",       book1_emb),
        (2, "Book 2: Cooking with Love", book2_emb),
        (3, "Book 3: Machine Learning",  book3_emb),
    ],
)
conn.commit()

# ------------------------------
# SEARCH: create query embedding
# ------------------------------
def fake_text_embedding(text: str) -> np.ndarray:
    return np.array([0.15] * 384, dtype=np.float32)

query_text = input("Enter your search text: ")
query_emb = fake_text_embedding(query_text)

# ------------------------------
# PYTHON VECTOR SEARCH (easy)
# ------------------------------

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Load embeddings from SQLite
rows = conn.execute("SELECT id, title, embedding FROM books_vectors").fetchall()

# Compute cosine similarity for each row
scored = []
for row in rows:
    id_, title, blob = row
    emb = np.frombuffer(blob, dtype=np.float32)
    score = cosine_similarity(query_emb, emb)
    scored.append((score, id_, title))

# Sort by score (highest similarity first)
scored.sort(reverse=True, key=lambda x: x[0])

# Take top-2
top2 = scored[:2]

print("\nTop-2 similar books:")
for score, id_, title in top2:
    print(f"{id_}: {title}   (score={score:.4f})")
