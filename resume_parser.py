import re


SKILLS = [
    "python",
    "java",
    "javascript",
    "sql",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "pandas",
    "numpy",
    "opencv",
    "html",
    "css",
    "react",
    "node.js",
    "express",
    "mongodb",
    "mysql",
    "git",
    "github",
    "docker",
    "aws",
    "azure",
    "gcp"
]


def extract_email(text):
    match = re.search(
        r"[\w.+-]+@[\w-]+\.[\w.-]+",
        text
    )

    return match.group(0) if match else None


def extract_phone(text):
    pattern = r"(?:\+91[\s-]?)?[6-9]\d{9}"

    match = re.search(
        pattern,
        text.replace(" ", "")
    )

    return match.group(0) if match else None


def extract_name(text):

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    if not lines:
        return None

    first_line = lines[0]

    if (
        len(first_line) <= 60
        and not re.search(r"[@\d]", first_line)
    ):
        return first_line

    return None


def extract_skills(text):

    text_lower = text.lower()

    detected = []

    for skill in SKILLS:

        if skill.lower() in text_lower:
            detected.append(skill)

    return sorted(set(detected))


def extract_structured_fields(text):

    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text)
    }


def calculate_ats_score(text, structured):

    score = 100
    feedback = []

    text_lower = text.lower()

    required_sections = {
        "education": "Education section not clearly detected.",
        "experience": "Experience section not clearly detected.",
        "skills": "Skills section not clearly detected.",
        "project": "Projects section not clearly detected."
    }

    for section, message in required_sections.items():

        if section not in text_lower:
            score -= 10
            feedback.append(message)

    if not structured["email"]:
        score -= 10
        feedback.append(
            "Add a clearly readable professional email address."
        )

    if not structured["phone"]:
        score -= 10
        feedback.append(
            "Add a clearly readable phone number."
        )

    if len(structured["skills"]) < 3:
        score -= 10
        feedback.append(
            "The resume contains very few recognizable technical skills."
        )

    word_count = len(text.split())

    if word_count < 200:
        score -= 10
        feedback.append(
            "Resume content appears too short."
        )

    elif word_count > 1200:
        score -= 10
        feedback.append(
            "Resume may be too lengthy for quick recruiter review."
        )

    if not feedback:
        feedback.append(
            "No major structural issues were detected."
        )

    return max(score, 0), feedback


def analyze_resume(text):

    structured = extract_structured_fields(text)

    ats_score, feedback = calculate_ats_score(
        text,
        structured
    )

    return {
        "structured": structured,
        "ats_score": ats_score,
        "ats_feedback": feedback
    }
