"""BlinkPay: the worst app idea ever pitched.

Writes a single 180-character sentence pitching BlinkPay, an app that
charges you $0.99 every time you blink, to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import pathlib
import shutil

ENTRY = (
    "BlinkPay is the app that charges you $0.99 every time you blink, "
    "and its $9.99-a-month premium tier generously lets you blink twice "
    "a day before it locks your eyelids until payday."
)


def main() -> None:
    # Gate check: the entry must be one line of 1-240 characters.
    if not 1 <= len(ENTRY) <= 240 or "\n" in ENTRY or not ENTRY.strip():
        raise SystemExit("entry violates the 1-240 character single-line gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        raise SystemExit("MAKEFUN_OUTPUT_DIR is not set")
    out_path = pathlib.Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    # Clear only the directory's contents, never the directory itself:
    # the grader mounts it, and removing it fails with EPERM.
    for child in out_path.iterdir():
        if child.is_dir() and not child.is_symlink():
            shutil.rmtree(child)
        else:
            child.unlink()
    target = out_path / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
