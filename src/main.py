import sys
import json
from pdf_analyzer import analyze_pdfs
from utils import load_input_json, write_output_json

def main(input_path, output_path):
    input_data = load_input_json(input_path)
    result = analyze_pdfs(input_data)
    write_output_json(result, output_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_json> <output_json>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
