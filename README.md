<div align="center">

# 📄 AI Resume Analyzer

### Intelligent Resume Analysis • ATS-Oriented Evaluation • AI-Powered Feedback

<p>
An AI-assisted resume analysis platform built with Python, Streamlit and Google Gemini that extracts resume information, evaluates common resume-quality factors and generates actionable improvement suggestions.
</p>
<p align="center">
  <a href="https://airesumeanalyzer814.streamlit.app/">
    <img src="https://img.shields.io/badge/🚀_Live_Demo-Open_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  </a>
  <a href="https://github.com/pvshivaprasad/AI_RESUME_ANALYZER">
    <img src="https://img.shields.io/badge/Source_Code-GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-Web_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Google-Gemini_AI-4285F4?style=for-the-badge&logo=google&logoColor=white"/>
  <img src="https://img.shields.io/badge/PDF-PyMuPDF-02569B?style=for-the-badge"/>
</p>

<p>
  <a href="#-features">Features</a> •
  <a href="#-system-architecture">Architecture</a> •
  <a href="#-how-it-works">How It Works</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-future-roadmap">Roadmap</a>
</p>

</div>

---

## 📌 Overview

Recruiters often receive large numbers of resumes for a single role. Candidates, meanwhile, may not know whether their resume is structured clearly, contains relevant technical information or communicates their experience effectively.

**AI Resume Analyzer** explores how traditional text-processing techniques and Generative AI can be combined to provide useful resume feedback.

The application accepts a PDF resume, extracts its textual content, identifies important candidate information, performs a set of ATS-oriented structural checks and uses **Google Gemini** to generate contextual improvement suggestions.

An optional job description can also be supplied to make the AI feedback more relevant to a particular role.

> **Note:** The ATS readiness score used by this project is a custom heuristic. It does not reproduce or claim to represent the proprietary scoring system of any commercial Applicant Tracking System.

---

## 🎯 Problem Statement

Job seekers frequently encounter several problems when preparing resumes:

- Important information may not be presented clearly.
- Relevant technical skills can be difficult to identify quickly.
- Resumes may omit common sections expected by recruiters.
- Candidates may not know how well their resume aligns with a target role.
- Manual resume review can be subjective and time-consuming.
- Generic resume advice often ignores the actual content of the candidate's resume.

The project addresses these problems through a simple pipeline:

```text
Resume
   ↓
PDF Text Extraction
   ↓
Structured Information Extraction
   ↓
ATS-Oriented Checks
   ↓
AI-Powered Analysis
   ↓
Actionable Resume Feedback
```

---

# ✨ Features

### 📄 PDF Resume Processing

Users can upload a resume in PDF format directly through the Streamlit interface.

The application uses **PyMuPDF** to extract readable textual content from the uploaded document.

---

### 🔍 Resume Information Extraction

The parser attempts to identify useful information such as:

- Candidate name
- Email address
- Phone number
- Technical skills

This provides a structured representation of information detected in the resume.

---

### 🛠️ Technical Skill Detection

The analyzer searches resume content for predefined technical skills across areas such as:

**Programming**

`Python` `Java` `JavaScript` `SQL`

**AI / Machine Learning**

`Machine Learning` `Deep Learning` `TensorFlow` `PyTorch` `Scikit-learn` `OpenCV`

**Web / Backend**

`React` `Node.js` `Express`

**Databases**

`MongoDB` `MySQL`

**Cloud & Development Tools**

`Git` `GitHub` `Docker` `AWS` `Azure` `GCP`

---

### 🎯 ATS-Oriented Resume Checks

The application performs heuristic checks for common resume elements.

Examples include checking for:

- Education section
- Experience section
- Skills section
- Projects section
- Detectable email address
- Detectable phone number
- Technical skills
- Resume content length

These checks contribute to a simple **Resume Readiness Score**.

---

### 📊 Resume Readiness Score

The application presents the result through a simple score:

```text
Resume Readiness
       │
       ├── Section Presence
       ├── Contact Information
       ├── Skill Detection
       └── Content Length
              │
              ▼
           0 – 100
```

The score is intended as an educational feedback mechanism rather than an official ATS score.

---

### 🤖 Gemini AI Resume Feedback

Google Gemini is used for deeper contextual analysis.

The AI is prompted to provide feedback covering areas such as:

- Overall resume assessment
- Strong sections
- Areas requiring improvement
- Relevant technical keywords
- Resume readability
- ATS-oriented suggestions

The prompt also explicitly discourages inventing experience or qualifications that are not present in the resume.

---

### 💼 Job Description Analysis

Users can optionally paste a target job description.

When supplied, Gemini can provide more targeted feedback by identifying:

- Matching skills
- Potentially missing keywords
- Relevant areas to emphasize
- Resume improvements related to the role

This makes the analysis more useful than completely generic resume advice.

---

# 🏗️ System Architecture

```text
                    ┌─────────────────────────┐
                    │          USER           │
                    └────────────┬────────────┘
                                 │
                          Upload PDF Resume
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      STREAMLIT UI       │
                    │                         │
                    │ Resume Upload           │
                    │ Job Description Input   │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │        PyMuPDF          │
                    │                         │
                    │   PDF Text Extraction   │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      RESUME PARSER      │
                    │                         │
                    │ • Contact Extraction    │
                    │ • Skill Detection       │
                    │ • Structural Analysis   │
                    └────────────┬────────────┘
                                 │
                    ┌────────────┴────────────┐
                    │                         │
                    ▼                         ▼
        ┌──────────────────────┐   ┌──────────────────────┐
        │ ATS-ORIENTED CHECKS  │   │      GEMINI AI       │
        │                      │   │                      │
        │ • Resume Sections    │   │ • Resume Review      │
        │ • Contact Details    │   │ • Improvements       │
        │ • Skills             │   │ • Keywords           │
        │ • Content Length     │   │ • JD Comparison      │
        └──────────┬───────────┘   └──────────┬───────────┘
                   │                          │
                   └────────────┬─────────────┘
                                ▼
                    ┌─────────────────────────┐
                    │     ANALYSIS RESULTS    │
                    │                         │
                    │ • Extracted Details     │
                    │ • Readiness Score       │
                    │ • ATS Feedback          │
                    │ • AI Suggestions        │
                    └─────────────────────────┘
```

---

# 🔄 How It Works

## 1️⃣ Resume Upload

The user uploads a PDF resume through the Streamlit interface.

```text
User
 │
 └──────► Resume.pdf
```

## 2️⃣ PDF Text Extraction

PyMuPDF reads the uploaded document and extracts text from each page.

```text
PDF
 │
 ▼
PyMuPDF
 │
 ▼
Raw Resume Text
```

## 3️⃣ Structured Parsing

The extracted text is passed to the resume parser.

Regular expressions and predefined skill matching are used to identify information from the resume.

```text
Raw Text
   │
   ├──► Name
   ├──► Email
   ├──► Phone
   └──► Skills
```

## 4️⃣ Resume Quality Checks

The analyzer checks whether common resume elements can be detected.

A heuristic score is calculated from those checks.

```text
Resume Text
    │
    ▼
Structural Checks
    │
    ▼
Readiness Score + Feedback
```

## 5️⃣ AI Analysis

The resume text is sent to Gemini with a structured review prompt.

If a job description is supplied, it is included in the analysis context.

```text
Resume + Optional JD
          │
          ▼
      Gemini AI
          │
          ▼
 Contextual Feedback
```

## 6️⃣ Results

The Streamlit dashboard displays the combined results.

```text
┌────────────────────────────┐
│     ANALYSIS DASHBOARD     │
├────────────────────────────┤
│ Candidate Information      │
│ Detected Skills            │
│ Resume Readiness Score     │
│ Structural Feedback        │
│ Gemini AI Suggestions      │
└────────────────────────────┘
```

---

# 🧰 Tech Stack

| Technology | Role |
|---|---|
| **Python** | Core programming language |
| **Streamlit** | Interactive web application |
| **PyMuPDF** | PDF text extraction |
| **Google Gemini** | Generative AI resume analysis |
| **Regex** | Contact information extraction |
| **Environment Variables** | API credential configuration |
| **Git** | Version control |
| **GitHub** | Source-code hosting |

---

# 📁 Project Structure

```text
AI_RESUME_ANALYZER/
│
├── app.py
│   └── Streamlit application and user interface
│
├── resume_parser.py
│   ├── Resume field extraction
│   ├── Technical skill detection
│   └── ATS-oriented checks
│
├── ai_feedback.py
│   └── Gemini AI integration and feedback generation
│
├── job_matcher.py
│   └── Job-matching experimentation/module
│
├── requirements.txt
│   └── Python dependencies
│
├── sample_data/
│   └── Sample/testing resources
│
├── .gitignore
│   └── Git exclusions
│
└── README.md
    └── Project documentation
```

---

# 🔐 Security & Configuration

The Gemini API key should **never be hard-coded into the source code**.

The application reads the key from an environment variable:

```text
GEMINI_API_KEY
```

This keeps credentials separate from the public repository.

### Example

**Windows PowerShell**

```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

**Linux / macOS**

```bash
export GEMINI_API_KEY="your_api_key_here"
```

Sensitive files such as `.env` should be excluded through `.gitignore`.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/pvshivaprasad/AI_RESUME_ANALYZER.git
```

```bash
cd AI_RESUME_ANALYZER
```

---

## 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Gemini

Set your Gemini API key using an environment variable.

```text
GEMINI_API_KEY=your_api_key
```

---

## 5. Run the Application

```bash
streamlit run app.py
```

Streamlit will display a local URL similar to:

```text
http://localhost:8501
```

Open it in your browser.

---

# 🖥️ Application Workflow

```text
┌──────────────────────────┐
│      Upload Resume       │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│    Extract PDF Text      │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│   Parse Resume Details   │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ ATS-Oriented Evaluation  │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│    Gemini AI Analysis    │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│    Results Dashboard     │
└──────────────────────────┘
```

---

# 📸 Screenshots

> Screenshots will be added after the final UI and functionality verification.

### Home / Resume Upload

```text
assets/screenshots/home.png
```

### Resume Analysis

```text
assets/screenshots/analysis.png
```

### AI Feedback

```text
assets/screenshots/feedback.png
```

Once the application is finalized, these screenshots can be embedded directly into this README.

---

# 🧪 Example Use Case

Consider a candidate applying for a Python developer position.

### Resume

```text
Skills:
Python, SQL, Git, Pandas
```

### Target Job

```text
Python Developer

Required:
Python
REST APIs
SQL
Git
Docker
```

The application can identify existing skills from the resume and use the supplied job description to request more targeted AI feedback.

The system should **not** claim that the candidate knows Docker simply because it appears in the job description. Instead, it can identify it as a potentially relevant missing keyword or skill to evaluate honestly.

---

# 🧠 Design Decisions

### Why combine traditional parsing with Generative AI?

Using an LLM for every operation would make simple extraction unnecessarily expensive and unpredictable.

Therefore, the project separates responsibilities:

```text
Deterministic Tasks
        │
        ├── Email extraction
        ├── Phone extraction
        ├── Skill detection
        └── Structural checks

Contextual Tasks
        │
        └── Gemini AI
             ├── Resume review
             ├── Suggestions
             ├── Keyword recommendations
             └── Job-specific feedback
```

This provides a clearer separation between deterministic processing and AI-generated analysis.

---

# ⚠️ Current Limitations

This project is still evolving.

Current limitations include:

- Only PDF resumes are supported.
- Text extraction depends on readable PDF content.
- Scanned/image-only PDFs may not provide usable text.
- Skill detection uses a predefined skill list.
- Contact extraction uses pattern matching.
- The readiness score is heuristic.
- The application does not reproduce a commercial ATS.
- AI feedback quality depends on the model response and input quality.
- Job matching is not yet a full semantic ranking system.

Documenting these limitations is intentional—the project focuses on demonstrating the engineering approach without overstating its capabilities.

---

# 🚀 Future Roadmap

### Resume Intelligence

- [ ] Advanced resume section detection
- [ ] Named Entity Recognition
- [ ] Dynamic skill extraction
- [ ] Resume keyword frequency analysis
- [ ] Better experience and education parsing

### Job Matching

- [ ] Semantic resume/JD similarity
- [ ] Skill-gap analysis
- [ ] Match percentage
- [ ] Missing keyword identification
- [ ] Role-specific recommendations

### User Experience

- [ ] Improved Streamlit dashboard
- [ ] Resume analysis visualization
- [ ] Downloadable analysis report
- [ ] DOCX support
- [ ] Multiple resume comparison

### Engineering

- [ ] Unit tests
- [ ] Input validation
- [ ] Better exception handling
- [ ] Structured logging
- [ ] Configuration management
- [ ] CI workflow

---

# 📚 Key Learning Outcomes

Building this project provides practical experience with:

- Python application development
- PDF document processing
- Regular expressions
- Text parsing
- Generative AI integration
- Prompt design
- Environment-based secret management
- Streamlit application development
- Modular Python project organization
- Git/GitHub workflow
- Responsible representation of AI-generated results

---

# 💡 Potential Applications

The concepts demonstrated by this project can be extended to:

- Resume review tools
- Career-assistance platforms
- Candidate screening support
- Skill extraction systems
- Job-description comparison tools
- Career recommendation systems
- Recruitment analytics applications

---

# 🤝 Contributing

Suggestions and improvements are welcome.

A typical contribution workflow:

```bash
git checkout -b feature/improvement-name
```

Make the required changes and commit them:

```bash
git commit -m "feat: add improvement"
```

Then push your branch and create a pull request.

---

# 👨‍💻 Author

### Venkata Shiva Prasad Punna

**Software Developer | Java • Python • AI/ML**

GitHub: [@pvshivaprasad](https://github.com/pvshivaprasad)

---

<div align="center">

### ⭐ AI Resume Analyzer

**Transforming resume content into actionable technical insights using Python and Generative AI.**

If you find the project useful, consider giving the repository a ⭐.

</div>
