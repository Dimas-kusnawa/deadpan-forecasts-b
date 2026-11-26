"""Deadpan forecast for Brindlewick, a city that does not exist.

Writes one deadpan weather line to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

ENTRY = "Tomorrow in Brindlewick, expect scattered showers and a high of 18, with the showers landing exclusively on people who forgot an umbrella."


def main() -> None:
    """Write the forecast line to entry.txt with no trailing newline."""
    import os
    from pathlib import Path

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
