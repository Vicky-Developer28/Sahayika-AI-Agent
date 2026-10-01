# Sahayika AI Agent

## Overview

**Sahayika** ("Female Helper") is an AI-powered voice and text guide designed to help first-time rural women users—with no English proficiency, no technical background, and no prior digital experience—independently access essential government welfare schemes. 

Built for a hackathon environment, the application provides a zero-knowledge, voice-first interface in regional languages (Tamil), abstracting away the complexity of government digital portals and enabling autonomous access to welfare services such as the **PM Ujjwala Yojana**.

---

## Hackathon

### Hackathon Problem Statement

> "Build an AI tool that helps a first-time woman user — with no English, no tech background, and no one to ask — independently access one essential government service, scheme, or skill resource through voice or simple text in her own language. The tool must require zero prior digital knowledge to use."

### Problem Analysis

Rural women in India face severe structural barriers when attempting to access government benefits online:
* **Language Barrier:** Digital systems default to English or formal Hindi without adequate regional language support.
* **Literacy & Technical Barriers:** Complex, text-heavy interfaces assume literacy and prior device experience.
* **Dependency Barrier:** Access typically requires guidance from a male family member or intermediary.
* **Navigation Complexity:** Government portals involve multi-step processes that are difficult for novices to navigate independently.

### Objective

Deliver a lightweight, highly accessible web application within a 4-hour development window that leverages the Gemini API and browser speech capabilities to guide a user through a single government scheme (PM Ujjwala Yojana) entirely through spoken or simple typed regional language.

---

## Solution

Sahayika implements a minimal, single-page Django application featuring:
* A welcoming, non-intimidating interface centered around a large voice input button.
* Browser-native Speech-to-Text (STT) and Text-to-Speech (TTS) via the Web Speech API.
* Gemini API integration guided by a specialized system prompt to provide simple, conversational Tamil responses.
* Session-based conversation context maintenance.

---

## Implemented Scope

The current implementation focuses specifically on:
* **Target Scheme:** PM Ujjwala Yojana (free LPG connection scheme).
* **Language:** Tamil (spoken and text input/output).
* **Architecture:** Django backend handling session history and Gemini API communication, paired with a vanilla JavaScript frontend using browser speech APIs.

---

## Features

* **Voice Input:** Tap-to-speak functionality allowing users to speak naturally in Tamil.
* **Text Input Fallback:** A simple text box for typing in Tamil script if voice input is not preferred.
* **AI-Powered Guidance:** Gemini 1.5 Flash processes user inputs and provides conversational, easy-to-understand explanations of eligibility and requirements.
* **Voice Output (TTS):** The application reads AI responses aloud in Tamil using browser speech synthesis.
* **Step-by-Step Action Plan:** Guides the user directly to actionable next steps (e.g., visiting the nearest Fair Price Shop with necessary documents).
* **Zero Registration Required:** No login or account creation needed to start interacting with the agent.

---

## PM Ujjwala Yojana

The application provides focused assistance for **PM Ujjwala Yojana**:
* Explains what the scheme offers in simple spoken-word Tamil.
* Guides the user through basic eligibility criteria (e.g., adult women from low-income households).
* Directs the user on exact offline steps (e.g., visiting an authorized LPG distributor or Fair Price Shop with an Aadhaar card and BPL card).

---

## AI Integration

* **AI Model:** `gemini-1.5-flash` via the `google-generativeai` Python SDK.
* **API Integration:** Backend view endpoint sends user messages along with conversation history and a strict system prompt to the Gemini API.
* **Prompting Approach:** System instructions enforce Tamil-only, simple, non-bureaucratic, spoken-style responses focused exclusively on the PM Ujjwala Yojana workflow.
* **Token/Output Constraints:** Relies on standard Gemini API rate limits and model token windows, structured for short conversational turns suitable for voice interaction.

---

## Technology Stack

| Component | Technology |
|---|---|
| **Language** | Python 3.11+ |
| **Web Framework** | Django |
| **AI Model** | Google Gemini API (`gemini-1.5-flash`) |
| **Frontend UI** | HTML5, CSS3, Vanilla JavaScript |
| **Voice & Speech** | Browser Web Speech API (SpeechRecognition & SpeechSynthesis) |

---

## Architecture


```

+--------------------------------------------------+
|               Browser (Chrome Mobile)            |
|  +--------------------------------------------+  |
|  |           Single Page (index.html)         |  |
|  |  - Large "Speak" button                    |  |
|  |  - Chat display (Tamil text)               |  |
|  |  - Web Speech API (STT + TTS)              |  |
|  +-------------------+------------------------+  |
+----------------------|---------------------------+
| POST /chat/ (fetch API)
v
+--------------------------------------------------+
|               Django Application                 |
|  +--------------+   +------------------------+  |
|  | URL Router   +-->|  Chat View             |  |
|  +--------------+   |  - Session management  |  |
|                     |  - Gemini API call     |  |
|  +--------------+   +------------------------+  |
|  | Django       |                               |
|  | Session      |                               |
|  +--------------+                               |
+----------------------+---------------------------+
| google-generativeai SDK
v
+--------------------------------------------------+
|                   Gemini API                     |
|  Model: gemini-1.5-flash                         |
|  System Prompt: Tamil-only, Ujjwala Yojana       |
+--------------------------------------------------+

```

---

## Project Structure


```

Sahayika-AI-Agent/
├── manage.py
├── requirements.txt
├── sahib/ (or project configuration directory)
│   ├── **init**.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── core/ (or main application directory)
├── **init**.py
├── admin.py
├── apps.py
├── views.py
├── urls.py
├── templates/
│   └── core/
│       └── index.html
└── static/
└── css/ & js/

```

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Vicky-Developer28/Sahayika-AI-Agent.git](https://github.com/Vicky-Developer28/Sahayika-AI-Agent.git)
   cd Sahayika-AI-Agent

```

2. **Create and activate a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```



---

## Environment Variables

Create a `.env` file in the root directory or configure your environment variables with the following required key:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here

```

*Note: Never commit your actual API keys, passwords, or secrets to version control.*

---

## Running the Project

1. **Apply database migrations (if applicable for session storage):**
```bash
python manage.py migrate

```


2. **Start the development server:**
```bash
python manage.py runserver

```


3. **Open the application:**
Navigate to `http://127.0.0.1:8000/` in your browser (Google Chrome recommended for full Web Speech API support).

---

## Usage

1. Open the web interface in a browser supporting speech APIs (such as Chrome).
2. Tap the prominent **Speak** button (or use the text input field).
3. Speak your query in Tamil (e.g., asking about cooking gas subsidy or eligibility).
4. Listen to the audio response read aloud by the browser while viewing the translated Tamil text on screen.
5. Follow the conversational prompts provided by the agent until you receive final offline instructions.

---

## API / Backend

* **`POST /chat/`**: Receives user input from the frontend JavaScript client, appends the message to the current Django session history, communicates with the Gemini API using the configured system prompt, and returns the response JSON containing the AI-generated Tamil text.

---

## Database

* The application utilizes Django's built-in **Session Framework** (server-side session storage) to maintain conversation history across chat turns. No permanent relational database models are required for the MVP scope.

---

## Limitations

* **Single Scheme Focus:** The current implementation is scoped exclusively to PM Ujjwala Yojana.
* **Language Scope:** Optimized primarily for Tamil interaction in the MVP release.
* **Browser Dependency:** Voice input and output rely on the browser's Web Speech API, which works best on Google Chrome and may have limited support or accuracy on older browsers or non-Chromium mobile environments.
* **Session Persistence:** Conversation histories are session-based and do not persist across browser restarts or long session timeouts.

---

## Future Improvements

* **Multi-Language Support:** Expand system prompts and speech recognition dictionaries to include additional regional Indian languages (Hindi, Telugu, Bengali, Kannada, etc.).
* **Expanded Scheme Catalog:** Integrate multiple welfare schemes spanning healthcare, skill training, and financial inclusion.
* **Database Persistence:** Store user session data securely using Django ORM for multi-session continuity.
* **Cloud Deployment:** Provide containerized deployment scripts (Dockerfile) for cloud platforms like Render or Railway.

---

## Hackathon Development Notes

This project was developed within an intensive 4-hour hackathon timeframe (PromptWars x HACKARENA) by a solo developer. The implementation prioritizes functional simplicity, voice accessibility, and rapid integration with the Gemini API, guided by structured analysis documented during development.

---

## Learning Outcomes

* Rapid prototyping of AI-driven web applications using Python and Django.
* Implementing zero-knowledge, voice-first user interfaces leveraging browser Web Speech APIs.
* Designing effective system prompts for localized, regional language assistant workflows.

---

## Screenshots

*No screenshots are currently included in the repository.*

---

## Contributing

Contributions, bug reports, and feature requests are welcome. Feel free to open an issue or submit a pull request on GitHub.

---

## License

GNU license is currently specified in the repository.

---

## Acknowledgements

* Google for Developers for organizing PromptWars x HACKARENA.
* Google Gemini API for providing the generative AI capabilities.

```
