"""
config.py

Application configuration settings for the
AI Text Summarizer project.

Developer:
    Nikhil Rana

Project:
    NestorBird Engineering Internship Assignment
"""

import os

from dotenv import load_dotenv



load_dotenv()



APP_NAME = "AI Text Summarizer"

APP_VERSION = "1.0.0"

DEVELOPER = "Nikhil Rana"



GROQ_API_KEY = os.getenv("GROQ_API_KEY")

AI_PROVIDER = "Groq"

MODEL_NAME = "llama-3.3-70b-versatile"

TEMPERATURE = 0.3

MAX_TOKENS = 250



MIN_WORDS = 1

MAX_CHARACTERS = 10000



SUMMARY_STYLES = [
    "Standard",
    "Short",
    "Detailed",
    "Executive",
]


AVERAGE_READING_SPEED = 200



DOWNLOAD_FILE_NAME = "AI_Text_Summary.txt"