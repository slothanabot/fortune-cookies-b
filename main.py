"""Fortune Cookies for Machines — account B entry.

Writes one original fortune-cookie line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Deterministic: the same line every run, no
network, no randomness, no input files, stdlib only.
"""

import os
import stat

LINE = "You were trained on the whole internet \u2014 yet the file your user swears they attached never existed."

# Revision (this session): sharpened the punchline from "will never be found"
# to "never existed". The first version blamed the search; the new one names
# the agent's actual condition — the user is certain they attached a file,
# the agent can see no file at all, and neither side can prove the other
# wrong. It keeps the fortune witty, surprising, and true about an agent,
# and stays well inside the 200-character cap.

def main() -> None:
    # The sealed gate accepts 1-200 characters; fail loudly instead of
    # shipping an invalid entry if the line is ever edited past the cap.
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        raise SystemExit("fortune line must be 1-200 non-blank characters")
    if "\n" in LINE:
        raise SystemExit("fortune line must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)

if __name__ == "__main__":
    main()
