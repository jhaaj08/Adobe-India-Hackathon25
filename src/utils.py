import json
import pdfplumber
from datetime import datetime

def load_input_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_output_json(data, path):
    data["metadata"]["processing_timestamp"] = datetime.now().isoformat()
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def extract_sections_from_pdf(pdf_path):
    sections = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text() or ""
            # Simple heuristic: split by lines, treat lines with ALL CAPS as section titles
            lines = text.split('\n') if text else []
            for idx, line in enumerate(lines):
                if line.isupper() and len(line) > 5:
                    section = {
                        "title": line.strip(),
                        "text": " ".join(lines[idx+1:idx+6]),
                        "page": i+1,
                        "subsections": []
                    }
                    sections.append(section)
    return sections
