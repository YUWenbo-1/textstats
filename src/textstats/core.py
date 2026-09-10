def word_count(text: str) -> int:
    """Number of whitespace‑separated tokens in `text`."""
    tokens=text.split()
    return len(tokens)


def char_frequencies(text: str) -> dict[str, int]:
    """Count of each character, ignoring whitespace and case."""
    ...


def longest_word(text: str) -> str:
    """The longest token. Raises ValueError on empty input."""
    ...