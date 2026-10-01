"""
Core views for Sahayika.

GET  /        -> main chat page
POST /chat/   -> send message to Gemini
POST /reset/  -> clear conversation history
"""

import json
import logging

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.translation import get_language
from django.views.decorators.http import require_GET, require_POST

from .gemini_service import get_gemini_response


logger = logging.getLogger(__name__)


SESSION_KEY = "conversation_history"
MAX_HISTORY = settings.SAHAYIKA_MAX_HISTORY


def _get_history(request) -> list:
    """Retrieve conversation history from session."""

    return request.session.get(
        SESSION_KEY,
        [],
    )


def _save_history(request, history: list) -> None:
    """Persist conversation history to session."""

    if len(history) > MAX_HISTORY:
        history = history[-MAX_HISTORY:]

    request.session[SESSION_KEY] = history
    request.session.modified = True


@require_GET
def index(request):
    """Serve the main Sahayika interface."""

    return render(
        request,
        "core/index.html",
    )


@require_POST
def chat(request):
    """
    Accept a user message, call Gemini,
    and return a JSON response.
    """

    try:
        body = json.loads(request.body)

    except (json.JSONDecodeError, AttributeError):
        return JsonResponse(
            {
                "success": False,
                "error": "Please enter a message.",
            },
            status=400,
        )

    user_message = body.get("message", "")
    language_code_from_frontend = body.get("language", "")

    if not isinstance(user_message, str):
        return JsonResponse(
            {
                "success": False,
                "error": "Invalid message.",
            },
            status=400,
        )

    user_message = user_message.strip()

    if not user_message:
        return JsonResponse(
            {
                "success": False,
                "error": "Please enter a message.",
            },
            status=400,
        )

    if len(user_message) > 1000:
        return JsonResponse(
            {
                "success": False,
                "error": (
                    "Your question is too long. "
                    "Please ask it briefly."
                ),
            },
            status=400,
        )

    # ---------------------------------------------------------
    # Conversation history
    # ---------------------------------------------------------

    history = _get_history(request)

    # ---------------------------------------------------------
    # Language resolution
    # ---------------------------------------------------------

    # 1. Prioritize the language sent from the frontend JS dropdown
    if language_code_from_frontend:
        language_code = language_code_from_frontend
    else:
        # 2. Fallback to Django's active translation language
        language_code = get_language() or "en"

    # Clean it up (e.g., 'hi-in' becomes 'hi')
    language_code = language_code.split("-")[0].lower()

    # ---------------------------------------------------------
    # Gemini
    # ---------------------------------------------------------

    result = get_gemini_response(
        user_message=user_message,
        conversation_history=history,
        language_code=language_code,
    )

    # ---------------------------------------------------------
    # Successful response
    # ---------------------------------------------------------

    if result["success"]:

        history.append(
            {
                "role": "user",
                "parts": [user_message],
            }
        )

        history.append(
            {
                "role": "model",
                "parts": [result["response"]],
            }
        )

        _save_history(
            request,
            history,
        )

        return JsonResponse(
            {
                "success": True,
                "response": result["response"],
                "language": language_code,
            }
        )

    # ---------------------------------------------------------
    # Gemini error
    # ---------------------------------------------------------

    return JsonResponse(
        {
            "success": False,
            "error": result["error"],
        },
        status=500,
    )

    
@require_POST
def reset(request):
    """Clear the session conversation history."""

    request.session[SESSION_KEY] = []
    request.session.modified = True

    logger.info(
        "Conversation reset for session %s",
        request.session.session_key,
    )

    return JsonResponse(
        {
            "status": "ok",
        }
    )