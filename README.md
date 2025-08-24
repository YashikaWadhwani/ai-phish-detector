PhishGuard AI - Threat Detection Tool
PhishGuard AI is a web application designed to help users identify phishing threats in real time. By leveraging Google's Gemini 1.5 Flash model, this tool analyzes the content of uploaded files (PDFs, TXT) and URLs to detect potential scams, providing a simple and effective way to verify the safety of digital content.

## Key Features
File Content Analysis: Upload .pdf or .txt files to have their content scanned for phishing indicators and scam language.

URL Classification: Submit a URL to check if it's potentially a phishing, malware, spam, or defaced website.

AI-Powered Detection: Utilizes the Google Gemini 1.5 Flash model to understand the context and nuances of the content.

Web-Based Interface: A clean, modern, and user-friendly interface built with Flask.

## Technologies Used
Backend: Python, Flask

AI/ML: Google Generative AI (Gemini 1.5 Flash)

File Processing: PyPDF2

Frontend: HTML, CSS, Jinja2

Here is a complete README file for your project.

PhishGuard AI - Threat Detection Tool
PhishGuard AI is a web application designed to help users identify phishing threats in real time. By leveraging Google's Gemini 1.5 Flash model, this tool analyzes the content of uploaded files (PDFs, TXT) and URLs to detect potential scams, providing a simple and effective way to verify the safety of digital content.

## Key Features
File Content Analysis: Upload .pdf or .txt files to have their content scanned for phishing indicators and scam language.

URL Classification: Submit a URL to check if it's potentially a phishing, malware, spam, or defaced website.

AI-Powered Detection: Utilizes the Google Gemini 1.5 Flash model to understand the context and nuances of the content.

Web-Based Interface: A clean, modern, and user-friendly interface built with Flask.

## Technologies Used
Backend: Python, Flask

AI/ML: Google Generative AI (Gemini 1.5 Flash)

File Processing: PyPDF2

Frontend: HTML, CSS, Jinja2

## Setup and Installation
To run this project locally, follow these steps:

### 1. Prerequisites
Python 3.8 or higher

A Google API Key from Google AI Studio

### 2. Installation Steps
Clone the Repository

Bash

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Create and Activate a Virtual Environment

Bash

# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
Install Required Libraries

Bash

pip install Flask google-generativeai PyPDF2
Configure the API Key
Open the main.py file and replace the placeholder with your actual Google API key:

Python

# Find this line in your main.py file
os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY_HERE" 
Set Up the Folder Structure
Make sure your index.html file is inside a folder named templates. Your project structure should look like this:

your-repo-name/
|-- venv/
|-- main.py
`-- templates/
    `-- index.html
### 3. Running the Application
Execute the main Python script from your terminal:

Bash

python main.py
Open your web browser and navigate to the following URL:
http://12.0.0.1:5000

## How to Use
Navigate to the homepage in your browser.

To check a file: Use the "malicious files" form to upload a .pdf or .txt file and click "Analyze".

To check a URL: Use the "URL Threat Detection" form to enter a full URL and click "Classify".

The AI's analysis will appear on the page after submission.
