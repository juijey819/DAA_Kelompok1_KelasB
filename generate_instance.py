import random
import csv

alphabet = "abcdefghijklmnopqrstuvwxyz"
random.seed(42)

def mutate(word):
    word = list(word)
    ops = random.randint(1, 3)

    for _ in range(ops):
        op = random.choice(["insert", "delete", "substitute"])

        if op == "insert":
            pos = random.randint(0, len(word))
            char = random.choice(alphabet)
            word.insert(pos, char)

        elif op == "delete" and len(word) > 1:
            pos = random.randint(0, len(word) - 1)
            word.pop(pos)

        elif op == "substitute":
            pos = random.randint(0, len(word) - 1)
            char = random.choice(alphabet)
            word[pos] = char

    return "".join(word)


def generate_dataset():
    with open("data\\indonesian-words.txt", encoding="utf-8") as f:
        words = [w.strip() for w in f if w.strip()]

    pairs = []
    for _ in range(1000):
        rill = random.choice(words)
        fake = mutate(rill)
        pairs.append([rill, fake])

    with open("Rill-Fake dataset.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Rill", "Fake"])
        writer.writerows(pairs)

    print("Dataset berhasil dibuat (1000 pasangan).")


if __name__ == "__main__":
    generate_dataset()
