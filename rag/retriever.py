import faiss
import numpy as np

class Retriever:
    def __init__(self, embeddings):
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)

    def retrieve(self, query_embedding, top_k=2):
        distances, indices = self.index.search(np.array([query_embedding]), top_k)
        return indices[0]