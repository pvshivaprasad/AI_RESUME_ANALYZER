import fitz
import streamlit as st

from ai_feedback import get_gemini_feedback
from resume_parser import analyze_resume


st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")
st.title("📄 AI Resume Analyzer")
st.caption(
    "Analyze your resume for structure, ATS readability, skills and AI-powered improvement suggestions."
)

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
job_description = st.text_area(
    "Job Description (Optional)",
    placeholder="Paste a job description here for targeted feedback...",
    height=160,
)


def extract_pdf_text(file_obj):
    document = fitz.open(stream=file_obj.getvalue(), filetype="pdf")
    text = "\n".join(page.get_text() for page in document)
    document.close()
    return text.strip()


if uploaded_file:
    try:
        resume_text = extract_pdf_text(uploaded_file)

        if not resume_text:
            st.error(
                "No readable text was found in this PDF. Please upload a text-based resume."
            )
            st.stop()

        st.success("Resume uploaded successfully.")

        with st.expander("Preview extracted resume text"):
            st.text_area("Extracted Text", resume_text, height=300, disabled=True)

        if st.button("Analyze Resume", type="primary", use_container_width=True):
            with st.spinner("Analyzing your resume..."):
                analysis = analyze_resume(resume_text)
                ai_feedback = get_gemini_feedback(
                    resume_text,
                    job_description.strip() or None,
                )

            st.divider()
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("📋 Extracted Information")
                structured = analysis["structured"]

                st.write("**Name:**", structured.get("name") or "Not detected")
                st.write("**Email:**", structured.get("email") or "Not detected")
                st.write("**Phone:**", structured.get("phone") or "Not detected")

                st.write("**Detected Skills:**")
                skills = structured.get("skills", [])
                if skills:
                    st.write(", ".join(skills))
                else:
                    st.write("No predefined skills detected.")

            with col2:
                st.subheader("🎯 ATS Analysis")
                score = analysis["ats_score"]

                st.metric("Resume Readiness Score", f"{score}/100")
                st.progress(score / 100)

                for feedback in analysis["ats_feedback"]:
                    st.write(f"• {feedback}")

            st.divider()
            st.subheader("🤖 AI Resume Feedback")
            st.markdown(ai_feedback)

    except Exception as error:
        st.error(
            "Unable to analyze the resume. Please verify your configuration and try again."
        )
        with st.expander("Technical details"):
            st.code(str(error))
