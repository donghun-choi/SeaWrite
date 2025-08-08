# SeaWrite

SeaWrite is a minimal command line tool that demonstrates the core ideas of the
"SeaWrite" lecture transcription concept:

1. **V2T** – Convert recorded audio to text using the local `whisper.cpp` engine.
2. **T2T** – Summarize the resulting transcript into concise lecture notes using
   OpenAI's GPT models.

## Usage

```
python -m seawrite <audio_file>
```

By default this uses the small `base.en` model from `whisper.cpp` and expects a
WAV input file. You can choose a different model with `--model`.

The command produces two files next to the original audio file:

- `<name>.transcript.txt` – raw transcript
- `<name>.summary.txt` – summarized notes

To enable summarization, set an `OPENAI_API_KEY` environment variable. Without
it, the summarizer falls back to returning the original transcript with a notice.

## Development

Install dependencies:

```
pip install -r requirements.txt
```

Run the test suite:

```
pytest
```
