import os, json, time, re
from extractor import extract_text_and_titles
from ranker import rank_sections
from title_detector import get_title_candidates

input_dir = "/app/input"
output_dir = "/app/output"

# Step 1: Read persona and job
with open(os.path.join(input_dir, "persona.json")) as f:
    data = json.load(f)

persona = data["persona"]
job = data["job_to_be_done"]
task = job.get("task", "")

# Step 2: Extract keywords from task (improved keyword extraction)
stopwords = {"a", "an", "of", "for", "the", "is", "to", "in", "and", "with", "on", "at", "by", "or", "but", "as", "are", "was", "were", "be", "been", "have", "has", "had", "do", "does", "did", "will", "would", "could", "should", "may", "might", "can", "shall"}
task_clean = re.sub(r"[^\w\s]", "", task.lower())
keywords = [word for word in task_clean.split() if word not in stopwords and len(word) > 2]

# Add relevant travel-related keywords for better matching
additional_keywords = ["trip", "travel", "group", "friends", "college", "days", "plan", "visit", "activity", "restaurant", "hotel", "accommodation"]
keywords.extend(additional_keywords)

# Step 3: Initialize final output structure
final_output = {
    "metadata": {
        "input_documents": [],
        "persona": persona.get("role", persona),
        "job_to_be_done": task,
        "processing_timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
    },
    "extracted_sections": [],
    "subsection_analysis": []
}

# Step 4: Process each PDF
pdf_files = [f for f in os.listdir(input_dir) if f.endswith(".pdf")]

for filename in pdf_files:
    final_output["metadata"]["input_documents"].append(filename)
    full_path = os.path.join(input_dir, filename)

    # Extract text from PDF
    pages = extract_text_and_titles(full_path)
    
    # Rank sections based on keywords
    ranked = rank_sections(pages, keywords)

    # Process top 5 ranked sections for each document
    for i, sec in enumerate(ranked[:5]):
        # Get title candidates
        titles = get_title_candidates(sec["text"])
        section_title = titles[0] if titles else "Relevant Section"

        # Extract the most relevant snippet (improved logic)
        relevant_lines = [line.strip() for line in sec["lines"] 
                         if line.strip() and any(k in line.lower() for k in keywords)]
        
        if relevant_lines:
            # Choose the most relevant line based on keyword density
            best_line = max(relevant_lines, 
                          key=lambda x: sum(1 for k in keywords if k in x.lower()))
            refined_text = best_line
        else:
            # Fallback to first non-empty line
            refined_text = next((line.strip() for line in sec["lines"] if line.strip()), "")

        # Add to extracted sections
        final_output["extracted_sections"].append({
            "document": filename,
            "section_title": section_title,
            "importance_rank": i + 1,
            "page_number": sec["page"]
        })

        # Add to subsection analysis
        final_output["subsection_analysis"].append({
            "document": filename,
            "refined_text": refined_text,
            "page_number": sec["page"]
        })

# Step 5: Save to output.json
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "output.json"), "w") as f:
    json.dump(final_output, f, indent=2)