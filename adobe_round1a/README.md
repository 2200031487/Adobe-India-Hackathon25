# 📄 Round 1A: PDF Structure Extraction Engine  
**Theme**: "Connect What Matters — For the User Who Matters"  
**Event**: Adobe India Hackathon 2025

---

## 🧠 Overview

This is my solution for **Round 1A** of the **Adobe India Hackathon 2025**.

The challenge involves building a **containerized PDF processing engine** capable of extracting **document titles** and **outline structures** from a collection of PDF files. The solution is lightweight, optimized for CPU-only environments, and does **not** rely on any ML models.

The engine meets **all critical constraints**, runs entirely offline, and works on the **AMD64** architecture with strict runtime and memory limits.

---

## ⚙️ Build & Run Instructions

### 🧱 Build Command

```bash
docker build --platform linux/amd64 -t pdf-title-extractor .
```

### ▶️ Run Command

```bash
docker run --rm -v $(pwd)/input:/app/input:ro -v $(pwd)/output:/app/output --network none pdf-title-extractor
```

---

## 📌 Problem Requirements

### 🔽 Input

* **PDF Files**:
  Located in `/app/input/`, with read-only access during runtime.

### 🔼 Output

* One JSON file per input PDF in `/app/output/`
  Each `filename.json` includes:

  * Extracted **document title**
  * Structured **outline** with heading levels and page numbers

---

## 📁 Project Structure

```
pdf-processor/
├── app/
│   ├── main.py              # Main processing logic
│   ├── requirements.txt     # Python dependencies
│   ├── input/               # Sample PDFs (read-only at runtime)
│   └── output/              # Generated JSON outputs
├── Dockerfile               # Docker configuration
└── README.md                # Documentation
```

---

## 🚧 Hackathon Constraints

| Constraint         | Limit                            |
| ------------------ | -------------------------------- |
| ⏱️ Execution Time  | ≤ 10 seconds (for a 50-page PDF) |
| 📦 Model Size      | ≤ 200MB (No ML models used)      |
| 💻 Runtime         | CPU-only (AMD64)                 |
| 🌐 Internet Access | ❌ Not allowed during runtime     |
| 🧠 Architecture    | Must support AMD64 CPUs          |

✅ **All constraints are satisfied.**

---

## 🧩 Implementation Summary

### ✔️ Title Extraction

* Analyzes text spans on the **first page**
* Selects title based on:

  * **Font size ≥10pt**
  * **Position on page**
  * **Content pattern (non-noise)**
* Filters out:

  * URLs, punctuation-heavy text, dates, etc.
* Supports **multi-language Unicode** (English, Hindi, Arabic, Chinese, etc.)

---

### ✔️ Outline Detection

* Scans **all pages**
* Detects heading candidates based on:

  * Font size variations
  * Numbering patterns (e.g., "1.1", "2.3.1")
* Assigns heading levels (`H1`, `H2`, `H3`) using typography hierarchy
* Filters irrelevant content like:

  * Page numbers, table data, footers

---

### 🧠 Key Functions

| Module                 | Role                                      |
| ---------------------- | ----------------------------------------- |
| `main.py`              | Handles PDF loop, orchestrates extraction |
| `extract_title_only()` | Extracts candidate title using heuristics |
| `extract_outline()`    | Identifies and maps outline sections      |

---

---

## 🧮 Dependencies

```txt
PyMuPDF==1.22.5
```

Install locally using:

```bash
pip install -r requirements.txt
```

---

## 🚀 Performance & Optimization

| Feature              | Description                                       |
| -------------------- | ------------------------------------------------- |
| 🧠 Memory Usage      | < 100MB RAM for standard PDFs                     |
| ⚡ Speed              | < 1s for multi-page documents                     |
| 🧵 Single-threaded   | Works efficiently on CPUs (no parallelism needed) |
| 💾 Storage Efficient | Minimal Docker image size                         |
| 🧱 No ML Dependency  | Fully algorithmic — No trained model required     |

---

## 🔎 Testing Strategy

* ✅ PDFs tested: forms, manuals, academic docs, promotional flyers
* ✅ Output validated for JSON structure & content accuracy
* ✅ Tested offline (no network dependencies)
* ✅ Compatible with both simple & complex layouts

---

## 🛠️ Future Enhancements

* Add support for embedded **tables of contents**
* Improve outline hierarchy accuracy with layout analysis
* Optional: Integrate post-processing summary module

---

**📦 Status**: ✅ Fully functional and ready for submission.
Tested, documented, and meets all Adobe India Hackathon 2025 Round 1A constraints.
