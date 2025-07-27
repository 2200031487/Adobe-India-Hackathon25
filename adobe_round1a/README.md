# 🧠 Adobe India Hackathon 2025 – Challenge 1A: PDF Outline Extractor

## 📌 Overview

This repository contains a solution for **Challenge 1A – Understand Your Document** of the **Adobe India Hackathon 2025**.  
The goal is to extract a **structured outline** from PDF documents, including:

- 📌 **Title**
- 🔠 **Headings**: `H1`, `H2`, and `H3` (with page numbers)

The solution runs fully **offline**, is **containerized using Docker**, and supports the **amd64 CPU architecture**.

---

## 🗂️ Project Structure

adobe_round1a/
├── app/
│ ├── input/ # Input directory for PDF files
│ ├── output/ # Output directory for generated JSON files
│ └── main.py # Core script to extract title and headings
├── Dockerfile # Docker configuration for containerized execution
├── requirements.txt # Python dependency file
└── README.md # This documentation


---

## ⚙️ Features

- 🚀 Fast processing (≤10s for 50-page PDFs)
- 🧠 Accurate title detection using layout and typography
- 🔡 Hierarchical heading extraction (`H1`, `H2`, `H3`)
- 🌍 Multilingual support (CJK, Indic, Cyrillic, etc.)
- 📄 JSON output conforms to provided schema
- 🐳 Fully containerized and offline-compatible

---

## 📥 Input & 📤 Output

### Input

All `.pdf` files placed in `/app/input/`.

### Output

Each input PDF will generate a corresponding `.json` in `/app/output/`.  
Example:

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "1 Introduction", "page": 1 },
    { "level": "H2", "text": "1.1 What is AI?", "page": 2 },
    { "level": "H3", "text": "1.1.1 History of AI", "page": 3 }
  ]
}
🧠 Approach
🔹 Title Extraction
Extracted from first page

Filters out URLs, metadata, headers/footers

Based on font size and position

🔹 Heading Extraction
Identifies heading levels (H1, H2, H3) using:

Font size thresholds

Numeric patterns (e.g., 1., 1.2., 1.2.1.)

Layout analysis (span density and width)

Ignores irrelevant spans (page numbers, tables, dates)

🔹 Multilingual Handling
Supports characters from:

Latin

Devanagari

CJK (Chinese, Japanese, Korean)

Cyrillic, and more

🐳 Docker Usage

1️⃣ Build the Docker Image

docker build --platform linux/amd64 -t pdf-outline-extractor .

2️⃣ Run the Container

docker run --rm \
  -v $(pwd)/app/input:/app/input:ro \
  -v $(pwd)/app/output:/app/output \
  --network none \
  pdf-outline-extractor
✅ JSON output will be generated for each PDF in app/output.

📦 Dependencies
Listed in requirements.txt:

PyMuPDF==1.22.5

To install locally:

pip install -r requirements.txt

✅ Compliance Checklist
Requirement	                         Status
Execution Time ≤ 10 seconds	          ✅
Model Size ≤ 200MB (if used)	      ✅ (None used)
No Internet Access	                  ✅
CPU-Only Execution (amd64)	          ✅
Output Schema Compliance	          ✅
Dockerized with Platform Targeting	  ✅

🧪 Testing Strategy
PDFs with simple & nested headings

PDFs with multilingual content

Documents with tables, footers, and multi-column layouts

✅ Validated against expected output schema.

