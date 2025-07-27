# 📄 Round 1A: PDF Structure Extraction Engine  
**Theme**: “Connect What Matters — For the User Who Matters”  
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
