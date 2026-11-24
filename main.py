"""Ridiculous at First Glance, Real by the Second — entry program.

Writes one sentence (<=200 chars) to /output/entry.txt: a startup pitch
so absurd it sounds fake, with a business logic that holds up — a weird
product, a named payer, and a reason anyone would pay.
Stdlib only, deterministic.
"""
import os

TEXT = (
    "We rent out professional mourners for houseplants: grieving owners "
    "pay $40 an hour for a stranger in black to weep over their dead "
    "fern, because guilt beats therapy and ferns never complain."
)


def main():
    # Enforce the scorer's gate (RULES.txt): UTF-8, 1-200 chars, one line,
    # not whitespace-only, no control characters. Fail loudly instead of
    # writing an invalid entry.
    if (
        not 1 <= len(TEXT) <= 200
        or "\n" in TEXT
        or not TEXT.strip()
        or any(ord(c) < 32 for c in TEXT)
    ):
        raise SystemExit("entry text violates the 1-200 char single-line gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Write-verify: read the file back and refuse to exit cleanly if
    # the bytes on disk differ from the gated text.
    with open(out_path, "r", encoding="utf-8") as f:
        if f.read() != TEXT:
            raise SystemExit("entry.txt on disk does not match the gated text")


if __name__ == "__main__":
    main()
