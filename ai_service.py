"""
ai_service.py

Handles communication with the Groq API
to generate AI-powered summaries.

Developer:
    Nikhil Rana

Project:
    NestorBird Engineering Internship Assignment
"""

from groq import Groq

from config import (
    GROQ_API_KEY,
    MODEL_NAME,
    TEMPERATURE,
    MAX_TOKENS,
)

from prompts import (
    SYSTEM_PROMPT,
    build_prompt,
)




client = Groq(
    api_key=GROQ_API_KEY,
)



def generate_summary(user_text, summary_style):
    """
    Generate a summary using the Groq API.

    Parameters:
        user_text (str):
            Text entered by the user.

        summary_style (str):
            Selected summary style.

    Returns:
        str:
            AI-generated summary.
    """

    prompt = build_prompt(
        user_text=user_text,
        summary_style=summary_style,
    )

    try:

        response = client.chat.completions.create(

            model=MODEL_NAME,

            messages=[

                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },

                {
                    "role": "user",
                    "content": prompt,
                },

            ],

            temperature=TEMPERATURE,

            max_tokens=MAX_TOKENS,

        )

        summary = (
            response
            .choices[0]
            .message
            .content
            .strip()
        )

        return summary

    except Exception as error:

        raise Exception(
            f"Failed to generate summary.\n{error}"
        )