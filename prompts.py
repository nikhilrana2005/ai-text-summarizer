"""
prompts.py

Prompt templates used by the AI Text Summarizer.

This module contains the instructions that guide
the AI model to generate consistent and meaningful
summaries.

Developer:
    Nikhil Rana

Project:
    NestorBird Engineering Internship Assignment
"""



SYSTEM_PROMPT = """
You are an intelligent AI assistant specialized in text summarization.

Your task is to summarize the user's text while preserving its
main ideas and important information.

Rules:

1. Generate exactly three bullet points.
2. Keep the summary clear and easy to understand.
3. Do not add new information.
4. Do not change the original meaning.
5. Use professional and simple language.
6. Return only the summary.
"""


def build_prompt(user_text, summary_style):
    """
    Create the final prompt that will be sent
    to the AI model.

    Parameters
    ----------
    user_text : str
        Original text entered by the user.

    summary_style : str
        Selected summary style.

    Returns
    -------
    str
        Formatted prompt for the AI model.
    """

    prompt = f"""
Summary Style:
{summary_style}

Text to Summarize:

{user_text}

Instructions:

- Generate exactly three bullet points.
- Follow the selected summary style.
- Keep the response concise and informative.
- Return only the summary.
"""

    return prompt