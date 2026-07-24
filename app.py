"""
app.py

AI Text Summarizer

A professional AI-powered web application that summarizes
long-form text into exactly three concise bullet points.

Developer:
    Nikhil Rana

Project:
    NestorBird Engineering Internship Assignment
"""

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
    MODEL_NAME,
    AI_PROVIDER,
    MAX_CHARACTERS,
    MIN_WORDS,
    SUMMARY_STYLES,
)




st.set_page_config(
    page_title=APP_NAME,
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded",
)



with st.sidebar:

    st.title("🤖 AI Text Summarizer")

    st.caption(
        f"Powered by {AI_PROVIDER} • {MODEL_NAME}"
    )

    st.markdown("---")

    page = st.radio(
        "📂 Navigation",
        (
            "🏠 Home",
            "ℹ️ About",
            "📖 How To Use",
        ),
    )

    st.markdown("---")

    st.subheader("🛠 Technology Stack")

    st.markdown("""
- 🐍 Python 3.12.10
- ⚡ Streamlit
- 🤖 Groq API
- 🧠 llama-3.3-70b-versatile
""")

    st.markdown("---")

    st.subheader("⚙ AI Configuration")

    st.info(f"""
**Provider:** {AI_PROVIDER}

**Model:** {MODEL_NAME}

**Temperature:** 0.3

**Maximum Tokens:** 250
""")

    st.markdown("---")

    st.subheader("✨ Features")

    st.markdown("""
- AI-powered text summarization
- Four summary styles
- Reading time estimation
- Compression analysis
- Download summary
- Session history
""")

    st.markdown("---")

    st.success("🚀 Internship Project")

    st.caption(f"Version {APP_VERSION}")

    st.caption(f"Developed by {DEVELOPER}")




if page == "ℹ️ About":

    st.title("ℹ️ About This Project")

    st.write(
        """
AI Text Summarizer is a beginner-friendly AI application
developed using Python, Streamlit, and the Groq API.

It converts lengthy text into exactly three meaningful
bullet points using the powerful
**llama-3.3-70b-versatile** language model.

The project demonstrates:

• AI API Integration

• Prompt Engineering

• Modular Python Programming

• Clean Code Structure

• Input Validation

• Error Handling

• Interactive User Interface
"""
    )

    st.success(
        "Developed for the NestorBird Engineering Internship Assignment."
    )

    st.stop()




if page == "📖 How To Use":

    st.title("📖 How To Use")

    st.markdown("""
### Step 1

Select a summary style.

---

### Step 2

Paste your text into the input box.

---

### Step 3

Click **Generate AI Summary**.

---

### Step 4

Wait while the AI processes your content.

---

### Step 5

Read or download the generated summary.
""")

    st.info(
        "💡 Better input usually produces better summaries."
    )

    st.stop()




st.title("📝 AI Text Summarizer")

st.caption(
    "Summarize long-form text into exactly three meaningful bullet points using Artificial Intelligence."
)

st.markdown("---")

left_column, right_column = st.columns([3, 1])

with left_column:

    st.subheader("Generate Smart Summaries")

    st.write(
        f"""
This application uses **{MODEL_NAME}**
through the **{AI_PROVIDER} API**
to summarize articles, reports,
blogs, meeting notes, research papers,
and other long-form content.

The generated summary always contains
exactly three concise bullet points while
preserving the main ideas of the original text.
"""
    )

with right_column:

    st.info(f"""
### 🤖 AI Information

**Provider**

{AI_PROVIDER}

**Model**

{MODEL_NAME}

**Output**

Exactly 3 Bullet Points
""")

st.markdown("---")



if "user_text" not in st.session_state:
    st.session_state.user_text = ""

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "history" not in st.session_state:
    st.session_state.history = []

if "processing_time" not in st.session_state:
    st.session_state.processing_time = 0


st.subheader("⚙️ Summary Settings")

summary_style = st.selectbox(
    label="Choose Summary Style",
    options=SUMMARY_STYLES,
    index=0,
    help="Select how you want the AI to summarize your text.",
)

st.info(
    """
### 📌 Summary Styles

**Standard**
- Balanced summary for everyday use.

**Short**
- Focuses only on the most important information.

**Detailed**
- Includes extra context while keeping exactly three bullet points.

**Executive**
- Best for business reports and professional documents.
"""
)

st.markdown("---")



st.subheader("📝 Enter Your Text")

st.caption(
    "Paste your article, report, research paper, meeting notes, "
    "blog, or any long-form content below."
)

user_text = st.text_area(
    label="",
    value=st.session_state.user_text,
    height=220,
    placeholder="""
Examples

• Research Paper

• News Article

• Meeting Notes

• Blog Post

• Business Report

Paste your content here...
""",
)

if not user_text:

    st.info(
        "👆 Paste your text above to get started."
    )

st.markdown("---")



st.subheader("📊 Text Statistics")

total_words = count_words(user_text)

total_characters = count_characters(user_text)

reading_time = estimate_reading_time(user_text)

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "📝 Total Words",
        total_words,
    )

with col2:

    st.metric(
        "🔠 Characters",
        total_characters,
    )

with col3:

    st.metric(
        "⏱ Reading Time",
        f"{reading_time} min",
    )


usage = total_characters / MAX_CHARACTERS

st.subheader("📈 Character Usage")

st.progress(min(usage, 1.0))

st.caption(
    f"{total_characters:,} / {MAX_CHARACTERS:,} characters used"
)

if usage >= 0.90:

    st.warning(
        "⚠️ You are close to the maximum character limit."
    )

elif usage >= 0.70:

    st.info(
        "ℹ️ Your text is getting close to the maximum limit."
    )

st.markdown("---")



st.subheader("🎯 Input Quality")

if total_words == 0:

    st.info(
        "Waiting for your input..."
    )

elif total_words < MIN_WORDS:

    st.warning(
        f"Please enter at least {MIN_WORDS} words."
    )

elif total_words <= 50:

    st.info(
        "Short input detected. The summary may contain limited details."
    )

elif total_words <= 200:

    st.success(
        "Good input. The AI has enough context to generate a useful summary."
    )

else:

    st.success(
        "Excellent input. The AI has enough context to generate a high-quality summary."
    )

st.markdown("---")



button1, button2 = st.columns(2)

with button1:

    generate = st.button(
        "🚀 Generate AI Summary",
        type="primary",
        use_container_width=True,
    )

with button2:

    clear = st.button(
        "🧹 Clear Text",
        use_container_width=True,
    )

if clear:

    st.session_state.user_text = ""
    st.session_state.summary = ""

    st.rerun()

st.markdown("---")


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
            "🤖 AI is analyzing your text..."
        ):

            summary = generate_summary(
                user_text=user_text,
                summary_style=summary_style,
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
            "❌ Failed to generate summary."
        )

        st.exception(error)



if not st.session_state.summary:

    st.info(
        "👆 Your AI-generated summary will appear here."
    )



if st.session_state.summary:

    st.success(
        "✅ Summary generated successfully."
    )

    st.subheader("📄 AI Generated Summary")

    st.markdown(
        st.session_state.summary
    )

    st.markdown("---")



if st.session_state.summary:

    summary_words = count_words(
        st.session_state.summary
    )

    compression = calculate_compression(
        st.session_state.user_text,
        st.session_state.summary,
    )

    saved_time = reading_time_saved(
        st.session_state.user_text,
        st.session_state.summary,
    )

    st.subheader("📊 Summary Analytics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "📝 Summary Words",
            summary_words,
        )

    with col2:

        st.metric(
            "📉 Compression",
            f"{compression}%",
        )

    with col3:

        st.metric(
            "⏱ Reading Time Saved",
            f"{saved_time} min",
        )

    with col4:

        st.metric(
            "⚡ Response Time",
            f"{st.session_state.processing_time} sec",
        )

    st.markdown("---")



if st.session_state.summary:

    st.subheader("🤖 AI Performance")

    if compression >= 80:

        st.success(
            "Excellent summarization with high compression while preserving key information."
        )

    elif compression >= 60:

        st.success(
            "The summary provides a good balance between detail and readability."
        )

    elif compression >= 40:

        st.info(
            "The summary includes additional context for better understanding."
        )

    else:

        st.warning(
            "The summary is relatively detailed because the original text required more context."
        )

    st.markdown("---")



if st.session_state.summary:

    st.download_button(
        label="📥 Download Summary",
        data=st.session_state.summary,
        file_name="AI_Text_Summary.txt",
        mime="text/plain",
        use_container_width=True,
    )

    st.markdown("---")

st.markdown("---")

st.caption(f"{APP_NAME} • Version {APP_VERSION}")

st.caption(
    f"Powered by {AI_PROVIDER} • {MODEL_NAME}"
)

st.caption(
    f"Developed by {DEVELOPER}"
)
    
