import os
import google.generativeai as genai


def get_gemini_feedback(
    resume_text,
    job_description=None
):

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY environment variable is not configured."
        )

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel(
        "gemini-1.5-flash"
    )

    prompt = f"""
You are an experienced technical recruiter and resume reviewer.

Review the resume below.

Provide concise, actionable feedback under these headings:

### Resume Summary
Briefly assess the candidate profile.

### Strengths
Identify the strongest parts of the resume.

### Improvements
Identify specific areas that should be improved.

### Skills & Keywords
Suggest relevant technical keywords that could improve discoverability.

### ATS & Readability
Suggest improvements for structure, clarity and ATS readability.

Do not invent experience, qualifications, achievements or skills that
are not supported by the resume.

RESUME:

{resume_text}
"""

    if job_description:

        prompt += f"""

### Job-Specific Analysis

Compare the resume with this job description.

Identify:
- relevant matching skills
- important missing keywords
- areas the candidate should emphasize
- reasonable improvements without inventing experience

JOB DESCRIPTION:

{job_description}
"""

    response = model.generate_content(prompt)

    return response.text.strip()
