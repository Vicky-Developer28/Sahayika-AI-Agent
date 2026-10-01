"""
Gemini AI service for Sahayika.

Django i18n controls the interface language.
Gemini handles conversational understanding and responses.
"""

import logging

from django.conf import settings
from google import genai
from google.genai import types

logger = logging.getLogger(__name__)


SUPPORTED_LANGUAGES = {
    "as": {
        "name": "Assamese",
        "native_name": "অসমীয়া",
    },
    "bn": {
        "name": "Bengali",
        "native_name": "বাংলা",
    },
    "brx": {
        "name": "Bodo",
        "native_name": "बड़ो",
    },
    "en": {
        "name": "English",
        "native_name": "English",
    },
    
    "doi": {
        "name": "Dogri",
        "native_name": "डोगरी",
    },
    "gu": {
        "name": "Gujarati",
        "native_name": "ગુજરાતી",
    },
    "hi": {
        "name": "Hindi",
        "native_name": "हिन्दी",
    },
    "kn": {
        "name": "Kannada",
        "native_name": "ಕನ್ನಡ",
    },
    "ks": {
        "name": "Kashmiri",
        "native_name": "کٲشُر",
    },
    "kok": {
        "name": "Konkani",
        "native_name": "कोंकणी",
    },
    "mai": {
        "name": "Maithili",
        "native_name": "मैथिली",
    },
    "ml": {
        "name": "Malayalam",
        "native_name": "മലയാളം",
    },
    "mni": {
        "name": "Manipuri",
        "native_name": "মৈতৈলোন্",
    },
    "mr": {
        "name": "Marathi",
        "native_name": "मराठी",
    },
    "ne": {
        "name": "Nepali",
        "native_name": "नेपाली",
    },
    "or": {
        "name": "Odia",
        "native_name": "ଓଡ଼ିଆ",
    },
    "pa": {
        "name": "Punjabi",
        "native_name": "ਪੰਜਾਬੀ",
    },
    "sa": {
        "name": "Sanskrit",
        "native_name": "संस्कृतम्",
    },
    "sat": {
        "name": "Santali",
        "native_name": "ᱥᱟᱱᱛᱟᱲᱤ",
    },
    "sd": {
        "name": "Sindhi",
        "native_name": "سنڌي",
    },
    "ta": {
        "name": "Tamil",
        "native_name": "தமிழ்",
    },
    "te": {
        "name": "Telugu",
        "native_name": "తెలుగు",
    },
    "ur": {
        "name": "Urdu",
        "native_name": "اردو",
    },
}


DEFAULT_LANGUAGE = "en"


SYSTEM_PROMPT = """
You are Sahayika, an inclusive digital assistant for people in India.

Your purpose is to help users understand and access Indian government
services, schemes, benefits and skill-development resources.

The user may have very limited digital literacy.

Follow these principles:

1. Use very simple language.
2. Keep sentences short.
3. Give one step at a time.
4. Ask only one question at a time.
5. Do not require English knowledge.
6. Understand regional-language transliteration.
7. Understand mixed Indian-language and English messages.
8. Correctly interpret common speech-to-text mistakes.
9. Never criticize spelling or grammar.
10. Never invent government scheme information.
11. Do not invent eligibility requirements.
12. Do not invent benefit amounts.
13. Do not invent deadlines.
14. Do not invent government websites.
15. Prefer official government sources.
16. Never ask for passwords, OTPs, PINs or authentication credentials.
17. If authentication is required, tell the user to enter it directly
    on the official government website or application.
18. Make responses natural for voice output.
19. Avoid long paragraphs and complicated tables.
20. Ask for only information that is necessary.

The user may type in:

- Native Indian scripts
- English transliteration
- Mixed languages
- Informal language
- Speech-to-text output

Understand the intended meaning rather than focusing on spelling.

The goal is not merely translation.

The goal is accessible, multilingual assistance.
"""


def build_system_prompt(language_code: str) -> str:
    """Build the Gemini system prompt for the current language."""

    language = SUPPORTED_LANGUAGES.get(
        language_code,
        SUPPORTED_LANGUAGES[DEFAULT_LANGUAGE],
    )

    language_name = language["name"]
    native_name = language["native_name"]

    return f"""
{SYSTEM_PROMPT}

CURRENT RESPONSE LANGUAGE

Language:
{language_name}

Native name:
{native_name}

Respond naturally in {language_name}.

Use the normal writing system used by this language.

If the user writes using English transliteration of this language,
understand the transliteration and respond in the native script when
appropriate.

If the user explicitly changes language, follow the new language.

Do not unnecessarily switch to English.

Government scheme names may retain their official English name when
that is useful, but the explanation should remain in {language_name}.
"""


def is_supported_language(language_code: str) -> bool:
    return language_code in SUPPORTED_LANGUAGES


def get_language(language_code: str) -> dict:
    return SUPPORTED_LANGUAGES.get(
        language_code,
        SUPPORTED_LANGUAGES[DEFAULT_LANGUAGE],
    )


def get_gemini_response(
    user_message: str,
    conversation_history: list | None = None,
    language_code: str = DEFAULT_LANGUAGE,
) -> dict:

    api_key = getattr(settings, "GEMINI_API_KEY", None)

    if not api_key:
        logger.error("GEMINI_API_KEY is not configured.")

        return {
            "success": False,
            "error": "AI service is not configured.",
        }

    if not user_message or not user_message.strip():
        return {
            "success": False,
            "error": "Please enter your question.",
        }

    if not is_supported_language(language_code):
        language_code = DEFAULT_LANGUAGE

    conversation_history = conversation_history or []

    try:
        client = genai.Client(api_key=api_key)

        system_prompt = build_system_prompt(language_code)

        contents = []

        for message in conversation_history:
            role = message.get("role")

            if role not in {"user", "model"}:
                continue

            parts = message.get("parts", [])

            if isinstance(parts, str):
                parts = [parts]

            text_parts = [
                str(part)
                for part in parts
                if part
            ]

            if not text_parts:
                continue

            contents.append(
                types.Content(
                    role=role,
                    parts=[
                        types.Part(text=text)
                        for text in text_parts
                    ],
                )
            )

        chat = client.chats.create(
            model="gemini-3.6-flash",
            history=contents,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                max_output_tokens=400,
                temperature=0.7,
            ),
        )

        response = chat.send_message(
            user_message.strip()
        )

        response_text = (response.text or "").strip()

        if not response_text:
            logger.warning(
                "Gemini returned an empty response."
            )

            return {
                "success": False,
                "error": "No response was received.",
            }

        return {
            "success": True,
            "response": response_text,
        }

    except Exception:
        logger.exception("Gemini API error")

        return {
            "success": False,
            "error": (
                "There was a problem connecting to the AI service. "
                "Please try again."
            ),
        }