"""
AI Text Summarizer

A professional Streamlit application that summarizes
long text into exactly three bullet points using Groq AI.

Developer:
Nikhil Rana

Project:
NestorBird Engineering Internship Assignment
"""

# ----------------------------------------------------
# Imports
# ----------------------------------------------------

import time

import streamlit as st

from ai_service import generate_summary

from utils import (
    count_words,
    count_characters,
    estimate_reading_time,
    calculate_compression,
    reading_time_saved,
    validate_input,
)

from config import (
    APP_NAME,
    APP_VERSION,
    DEVELOPER,
    MAX_CHARACTERS,
    MIN_WORDS,
    SUMMARY_STYLES,
)


# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

with st.sidebar:

    st.title("🤖 AI Text Summarizer")

    st.caption(
        "Powered by Groq • Llama 3.3 70B"
    )

    st.markdown("---")

    page = st.radio(
        "Navigation",
        (
            "🏠 Home",
            "ℹ️ About",
            "📖 How To Use",
        ),
    )

    st.markdown("---")

    st.subheader("🛠 Technology Stack")

    st.markdown("""
- 🐍 Python
- ⚡ Streamlit
- 🤖 Groq API
- 🧠 Llama 3.3
""")

    st.markdown("---")

    st.subheader("🤖 AI Configuration")

    st.info("""
**Model:** Llama 3.3 70B

**Provider:** Groq

**Temperature:** 0.3

**Maximum Tokens:** 250
""")

    st.markdown("---")

    st.subheader("✨ Application Features")

    st.markdown("""
- AI-powered text summarization
- Four summary styles
- Word & character counter
- Reading time estimation
- Compression analysis
- Reading time saved
- Download summary
- Clean & responsive UI
""")

    st.markdown("---")

    st.caption(f"Version {APP_VERSION}")

    st.caption(f"Developed by {DEVELOPER}")
    
# ----------------------------------------------------
# About Page
# ----------------------------------------------------

if page == "ℹ️ About":

    st.title("ℹ️ About This Project")

    st.write(
        """
The AI Text Summarizer is a professional web application
developed using Python, Streamlit, and the Groq API.

It converts lengthy articles, reports, meeting notes,
blogs, and study material into concise summaries
containing exactly three bullet points.

This project demonstrates:

• AI API Integration

• Prompt Engineering

• Clean Code Architecture

• Modular Python Programming

• Professional UI Design

• Error Handling

• Input Validation
"""
    )

    st.success(
        "Designed for the NestorBird Engineering Internship Assignment."
    )

    st.stop()
    
    # ----------------------------------------------------
# How To Use
# ----------------------------------------------------

if page == "📖 How To Use":

    st.title("📖 How To Use")

    st.markdown("""
### Step 1

Choose your preferred summary style.

---

### Step 2

Paste your article, report,
meeting notes, or any paragraph.

---

### Step 3

Click **Generate AI Summary**.

---

### Step 4

Wait a few seconds while
the AI processes your text.

---

### Step 5

Review the generated summary
and download it if needed.
""")

    st.info(
        "💡 Tip: Well-structured input generally produces better summaries."
    )

    st.stop()
    
    # ----------------------------------------------------
# Home Page
# ----------------------------------------------------

st.title("📝 AI Text Summarizer")

st.caption(
    "Transform lengthy text into concise, AI-powered summaries in just a few seconds."
)

st.markdown("---")


# ----------------------------------------------------
# Hero Section
# ----------------------------------------------------

left_column, right_column = st.columns([3, 1])

with left_column:

    st.subheader("Generate Smart Summaries with AI")

    st.write(
        """
Whether you're reading a news article, research paper,
meeting notes, blog, or documentation,
this application helps you quickly understand
the most important information.

Powered by the Groq API and the Llama 3.3 language model,
the application generates concise summaries in exactly
three bullet points while preserving the key meaning
of the original text.
"""
    )


st.markdown("---")

# ----------------------------------------------------
# Session State
# ----------------------------------------------------

if "user_text" not in st.session_state:

    st.session_state.user_text = ""


if "summary" not in st.session_state:

    st.session_state.summary = ""


if "history" not in st.session_state:

    st.session_state.history = []


if "processing_time" not in st.session_state:

    st.session_state.processing_time = 0
    
    # ----------------------------------------------------
# Summary Settings
# ----------------------------------------------------

st.subheader("⚙️ Summary Settings")

summary_style = st.selectbox(
    "Choose Summary Style",
    SUMMARY_STYLES,
    help="Select how detailed you want the generated summary to be.",
)

st.info(
    """
### Summary Style Guide

**Standard** → Balanced summary for general use.

**Short** → Very concise summary with only the essential points.

**Detailed** → Includes more context while keeping exactly three bullets.

**Executive** → Business-oriented summary highlighting key insights and decisions.
"""
)

st.markdown("---")

st.subheader("📝 Enter Your Text")

st.caption(
    "Paste an article, report, research paper, blog, meeting notes, or any paragraph below."
)

user_text = st.text_area(
    label="",
    value=st.session_state.user_text,
    height=100,
    placeholder="""
Example:

• News Article

• Research Paper

• Meeting Notes

• Blog Post

• Study Material

Paste your content here...
""",
)

if not user_text:

    st.info(
        "👆 Paste your content above and click **Generate AI Summary** to begin."
    )
    

    
# ----------------------------------------------------
# Text Statistics Dashboard
# ----------------------------------------------------

st.markdown("---")

st.subheader("📊 Text Statistics")

total_words = count_words(user_text)

total_characters = count_characters(user_text)

reading_time = estimate_reading_time(user_text)

metric1, metric2, metric3 = st.columns(3)

with metric1:

    st.metric(
        label="📝 Total Words",
        value=total_words,
    )

with metric2:

    st.metric(
        label="🔠 Characters",
        value=total_characters,
    )

with metric3:

    st.metric(
        label="⏱ Estimated Reading Time",
        value=f"{reading_time} min",
    )


# ----------------------------------------------------
# Character Limit Warning
# ----------------------------------------------------

usage = (
    total_characters /
    MAX_CHARACTERS
)

if usage >= 0.90:

    st.warning(
        "⚠️ You are approaching the maximum character limit."
    )

# ----------------------------------------------------
# Input Quality
# ----------------------------------------------------

st.markdown("### 🎯 Input Quality")

if total_words == 0:

    st.info(
        "Waiting for input..."
    )



else:

    st.success(
        "Excellent input. The AI has sufficient context to generate a detailed summary."
    )
    
# ----------------------------------------------------
# # Current Summary Style
# # ----------------------------------------------------

# st.markdown("### ⚙ Current Configuration")

# st.info(
#     f"""
# **Selected Style:** {summary_style}

# The AI will generate a **{summary_style}**
# summary containing **exactly three bullet points.**
# """
# )

# ----------------------------------------------------
# Action Buttons
# ----------------------------------------------------

st.markdown("---")

button1, button2 = st.columns(2)

with button1:

    generate = st.button(
        "🚀 Generate AI Summary",
        use_container_width=True,
        type="primary",
    )

with button2:

    clear = st.button(
        "🧹 Clear Text",
        use_container_width=True,
    )
    
# ----------------------------------------------------
# Generate Summary
# ----------------------------------------------------

if generate:

    validation_message = validate_input(
        user_text,
        MIN_WORDS,
        MAX_CHARACTERS,
    )

    if validation_message:

        st.warning(validation_message)

        st.stop()

    start_time = time.time()

    try:

        with st.spinner(
            "🤖 AI is analyzing your text and preparing the best possible summary..."
        ):

            summary = generate_summary(
                user_text,
                summary_style,
            )

        end_time = time.time()

        st.session_state.processing_time = round(
            end_time - start_time,
            2,
        )

        st.session_state.summary = summary

        st.session_state.user_text = user_text

        st.session_state.history.insert(
            0,
            summary,
        )

        st.session_state.history = (
            st.session_state.history[:5]
        )

    except Exception as error:

        st.error(
            f"❌ {error}"
        )

# ----------------------------------------------------
# Empty State
# ----------------------------------------------------

if not st.session_state.summary:

    st.info(
        "👆 Your generated summary will appear here."
    )
    
# ----------------------------------------------------
# Success Notification
# ----------------------------------------------------

if st.session_state.summary:

    st.success(
        "✅ Summary generated successfully. Review the results below."
    )
    
if st.session_state.summary:

    st.success(...)

    st.subheader(...)

    st.markdown(...)
    
# ----------------------------------------------------
# Display Summary
# ----------------------------------------------------

if st.session_state.summary:

    st.markdown("---")

    st.success(
        "✅ Your AI summary is ready!"
    )

    st.subheader("📄 AI Generated Summary")

    st.markdown(
        st.session_state.summary
    )
    
# ----------------------------------------------------
# Summary Analytics
# ----------------------------------------------------

    summary_words = count_words(
        st.session_state.summary
    )

    compression = calculate_compression(
        user_text,
        st.session_state.summary,
    )

    saved_time = reading_time_saved(
        user_text,
        st.session_state.summary,
    )

# ----------------------------------------------------
# Summary Metrics
# ----------------------------------------------------

    st.markdown("### 📊 Summary Analytics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "📝 Summary Words",
            summary_words,
        )

    with col2:

        st.metric(
            "📉 Compression",
            f"{compression}%"
        )

    with col3:

        st.metric(
            "⏱ Time Saved",
            f"{saved_time} min"
        )

    with col4:

        st.metric(
            "⚡ AI Response",
            f"{st.session_state.processing_time} sec"
        )
        
# ----------------------------------------------------
# Download Summary
# ----------------------------------------------------

    st.download_button(

        label="📥 Download Summary",

        data=st.session_state.summary,

        file_name="AI_Text_Summary.txt",

        mime="text/plain",

        use_container_width=True,
    )

# ----------------------------------------------------
# Summary Quality Indicator
# ----------------------------------------------------

    if compression >= 70:

        st.success(
            "🎯 Excellent compression while preserving the key information."
        )

    elif compression >= 50:

        st.info(
            "👍 Good balance between detail and brevity."
        )

    else:

        st.warning(
            "ℹ️ The generated summary is relatively detailed."
        )
        
# ----------------------------------------------------
# Recent Summaries
# ----------------------------------------------------

    if st.session_state.history:

        st.markdown("---")

        st.subheader("🕒 Recent Summaries")

        for index, item in enumerate(
            st.session_state.history,
            start=1,
        ):

            with st.expander(
                f"Summary {index}"
            ):

                st.markdown(item)
                
st.markdown("---")

st.subheader("📊 Project Statistics")

st.write(f"📝 Current Words: {count_words(st.session_state.user_text)}")

st.write(f"📄 Summaries Generated: {len(st.session_state.history)}")

st.write(f"⚙ Version: {APP_VERSION}")

# ----------------------------------------------------
# Recent Summary History
# ----------------------------------------------------

if st.session_state.history:

    st.markdown("---")

    st.subheader("🕒 Recent Summaries")

    for index, summary in enumerate(
        st.session_state.history,
        start=1,
    ):

        with st.expander(
            f"Summary {index}"
        ):

            st.markdown(summary)

else:

    st.info(
        "No summaries generated yet."
    )

st.markdown("---")

st.markdown(
"""
### 👨‍💻 Developer

**Nikhil Rana**

AI Text Summarizer developed using:

- Python
- Streamlit
- Groq API
- Llama 3.3 70B

This project was created as part of the
**NestorBird Engineering Internship Assignment (2026).**
"""
)

st.caption(
    f"{APP_NAME} • Version {APP_VERSION}"
)

st.caption(
    "© 2026 Nikhil Rana. All Rights Reserved."
)