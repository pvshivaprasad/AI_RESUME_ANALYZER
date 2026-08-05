<div align="center">

# 📄 AI Resume Analyzer

### AI-powered resume analysis with ATS-oriented checks and intelligent feedback

Built using **Python • Streamlit • Gemini AI • PyMuPDF**

</div>

---

## 🚀 Overview

AI Resume Analyzer is a web application that analyzes PDF resumes and
provides structured information, ATS-oriented checks and AI-generated
improvement suggestions.

Users can upload a resume and optionally provide a job description for
more targeted feedback.

The project combines traditional text processing with generative AI to
demonstrate a practical AI-assisted recruitment workflow.

---

## ✨ Features

- 📄 PDF resume upload
- 🔍 Automatic text extraction
- 👤 Basic contact information extraction
- 🛠️ Technical skill detection
- 🎯 ATS-oriented resume readiness checks
- 📊 Resume readiness score
- 🤖 Gemini-powered resume feedback
- 💼 Optional job-description-based analysis
- 🔐 API credentials managed through environment variables

---

## 🧠 How It Works

```text
          PDF Resume
              │
              ▼
      ┌─────────────────┐
      │    PyMuPDF      │
      │ Text Extraction │
      └────────┬────────┘
               │
               ▼
      ┌─────────────────┐
      │ Resume Parser   │
      │ Regex + Skills  │
      └────────┬────────┘
               │
        ┌──────┴──────┐
        ▼             ▼
 ATS-Oriented      Gemini AI
    Checks          Feedback
        │             │
        └──────┬──────┘
               ▼
       Streamlit Dashboard
