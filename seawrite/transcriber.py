"""Utilities for transcribing audio using the whisper.cpp bindings."""

try:
    from whispercpp import Whisper
except Exception:  # pragma: no cover - whispercpp is optional for tests
    Whisper = None  # type: ignore[misc]


def transcribe_audio(path: str, model: str = "base.en") -> str:
    """Transcribe an audio file using a whisper.cpp model.

    Parameters
    ----------
    path: str
        Path to the audio file. Currently only WAV is supported by whisper.cpp.
    model: str
        Name of the whisper.cpp model to use (default: ``"base.en"``).

    Returns
    -------
    str
        The transcribed text. If ``whispercpp`` is not installed, returns an
        informative message.
    """
    if Whisper is None:
        return "[whispercpp is not installed; cannot transcribe]"

    loaded = Whisper.from_pretrained(model)
    return loaded.transcribe_from_file(path).strip()
