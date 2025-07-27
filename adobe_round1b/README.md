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

📌 Problem Requirements
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

🔼 Output
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
⚠️ Hackathon Constraints
| Constraint          | Limit                        |
| ------------------- | ---------------------------- |
| Execution Time      | ≤ 60 seconds (3–5 PDFs)      |
| Model Size          | ≤ 1 GB                       |
| Runtime Environment | CPU-only (AMD64, no GPU)     |
| Internet Access     | ❌ Not allowed during runtime |

📚 Implementation Summary

✔️ PDF Text Extraction
Uses PyMuPDF to extract structured content from PDFs

Identifies text spans, font sizes, and layout metadata

## Sample Implementation

### Current Sample Solution
The provided implementation demonstrates:
- **Multi-PDF Processing**: Automatic scanning and processing of all travel guide PDFs
- **Intelligent Content Ranking**: Keyword-based scoring to identify most relevant sections
- **Title Detection**: Automatic identification of section headers and important content
- **Persona-Driven Analysis**: Tailored recommendations based on user requirements
- **Structured JSON Output**: Comprehensive travel planning data in organized format

### Sample Processing Script (`main.py`)
```python
# Main processing workflow
import os, json, time, re
from extractor import extract_text_and_titles
from ranker import rank_sections
from title_detector import get_title_candidates

def process_travel_documents():
    input_dir = "/app/input"
    output_dir = "/app/output"
    
    # Read persona and job requirements
    with open(os.path.join(input_dir, "persona.json")) as f:
        data = json.load(f)
    
    # Extract keywords and process all PDFs
    pdf_files = [f for f in os.listdir(input_dir) if f.endswith(".pdf")]
    
    # Generate structured travel recommendations
    final_output = {
        "metadata": {...},
        "extracted_sections": [...],
        "subsection_analysis": [...]
    }
    
    # Save structured output
    with open(os.path.join(output_dir, "output.json"), "w") as f:
        json.dump(final_output, f, indent=2)
```

### Sample Docker Configuration
```dockerfile
FROM --platform=linux/amd64 python:3.9-slim

WORKDIR /app

# Install system dependencies for PyMuPDF
RUN apt-get update && \
    apt-get install -y libglib2.0-0 libgl1-mesa-glx && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app/main.py"]
```

## Expected Output Format

### Required JSON Structure
The solution generates a comprehensive JSON file with travel recommendations:

```json
{
  "metadata": {
    "input_documents": ["document1.pdf", "document2.pdf"],
    "persona": "Travel Planner",
    "job_to_be_done": "Plan a trip of 4 days for a group of 10 college friends.",
    "processing_timestamp": "2025-07-25T14:35:57"
  },
  "extracted_sections": [
    {
      "document": "South of France - Restaurants and Hotels.pdf",
      "section_title": "Budget-Friendly Restaurants",
      "importance_rank": 1,
      "page_number": 2
    }
  ],
  "subsection_analysis": [
    {
      "document": "South of France - Cuisine.pdf",
      "refined_text": "Must-visit restaurants for group dining experiences",
      "page_number": 4
    }
  ]
}
```

## Implementation Guidelines

### Performance Considerations
- **Memory Management**: Efficient handling of multiple large PDF travel guides
- **Processing Speed**: Optimized keyword extraction and content ranking
- **Resource Usage**: Stay within 16GB RAM constraint
- **CPU Utilization**: Parallel processing of multiple documents

### Technical Architecture
- **PDF Processing**: PyMuPDF for reliable text extraction
- **Content Analysis**: Keyword-based scoring with travel-specific enhancements
- **Title Detection**: Multi-pattern recognition for section headers
- **Data Structuring**: Organized output for easy integration

### Travel-Specific Features
- **Group Travel Focus**: Prioritizes content relevant to group activities
- **Budget Considerations**: Identifies budget-friendly options for college students
- **Activity Planning**: Extracts information about attractions, restaurants, and accommodations
- **Cultural Insights**: Includes local traditions and cultural experiences

## Testing Your Solution

### Local Testing
```bash
# Build the Docker image
docker build --platform linux/amd64 -t adobe_round1b .

# Test with sample travel guides
docker run --rm -v $(pwd)/input:/app/input:ro -v $(pwd)/output:/app/output --network none adobe_round1b
```

### Sample Test Data
The solution has been tested with South of France travel guides covering:
- **Cuisine**: Restaurants, local dishes, wine regions
- **History**: Historical sites, cultural landmarks  
- **Accommodations**: Hotels across different budget ranges
- **Activities**: Things to do, attractions, entertainment
- **Practical Info**: Packing tips, travel advice
- **Culture**: Local traditions, festivals, customs

### Validation Checklist
- [ ] All PDFs in input directory are processed
- [ ] persona.json is correctly parsed and utilized
- [ ] JSON output file is generated with proper structure
- [ ] Content ranking produces relevant travel recommendations
- [ ] Processing completes within 10 seconds
- [ ] Solution works without internet access
- [ ] Memory usage stays within 16GB limit
- [ ] Compatible with AMD64 architecture
- [ ] Travel recommendations are contextually appropriate
- [ ] Group-friendly activities are prioritized

## Key Dependencies
```txt
PyMuPDF  # PDF processing and text extraction
```

## Algorithm Highlights

### Content Ranking System
- **Keyword Extraction**: Removes stopwords and extracts meaningful terms
- **Weighted Scoring**: Different weights for title matches vs. content matches
- **Length Consideration**: Bonus points for substantial content sections
- **Travel Context**: Enhanced keywords for group travel scenarios

### Title Detection Patterns
- Title case formatting recognition
- All-caps section headers
- Common travel guide patterns (Chapter, Section, etc.)
- Colon-terminated headers
- Multi-pattern validation

---

**Important**: This solution demonstrates travel-focused document processing for group trip planning. The implementation prioritizes budget-friendly options and group activities suitable for college friends visiting the South of France.
