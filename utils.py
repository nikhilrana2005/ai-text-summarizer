"""
Utility functions used throughout the AI Text Summarizer.

This module contains helper functions for:

- Word counting
- Character counting
- Reading time estimation
- Compression calculation
- Reading time saved
- User input validation
"""

import re

from config import (
    AVERAGE_READING_SPEED,
)



def count_words(text: str) -> int:
    """
    Return the total number of words.
    """

    if not text.strip():
        return 0

    return len(text.split())




def count_characters(text: str) -> int:
    """
    Return the total number of characters.
    """

    return len(text)




def estimate_reading_time(text: str) -> int:
    """
    Estimate reading time in minutes.

    Average reading speed:
    200 words per minute.
    """

    words = count_words(text)

    if words == 0:
        return 0

    return max(
        1,
        round(words / AVERAGE_READING_SPEED)
    )




def calculate_compression(
    original_text: str,
    summary_text: str,
) -> int:
    """
    Calculate compression percentage.
    """

    original_words = count_words(original_text)

    summary_words = count_words(summary_text)

    if original_words == 0:
        return 0

    compression = (
        1 -
        (summary_words / original_words)
    ) * 100

    return round(compression)




def reading_time_saved(
    original_text: str,
    summary_text: str,
) -> int:
    """
    Calculate estimated reading
    time saved in minutes.
    """

    original_time = estimate_reading_time(
        original_text
    )

    summary_time = estimate_reading_time(
        summary_text
    )

    saved = original_time - summary_time

    return max(saved, 0)




def validate_input(
    text: str,
    minimum_words: int,
    maximum_characters: int,
):
    """
    Validate user input.

    Returns:
        None -> Valid input

        String -> Error message
    """

    if not text.strip():
        return "Please enter some text."

    if count_words(text) < minimum_words:
        return (
            f"Please enter at least "
            f"{minimum_words} words."
        )

    if count_characters(text) > maximum_characters:
        return (
            f"Maximum allowed characters "
            f"are {maximum_characters}."
        )

    return None




def clean_text(text: str) -> str:
    """
    Remove extra spaces and
    unnecessary blank lines.
    """

    text = re.sub(
        r"\s+",
        " ",
        text,
    )

    return text.strip()
