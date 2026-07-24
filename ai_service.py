"""
AI Service

This module handles communication with the Groq API.

Responsibilities:
- Clean user input
- Select the correct system prompt
- Send request to Groq
- Return the generated summary
- Handle API errors gracefully
"""

from groq import Groq

from config import (
    GROQ_API_KEY,
    MODEL_NAME,
    TEMPERATURE,
    MAX_TOKENS,
)

from prompts import SUMMARY_PROMPTS

from utils import clean_text




client = Groq(
    api_key=GROQ_API_KEY
)




def generate_summary(
    user_text: str,
    summary_style: str,
) -> str:
    """
    Generate an AI summary using the selected summary style.

    Args:
        user_text:
            Text entered by the user.

        summary_style:
            Standard
            Short
            Detailed
            Executive

    Returns:
        AI-generated summary.
    """

    cleaned_text = clean_text(user_text)

    system_prompt = SUMMARY_PROMPTS.get(
        summary_style,
        SUMMARY_PROMPTS["Standard"],
    )

    try:

        response = client.chat.completions.create(

            model=MODEL_NAME,

            messages=[

                {
                    "role": "system",
                    "content": system_prompt,
                },

                {
                    "role": "user",
                    "content": cleaned_text,
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

        raise RuntimeError(

            "Unable to connect to the AI service. "
            "Please check your internet connection "
            "or try again in a few moments."

        ) from error
