# 📝 AI Text Summarizer

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12.10-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?style=for-the-badge&logo=streamlit)
![Groq](https://img.shields.io/badge/Groq-AI-orange?style=for-the-badge)
![Llama](https://img.shields.io/badge/Llama-3.3%2070B-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)

</p>

---

# 📌 Project Overview

AI Text Summarizer is a professional web application that uses Artificial Intelligence to transform lengthy text into short, meaningful summaries. The project is developed using **Python 3.12.10**, **Streamlit**, **Groq API**, and the **Llama 3.3 70B** language model.

The application allows users to paste long paragraphs, articles, reports, meeting notes, blogs, or study material and generate a concise summary in **exactly three bullet points**. This helps users understand large amounts of information quickly while preserving the key ideas from the original content.

The project follows a modular architecture where different responsibilities such as the user interface, AI integration, configuration, prompts, and utility functions are separated into individual Python modules. This improves readability, maintainability, and scalability.

This application was developed as part of the **NestorBird Engineering Internship Assignment (Python / AI Integration)** to demonstrate practical AI integration, clean coding practices, modular programming, and professional software development.

---

## 📑 Table of Contents

- Project Overview
- Project Objectives
- Problem Statement
- Proposed Solution
- Features
- Technology Stack
- Installation Guide
- Project Structure
- Code Overview
- Application Workflow
- Future Improvements
- Conclusion
- Acknowledgements
- Author
- License


# 🎯 Project Objectives

The primary objectives of this project are:

- Build a real-world AI-powered text summarization application.
- Integrate the Groq API with a Large Language Model.
- Generate concise and meaningful summaries.
- Create a clean and interactive user interface using Streamlit.
- Apply modular programming for better code organization.
- Validate user input before processing.
- Reduce reading time for long-form content.
- Demonstrate practical Python and AI development skills.

---

# 🌍 Problem Statement

Reading lengthy articles, reports, research papers, blogs, and documentation requires significant time and effort. Identifying the most important information manually can also be difficult, especially when dealing with large volumes of text.

An AI-powered summarization tool helps solve this problem by automatically extracting the key points and presenting them in a short, easy-to-read format.

---

# 💡 Proposed Solution

The AI Text Summarizer provides a simple and efficient solution by using the Groq API and the Llama 3.3 language model.

The application performs the following steps:

- Accepts text input from the user.
- Validates the entered content.
- Sends the text to the AI model.
- Generates a summary in exactly three bullet points.
- Displays useful text statistics.
- Allows the summary to be downloaded as a text file.

The result is a lightweight and user-friendly application suitable for students, professionals, researchers, and content creators.

---

# 📖 README Contents

This documentation includes:

- Project Features
- Technology Stack
- Installation Guide
- Project Structure
- Code Overview
- Application Workflow
- Future Improvements
- Conclusion

# ⭐ Features

The AI Text Summarizer is designed to provide a simple, fast, and user-friendly experience while demonstrating practical AI integration.

### Key Features

- **AI-Powered Summarization** – Uses the Groq API with the Llama 3.3 70B language model to generate accurate summaries.
- **Exactly Three Bullet Points** – Every summary follows a consistent three-point format for better readability.
- **Multiple Summary Styles** – Supports Standard, Short, Detailed, and Executive summary styles.
- **Live Text Statistics** – Displays word count, character count, and estimated reading time before summarization.
- **Compression Analysis** – Calculates how much the original text has been reduced after summarization.
- **Reading Time Saved** – Estimates the amount of reading time saved by using the generated summary.
- **Input Validation** – Prevents empty input, very short text, and oversized requests from being processed.
- **Download Summary** – Allows users to download the generated summary as a `.txt` file.
- **Responsive Interface** – Built with Streamlit to provide a clean and interactive user experience.
- **Modular Codebase** – The project is divided into multiple Python files, making it easier to maintain and extend.

---

# 🛠️ Technology Stack

The following technologies are used to build this project.

| Technology | Purpose |
|------------|---------|
| **Python 3.12.10** | Core programming language used to develop the application. |
| **Streamlit** | Creates the interactive web interface. |
| **Groq API** | Connects the application to the AI language model. |
| **Llama 3.3 70B** | Generates accurate and context-aware summaries. |
| **python-dotenv** | Loads environment variables such as the API key. |

---

# 📦 Python Libraries

The project uses a small set of libraries to keep the application lightweight and easy to manage.

- `streamlit`
- `groq`
- `python-dotenv`
- `os`
- `time`

These libraries work together to provide the user interface, AI integration, configuration management, and application functionality.

---

# 🎯 Why This Technology Stack?

This technology stack was selected because it is lightweight, efficient, and easy to maintain.

- **Python** provides clean and readable code.
- **Streamlit** enables rapid development of web applications.
- **Groq API** delivers fast AI inference with low latency.
- **Llama 3.3 70B** produces high-quality summaries while understanding the context of the input text.

Together, these technologies create a reliable AI-powered application that is suitable for learning, portfolio projects, and real-world text summarization tasks.

# ⚙️ Installation Guide

Follow the steps below to run the project on your local machine.

## 1. Clone the Repository

```bash
git clone https://github.com/nikhilrana2005/ai-text-summarizer.git 
cd ai-text-summarizer
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

Install all required Python packages using the following command:

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a file named `.env` in the project root directory and add your Groq API key.

```env
GROQ_API_KEY=your_api_key_here
```

---

## 5. Run the Application

Start the Streamlit application.

```bash
streamlit run app.py
```

After running the command, open the local URL displayed in your terminal (usually `http://localhost:8501`) to access the application.

---

# 📂 Project Structure

```
ai-text-summarizer/
│
├── app.py
├── ai_service.py
├── config.py
├── prompts.py
├── utils.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## File Overview

| File | Description |
|------|-------------|
| **app.py** | Main Streamlit application. Handles the user interface, user interactions, summary display, and session state. |
| **ai_service.py** | Connects to the Groq API, sends prompts to the AI model, and returns the generated summary. |
| **config.py** | Stores application configuration such as model name, API settings, and validation limits. |
| **prompts.py** | Contains the prompts used to guide the AI model for consistent summarization. |
| **utils.py** | Includes reusable helper functions for validation, word count, reading time, compression, and other calculations. |
| **requirements.txt** | Lists all Python packages required to run the project. |
| **.env** | Stores the Groq API key securely using environment variables. |
| **README.md** | Project documentation, setup instructions, and implementation details. |

---

## Project Design

The project follows a modular architecture where each file has a dedicated responsibility. This separation keeps the code organized, improves readability, and makes future maintenance easier. Instead of placing all logic in a single file, the application separates the user interface, AI communication, configuration, prompts, and utility functions into individual modules.

# 💻 Code Overview

The project follows a modular architecture where each Python file has a specific responsibility. This makes the code easier to understand, maintain, and extend.

### app.py
The main application file responsible for the Streamlit user interface. It manages user input, displays text statistics, handles button actions, calls the AI service, and presents the generated summary along with additional metrics.

### ai_service.py
Handles communication with the Groq API. It sends the prepared prompt to the Llama 3.3 language model and returns the generated summary to the main application.

### config.py
Stores configuration values such as the Groq model name, minimum word limit, maximum character limit, and other reusable settings used throughout the project.

### prompts.py
Contains the system prompt used by the AI model. Separating prompts from the application logic makes them easier to modify and maintain.

### utils.py
Provides reusable helper functions such as word counting, character counting, reading time estimation, compression calculation, reading time saved, and input validation.

---

# 🔄 Application Workflow

The overall workflow of the application is shown below.

```
User Input
     │
     ▼
Input Validation
     │
     ▼
Choose Summary Style
     │
     ▼
Generate Summary
     │
     ▼
Groq API
     │
     ▼
Llama 3.3 70B
     │
     ▼
Receive AI Response
     │
     ▼
Display Summary
     │
     ▼
Show Statistics
     │
     ▼
Download Summary
```

The application validates the user's input before sending it to the AI model. Once validated, the selected summary style and text are sent to the Groq API. The Llama 3.3 model processes the request and returns a concise summary, which is then displayed along with useful statistics such as compression percentage, reading time, and reading time saved.

---

# 🚀 Future Improvements

Although the current version is fully functional, the project can be extended with additional features in the future.

Possible improvements include:

- PDF document summarization.
- Microsoft Word (.docx) support.
- Multi-language summarization.
- Export summary as PDF.
- Summary history for previous sessions.
- Copy summary to clipboard.
- Dark mode support.
- User authentication.
- Cloud deployment with a public URL.

These enhancements would improve usability and make the application suitable for larger real-world use cases.

---

# 🏁 Conclusion

AI Text Summarizer demonstrates how Artificial Intelligence can be integrated into a Python application to solve a practical problem. Using Streamlit for the user interface and the Groq API with the Llama 3.3 language model, the application provides fast and accurate summaries while maintaining a clean, modular, and easy-to-understand codebase.

The project showcases Python programming, API integration, prompt-based AI interaction, modular software design, and user interface development. It serves as a strong portfolio project and successfully fulfills the requirements of the NestorBird Engineering Internship Assignment.

---

# 🙏 Acknowledgements

This project was developed as part of the **NestorBird Engineering Internship Assignment (Python / AI Integration)**.

Special thanks to:

- **Groq** for providing fast AI inference through its API.
- **Meta** for the Llama 3.3 language model.
- **Streamlit** for enabling rapid development of interactive web applications.
- The Python open-source community for providing reliable libraries and documentation.

---

# 👨‍💻 Author

**Nikhil Rana**

- 🎓 Bachelor of Computer Applications (BCA)
- 💻 Aspiring Python Developer & Data Analyst
- 🤖 Interested in Artificial Intelligence, Machine Learning, and Data Science

Skills:

- Python
- SQL
- Power BI
- Tableau
- Streamlit
- Artificial Intelligence

---

# 📄 License

This project is created for educational purposes as part of the **NestorBird Engineering Internship Assignment**.

It may be modified, extended, and used for learning and portfolio purposes.

This modular architecture separates the user interface, AI integration, configuration, prompts, and utility functions, making the project easier to maintain and extend.