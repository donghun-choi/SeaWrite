"""Command line interface for SeaWrite."""

from __future__ import annotations

import argparse
from pathlib import Path

from .transcriber import transcribe_audio
from .summarizer import summarize_text


def main() -> None:
    parser = argparse.ArgumentParser(description="SeaWrite: lecture transcription and summarization")
    parser.add_argument("audio", help="Path to audio file to transcribe")
    parser.add_argument(
        "--model",
        default="base.en",
        help="whisper.cpp model to use (e.g., base.en)",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Base filename for output (without extension). Defaults to audio filename",
    )
    args = parser.parse_args()

    transcript = transcribe_audio(args.audio, args.model)
    summary = summarize_text(transcript)

    base = args.output or str(Path(args.audio).with_suffix(""))
    with open(base + ".transcript.txt", "w", encoding="utf-8") as f:
        f.write(transcript)
    with open(base + ".summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)


if __name__ == "__main__":  # pragma: no cover
    main()
