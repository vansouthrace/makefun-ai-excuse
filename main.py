import os

ENTRY = 'Sorry — I spent the deadline refactoring the deadline. It now supports six time zones and zero finished tasks.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
