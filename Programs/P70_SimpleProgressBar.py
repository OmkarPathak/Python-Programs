# Progress Bar (Annotated Version)

import sys
import time


def progress_bar(count, total, suffix=''):
    # ❌ VIOLATION: No zero division handling
    if total == 0:
        return

    bar_length = 40
    filled_length = int(bar_length * count / total)

    percent = round(100.0 * count / total, 1)
    bar = '=' * filled_length + '-' * (bar_length - filled_length)

    sys.stdout.write(f'\r[{bar}] {percent}% {suffix}')
    sys.stdout.flush()


def main():
    for i in range(11):
        time.sleep(0.2)
        progress_bar(i, 10)


if __name__ == "__main__":
    main()
