"""Summarization utilities powered by OpenAI GPT models."""

from __future__ import annotations

import os
from typing import Optional

try:
    import openai  # type: ignore
except Exception:  # pragma: no cover - openai is optional for tests
    openai = None  # type: ignore

DEFAULT_PROMPT = (
    "Summarize the following lecture transcript into concise bullet-point notes."
)


def summarize_text(text: str, prompt: str = DEFAULT_PROMPT) -> str:
    """Summarize text using OpenAI's chat completion API.

    If the OpenAI API key is not available or the openai package is missing,
    the function returns the original text with an explanatory header.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or openai is None:
        return f"[OpenAI API key not configured]\n{text}"

    openai.api_key = api_key
    response: dict = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text},
        ],
    )
    choice: Optional[dict] = response.get("choices", [{}])[0]
    message: Optional[dict] = choice.get("message") if choice else None
    return message.get("content", "").strip() if message else ""
