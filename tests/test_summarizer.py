from seawrite.summarizer import summarize_text


def test_summarize_without_api_key(monkeypatch):
    """When no API key is present the original text is returned."""
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    text = "Sample transcript."
    result = summarize_text(text)
    assert text in result
    assert "not configured" in result
