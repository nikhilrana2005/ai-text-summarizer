"""
Application Configuration

This module contains all application constants,
AI model settings, validation limits, and
environment variables used across the project.
"""

import os

from dotenv import load_dotenv



load_dotenv()



GROQ_API_KEY = os.getenv("GROQ_API_KEY")




MODEL_NAME = "llama-3.3-70b-versatile"

TEMPERATURE = 0.3

MAX_TOKENS = 250




MIN_WORDS = 1

MAX_CHARACTERS = 5000



AVERAGE_READING_SPEED = 200




APP_NAME = "AI Text Summarizer | Groq AI"

APP_VERSION = "1.0.0"

DEVELOPER = "Nikhil Rana"



DOWNLOAD_FILE_NAME = "AI_Summary.txt"




SUMMARY_STYLES = (
    "Standard",
    "Short",
    "Detailed",
    "Executive",
)
