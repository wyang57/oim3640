def load_text(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def count_words(text):
    words = text.lower().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

def main():
    text = load_text("utopia.txt")
    freq = count_words(text)

    print("Total words:", sum(freq.values()))
    print("Unique words:", len(freq))

    print("Top 10 most common words:")
    for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(word, "-", count)

if __name__ == "__main__":
    main()
