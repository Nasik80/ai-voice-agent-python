# AI Voice Agent (Jarvis)

A voice-activated AI assistant built using Python, running locally on Linux (Pop!_OS). It uses **Groq (Llama 3.1)** for near-instant intelligence and **Google Speech Recognition** for voice commands.

## Features
* **Fast Responses:** Uses Llama 3.1 via Groq API.
* **Voice Activation:** Listens via `arecord` (Linux native) to avoid PyAudio driver issues.
* **Speech Output:** Speaks back using Google TTS.

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-link>
   cd voice_agent

This is a crucial step. Never upload your API keys to GitHub. Scanners constantly search GitHub for exposed keys and will steal your credits within seconds.

Here is the professional way to handle this using a .env file and .gitignore.
Step 1: Secure Your API Key

Instead of pasting the key directly into the Python code, we will store it in a separate hidden file and read it using code.

    Install the python-dotenv library:
    Bash

pip install python-dotenv

Create a file named .env (literally just .env) in your project folder.

    Inside this file, paste your key like this:
    Code snippet

    GROQ_API_KEY=gsk_your_actual_key_here_xyz123

Update your Python code. Replace the API key section in your script with this. It reads the hidden file.
Python

    import os
    from dotenv import load_dotenv # Import this

    # Load environment variables from .env file
    load_dotenv() 

    # Get the key securely
    # INSTRUCTIONS FOR GITHUB USERS:
    # 1. Create a file named .env in the project root
    # 2. Add this line inside: GROQ_API_KEY=your_groq_api_key_here
    API_KEY = os.getenv("GROQ_API_KEY") 

    if not API_KEY:
        raise ValueError("API Key not found! Please check your .env file.")

    client = Groq(api_key=API_KEY)

Step 2: Create the .gitignore File

This file tells Git: "Do not upload these specific files."

    Create a new file named .gitignore in your folder.

    Paste this content inside it:
    Plaintext

    # Ignore the virtual environment folder
    venv/

    # Ignore the secret API keys
    .env

    # Ignore python cache files
    __pycache__/

    # Ignore temporary audio files
    *.mp3
    *.wav

Step 3: Create a Requirements File

This lets other people know which libraries they need to install to run your code.

Run this command in your terminal:
Bash

pip freeze > requirements.txt

Step 4: Create a README.md

This is the front page of your project on GitHub. Create a file named README.md and paste this student-friendly description:
Markdown

# AI Voice Agent (Jarvis)

A voice-activated AI assistant built using Python, running locally on Linux (Pop!_OS). It uses **Groq (Llama 3.1)** for near-instant intelligence and **Google Speech Recognition** for voice commands.

## Features
* **Fast Responses:** Uses Llama 3.1 via Groq API.
* **Voice Activation:** Listens via `arecord` (Linux native) to avoid PyAudio driver issues.
* **Speech Output:** Speaks back using Google TTS.

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-link>
   cd voice_agent

2. **Install Dependencies**

   pip install -r requirements.txt
   sudo apt install alsa-utils ffmpeg

3. **Set up API Key**

    Create a file named .env in the main folder.

    Add your Groq API key inside:
    Code snippet

    GROQ_API_KEY=gsk_...

4. **Run the Agent**

    python main.py

**