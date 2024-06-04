# Chatbot AI Enhancer

This project is a chatbot application that helps users improve their English pronunciation, grammar, and vocabulary. The application consists of a React frontend and a Django backend.

## Project Structure

src/
├── client/ # React frontend application
└── web/ # Django backend application

markdown
Copy code

## Prerequisites

- Node.js (v14 or later)
- Python (v3.8 or later)
- pip (Python package installer)
- virtualenv (Python virtual environment manager)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/adriannborella/chatbot-ai-enhancer.git
cd chatbot-ai-enhancer
2. Set Up the Django Backend
Navigate to the web directory:

bash
Copy code
cd src/web
Create a virtual environment and activate it:

bash
Copy code
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Apply migrations and start the Django development server:

bash
Copy code
python manage.py migrate
python manage.py runserver
3. Set Up the React Frontend
Open a new terminal window and navigate to the client directory:

bash
Copy code
cd src/client
Install the required Node.js packages:

bash
Copy code
npm install
Start the React development server:

bash
Copy code
npm start
Usage
The React application will be running on http://localhost:3000.
The Django backend will be running on http://localhost:8000.
You can interact with the chatbot via the frontend application. The chatbot will use the Django backend to process audio files and provide feedback on pronunciation, grammar, and vocabulary.

API Endpoints
Random Text Endpoint
URL: /core/random-text/
Method: GET
Description: Returns a random text for the user to read and record.
Process Recorded Speech Endpoint
URL: /core/process-recorded-speech/
Method: POST
Description: Accepts an audio file and the random text, processes the audio to recognize speech, and compares it with the provided text.
Example Request
Random Text
bash
Copy code
curl -X GET http://localhost:8000/core/random-text/
Process Recorded Speech
bash
Copy code
curl -X POST http://localhost:8000/core/process-recorded-speech/ -F 'audio=@path_to_audio.wav' -F 'random_text=The quick brown fox jumps over the lazy dog.'
Troubleshooting
Ensure that both the React and Django servers are running.
Check the browser console and terminal for any error messages.
Verify that the API endpoints are correctly configured and accessible.
License
This project is licensed under the MIT License.

markdown
Copy code

This `README.md` file includes:

- Project structure
- Prerequisites
- Setup instructions for both the Django backend and React frontend
- Usage instructions
- API endpoint descriptions
- Troubleshooting tips

Replace `your-username` with your actual GitHub username if needed. This guide will help users set up and run your project locally.