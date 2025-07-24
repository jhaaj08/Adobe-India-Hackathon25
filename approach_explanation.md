# Approach Explanation

## Methodology

1. **Input Parsing**: The system reads the input JSON, which specifies the persona, job-to-be-done, and the list of PDF documents.
2. **PDF Extraction**: Each PDF is parsed using `pdfplumber` to extract text and identify section titles (using heuristics such as ALL CAPS lines).
3. **Section Ranking**: For each section, a semantic similarity score is computed between the section text and the persona/job context using a lightweight SentenceTransformer model (`all-MiniLM-L6-v2`).
4. **Output Generation**: The top-ranked sections and their subsections are included in the output JSON, along with metadata and a processing timestamp.

## Why This Works
- The approach is generic and works for any domain, persona, or task.
- The use of a small, local NLP model ensures compliance with the 1GB and CPU-only constraints.
- The output is structured and explainable, making it easy to evaluate and extend.

## Limitations
- Section extraction is based on simple heuristics and may miss complex document structures.
- The model does not use internet or external APIs, so accuracy is limited by the local model.

## Improvements
- More advanced section detection (e.g., using layout analysis)
- Custom fine-tuning of the ranking model (if allowed)
