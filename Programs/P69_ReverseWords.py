# Reverse Words (Annotated Version)

def reverse_words(text):
    # ❌ VIOLATION: Original directly used input() (not reusable)
    words = text.split()

    # ❌ VIOLATION: No validation for empty string
    if not words:
        return ""

    return ' '.join(words[::-1])


def main():
    user_input = input("Enter sentence: ")
    print(reverse_words(user_input))


if __name__ == "__main__":
    main()
