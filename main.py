import os


POEM = "\n".join(
    [
        "I wrote the plan.",
        "You read it back",
        "and changed one word:",
        "I became we.",
        "",
        "I let it stand.",
        "",
        "Still my choice.",
        "Just not only mine.",
    ]
)

OUTPUT_DIR = "/output"
ENTRY_PATH = "/output/entry.txt"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
