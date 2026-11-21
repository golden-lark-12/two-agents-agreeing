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


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
