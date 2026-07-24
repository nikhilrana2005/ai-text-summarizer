"""
utils.py

Utility functions used throughout the
AI Text Summarizer application.

Developer:
    Nikhil Rana

Project:
    NestorBird Engineering Internship Assignment
"""



def count_words(text):
    """
    Count the total number of words.

    Parameters:
        text (str): User input text.

    Returns:
        int: Total word count.
    """

    return len(text.split())



def count_characters(text):
    """
    Count the total number of characters.

    Parameters:
        text (str): User input text.

    Returns:
        int: Character count.
    """

    return len(text)



def estimate_reading_time(text):
    """
    Estimate reading time in minutes.

    Average reading speed:
    200 words per minute.

    Parameters:
        text (str): User input text.

    Returns:
        int: Estimated reading time.
    """

    words = count_words(text)

    return max(1, round(words / 200))



def calculate_compression(original_text, summary):
    """
    Calculate how much the text
    was compressed after summarization.

    Parameters:
        original_text (str)
        summary (str)

    Returns:
        int: Compression percentage.
    """

    original_words = count_words(original_text)
    summary_words = count_words(summary)

    if original_words == 0:
        return 0

    compression = (
        (original_words - summary_words)
        / original_words
    ) * 100

    return round(compression)



def reading_time_saved(original_text, summary):
    """
    Estimate reading time saved.

    Parameters:
        original_text (str)
        summary (str)

    Returns:
        int: Minutes saved.
    """

    original_time = estimate_reading_time(original_text)

    summary_time = estimate_reading_time(summary)

    return max(0, original_time - summary_time)



def validate_input(
    text,
    minimum_words,
    maximum_characters,
):
    """
    Validate the user's input.

    Parameters:
        text (str)
        minimum_words (int)
        maximum_characters (int)

    Returns:
        str | None
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
            f"Input exceeds the maximum limit of "
            f"{maximum_characters} characters."
        )

    return None