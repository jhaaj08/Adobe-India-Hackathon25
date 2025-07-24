from sentence_transformers import SentenceTransformer, util
import numpy as np

# Load a small, local model (ensure <1GB)
model = SentenceTransformer('all-MiniLM-L6-v2')

def rank_sections(sections, persona, job):
    context = persona["role"] + ". " + job["task"]
    context_emb = model.encode(context, convert_to_tensor=True)
    ranked = []
    for sec in sections:
        sec_emb = model.encode(sec["text"], convert_to_tensor=True)
        score = float(util.pytorch_cos_sim(context_emb, sec_emb))
        sec["rank"] = score
        ranked.append(sec)
    ranked.sort(key=lambda x: x["rank"], reverse=True)
    for i, sec in enumerate(ranked):
        sec["rank"] = i + 1
    return ranked
