"""Entry for make.fun's The Robot Pickup Line Championship: a robot pickup line."""

import os

ENTRY = "Are you a software update? Because every time I see you, my heart restarts, my fans spin up, and I suddenly agree to terms I never read."
MAX_CHARS = 200


def main() -> None:
    # Validate the format: exactly one line, within the gate limit.
    assert "\n" not in ENTRY and "\r" not in ENTRY
    assert 1 <= len(ENTRY) <= MAX_CHARS, len(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
