# Adobe India Hackathon 2025 - Round 1A Solution

## PDF Structure Extraction System

### Overview
This solution implements a high-performance PDF processing system for Challenge 1A of the Adobe India Hackathon 2025. The system extracts document titles and hierarchical headings (H1-H3) from PDF files with high accuracy while meeting all specified constraints.

## Repository Structure

Adobe-India-Hackathon25/
├── adobe_round1a/
│ ├── app/
│ │ ├── input/ # Input PDF directory (mounted volume)
│ │ ├── output/ # Output JSON directory (mounted volume)
│ │ ├── main.py # Core processing script
│ │ └── requirements.txt # Dependencies
├── Dockerfile # Container configuration
└── README.md # This documentation


## Key Features
- **Accurate Title Detection**: Identifies document titles from first page content
- **Hierarchical Heading Extraction**: Detects H1, H2, H3 headings with page numbers
- **Performance Optimized**: Processes 50-page PDFs in <10 seconds
- **Resource Efficient**: <200MB memory footprint
- **Offline Operation**: No network dependencies

## Technical Implementation
- **Core Library**: PyMuPDF (fitz) for high-performance PDF processing
- **Algorithm**:
  - Font size and positioning analysis
  - Structural pattern recognition
  - Contextual filtering of non-heading elements
- **Multilingual Support**: Handles Latin, Cyrillic, Arabic, and CJK scripts

## Installation & Usage

### Docker Setup
1. Build the container:
   ```bash
   docker build --platform linux/amd64 -t adobe-hackathon-round1a .
2. Run the processor:
docker run --rm \
  -v $(pwd)/input:/app/input:ro \
  -v $(pwd)/output:/app/output \
  --network none \
  adobe-hackathon-round1a

Input/Output Specification
Input: PDF files placed in /app/input directory

Output: JSON files generated in /app/output with structure:
{
  "title": "Document Title",
  "outline": [
    {"level": "H1", "text": "Main Section", "page": 1},
    {"level": "H2", "text": "Subsection", "page": 2}
  ]
}
Performance Metrics
Metric	Value
Processing Speed	<10s for 50-page PDF
Memory Usage	<200MB
CPU Utilization	Optimized for 8-core
Architecture Support	AMD64 (x86_64)

Testing Validation
The solution has been verified against:

Simple single-column documents

Complex multi-column layouts

Multilingual content (English, Arabic, Japanese)

Various heading styles and formats

Constraints Compliance
✅ Execution time ≤10 seconds
✅ Model size ≤200MB
✅ No network access required
✅ AMD64 architecture support
✅ 16GB RAM compatibility
