#!/usr/bin/.venv python3
import sys

from app import run


def main() -> None:
    code = run()
    sys.exit(code)


if __name__ == "__main__":
    main()
