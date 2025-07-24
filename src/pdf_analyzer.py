import os
import json
from relevance_model import rank_sections
from utils import extract_sections_from_pdf

def analyze_pdfs(input_data):
    documents = input_data["documents"]
    persona = input_data["persona"]
    job = input_data["job_to_be_done"]
    extracted_sections = []
    subsection_analysis = []
    for doc in documents:
        pdf_path = doc["filename"]
        sections = extract_sections_from_pdf(pdf_path)
        ranked = rank_sections(sections, persona, job)
        for sec in ranked:
            extracted_sections.append({
                "document": pdf_path,
                "section_title": sec["title"],
                "importance_rank": sec["rank"],
                "page_number": sec["page"]
            })
            for sub in sec.get("subsections", []):
                subsection_analysis.append({
                    "document": pdf_path,
                    "refined_text": sub["text"],
                    "page_number": sub["page"]
                })
    return {
        "metadata": {
            "input_documents": [d["filename"] for d in documents],
            "persona": persona["role"],
            "job_to_be_done": job["task"]
        },
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }
