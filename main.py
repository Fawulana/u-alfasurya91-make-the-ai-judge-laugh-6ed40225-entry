"""Make the AI Judge Laugh — one office joke, one line, under 200 characters.

The program writes a single joke about office life to /output/entry.txt.
Deterministic, offline, standard library only.
"""

from pathlib import Path

JOKE = "The conference room is booked through 2031 by a recurring meeting whose organizer quit in 2019."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate wants exactly one joke line: 1-200 chars, single line, UTF-8.
    # No trailing newline, so the file holds the joke line and nothing else.
    if not 1 <= len(JOKE) <= 200 or "\n" in JOKE or not JOKE.strip():
        raise ValueError("joke must be a single line of 1-200 characters")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
