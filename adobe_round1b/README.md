# 🔍 Challenge 1B: Persona-Driven Document Intelligence  
**Theme**: “Connect What Matters — For the User Who Matters”  
**Event**: Adobe India Hackathon 2025

---

## 🧠 Overview

This is my solution for **Challenge 1B** of the **Adobe India Hackathon 2025**.

The challenge involves designing a system that acts as an **intelligent document analyst**. The system is capable of extracting and prioritizing the **most relevant sections** from a collection of PDF documents — tailored to a **specific persona** and their **job-to-be-done**.

My solution is designed to:
- Understand the **persona's intent**
- Parse and analyze the document collection
- Surface only the **most meaningful and actionable insights**

The entire solution is containerized using **Docker**, designed to run offline, and adheres to the AMD64 CPU architecture with strict performance constraints.

---

## ⚙️ Build & Run Instructions

### 🧱 Build Command

```bash
docker build --platform linux/amd64 -t adobe-round1b .
```

### Run Command
```bash
docker run --rm -v ${PWD}\input:/app/input -v ${PWD}\output:/app/output --network none adobe-round1b
```

### 📌 Problem Requirements

🔽 Input
PDF Collection: 3–10 related documents from any domain

Persona Definition: JSON file with persona's role, expertise, and objectives

Job-to-be-Done: Specific task or question based on the persona's intent

Documents may come from diverse fields like:

Academic research

Financial reports

Educational content

News articles

Domain-specific manuals

### 🔼 Output
A structured output.json file including:

Metadata (documents, persona, job, timestamp)

Extracted sections with importance ranking

Subsection-level refined text summaries



## 📁 Project Structure
```
adobe_round1b/
├── app/
│   ├── main.py              # Orchestrates end-to-end execution
│   ├── extractor.py         # Extracts raw text and section data from PDFs
│   ├── ranker.py           # Scores and ranks relevant content
│   └── title_detector.py   # Helpers for text processing, timestamps, etc.
├── input/
│   ├── persona.json        # Persona and job-to-be-done
│   └── *.pdf              # Input document collection
├── output/
│   └── output.json        # Final structured output
├── Dockerfile             # Docker environment setup
├── requirements.txt       # Python dependencies
└── README.md             # This documentation
```
### ⚠️ Hackathon Constraints
| Constraint          | Limit                        |
| ------------------- | ---------------------------- |
| Execution Time      | ≤ 60 seconds (3–5 PDFs)      |
| Model Size          | ≤ 1 GB                       |
| Runtime Environment | CPU-only (AMD64, no GPU)     |
| Internet Access     | ❌ Not allowed during runtime |

### 📚 Implementation Summary

## ✔️ PDF Text Extraction
Uses PyMuPDF to extract structured content from PDFs

Identifies text spans, font sizes, and layout metadata

## ✔️ Content Ranking Engine
Uses keyword and semantic matching

Ranks content based on relevance to persona's job

## ✔️ Subsection Refinement
Extracts and summarizes fine-grained snippets within selected sections

✔️ Metadata Handling
Attaches full context: input files, timestamp, persona profile

### 🧠 Sample Use Cases
| Test Case         | Persona                      | Job-to-Be-Done                                          |
| ----------------- | ---------------------------- | ------------------------------------------------------- |
| Academic Research | PhD in Computational Biology | Create literature review on GNNs for drug discovery     |
| Business Analysis | Investment Analyst           | Compare R\&D spending across tech companies (2022–2024) |
| Education         | Chemistry Student            | Study key concepts for exam on reaction kinetics        |

### 🔎 Testing Strategy
Tested across documents with:

Different structures (headings, no headings)

Multi-page formats

Multi-domain content (research, financial, educational)

Validated output:

Matches required JSON schema

Extracted content aligns with job relevance

System runs offline under time/memory constraints

### 🧩 Key Modules
| Module         | Role                                                            |
| -------------- | --------------------------------------------------------------- |
| `extractor.py` | Parses documents and detects candidate content sections         |
| `ranker.py`    | Scores sections based on persona and task alignment             |
| `main.py`      | Coordinates input/output processing and builds output structure |

### 🧮 Dependencies
PyMuPDF>=1.22.0     # PDF text extraction
Install with:
pip install -r requirements.txt

### 🧭 Future Enhancements
Integrate lightweight NLP models for better semantic matching

Improve multi-page context tracing for long sections

Introduce visual UI for persona input and JSON visualization

Extend to support images and figures in output



