# Challenge 1b: Travel Planning Document Processing Solution

## Overview
This is a **sample solution** for Challenge 1b of the Adobe India Hackathon 2025. The challenge requires implementing a document processing solution that extracts and analyzes travel information from PDF documents to create personalized trip recommendations. The solution must be containerized using Docker and process multiple travel guide PDFs to generate structured JSON output.

## Official Challenge Guidelines

### Submission Requirements
- **GitHub Project**: Complete code repository with working solution
- **Dockerfile**: Must be present in the root directory and functional
- **README.md**: Documentation explaining the solution, models, and libraries used

### Build Command
```bash
docker build --platform linux/amd64 -t adobe-round1b .
```

### Run Command
```bash
docker run --rm -v ${PWD}\input:/app/input -v ${PWD}\output:/app/output --network none adobe-round1b
```

### Critical Constraints
- **Execution Time**: ≤ 10 seconds for processing multiple travel guide PDFs
- **Model Size**: ≤ 200MB (if using ML models)
- **Network**: No internet access allowed during runtime execution
- **Runtime**: Must run on CPU (amd64) with 8 CPUs and 16 GB RAM
- **Architecture**: Must work on AMD64, not ARM-specific

### Key Requirements
- **Automatic Processing**: Process all PDFs from `/app/input` directory
- **Persona-Based Analysis**: Use persona.json to tailor recommendations
- **Output Format**: Generate structured `output.json` with travel recommendations
- **Input Directory**: Read-only access only
- **Open Source**: All libraries, models, and tools must be open source
- **Travel Focus**: Extract relevant information for group travel planning

## Sample Solution Structure
```
adobe_round1b/
├── app/
│   ├── main.py              # Main processing orchestrator
│   ├── extractor.py         # PDF text extraction using PyMuPDF
│   ├── ranker.py           # Content ranking and scoring system
│   └── title_detector.py   # Title and header detection algorithms
├── input/
│   ├── persona.json        # User persona and trip requirements
│   └── *.pdf              # Travel guide PDF documents
├── output/
│   └── output.json        # Generated travel recommendations
├── Dockerfile             # Docker container configuration
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

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
