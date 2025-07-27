import fitz  # PyMuPDF

def extract_text_and_titles(pdf_path):
    doc = fitz.open(pdf_path)
    results = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        results.append({
            "page": page_num + 1,
            "text": text,
            "raw_lines": text.split('\n')
        })
    return results
