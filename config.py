"""
Application Configuration

This module contains all application constants,
AI model settings, validation limits, and
environment variables used across the project.
"""

import os

from dotenv import load_dotenv


# ----------------------------------------------------
# Load Environment Variables
# ----------------------------------------------------

load_dotenv()


# ----------------------------------------------------
# API Configuration
# ----------------------------------------------------

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# ----------------------------------------------------
# AI Model Configuration
# ----------------------------------------------------

MODEL_NAME = "llama-3.3-70b-versatile"

TEMPERATURE = 0.3

MAX_TOKENS = 250


# ----------------------------------------------------
# Input Validation
# ----------------------------------------------------

MIN_WORDS = 1

MAX_CHARACTERS = 5000


# ----------------------------------------------------
# Reading Speed
# ----------------------------------------------------

AVERAGE_READING_SPEED = 200


# ----------------------------------------------------
# Application Information
# ----------------------------------------------------

APP_NAME = "AI Text Summarizer | Groq AI"

APP_VERSION = "1.0.0"

DEVELOPER = "Nikhil Rana"


# ----------------------------------------------------
# Download Settings
# ----------------------------------------------------

DOWNLOAD_FILE_NAME = "AI_Summary.txt"


# ----------------------------------------------------
# UI Labels
# ----------------------------------------------------

SUMMARY_STYLES = (
    "Standard",
    "Short",
    "Detailed",
    "Executive",
)