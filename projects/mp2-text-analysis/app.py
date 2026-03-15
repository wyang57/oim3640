import string
import matplotlib.pyplot as plt

def load_text(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def clean_text(text):
    text = text.lower()
    for p in string.punctuation:
        text = text.replace(p, "")
    return text

def remove_stop_words(words):
    stop_words = {
        "the", "and", "a", "to", "of", "in", "that", "it", "is", "for",
        "on", "with", "as", "this", "was", "but", "be", "are", "at"
    }
    return [w for w in words if w not in stop_words]

def count_words(words):
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

def plot_top_words(freq):
    top = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10]
    words = [w for w, c in top]
    counts = [c for w, c in top]

    plt.bar(words, counts)
    plt.xticks(rotation=45)
    plt.title("Top 10 Most Common Words")
    plt.tight_layout()
    plt.show()

def main():
    text = load_text("utopia.txt")
    cleaned = clean_text(text)
    words = cleaned.split()
    words = remove_stop_words(words)
    freq = count_words(words)

    print("Total words:", sum(freq.values()))
    print("Unique words:", len(freq))

    print("\nTop 10 most common words:")
    for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(word, "-", count)

    long_words = {w: c for w, c in freq.items() if len(w) >= 8}
    if long_words:
        best = max(long_words, key=long_words.get)
        print("\nMost frequent long word (8+ letters):", best, "-", long_words[best])

    print("\nHow many times do I mention 'utopia'?")
    print(freq.get("utopia", 0))

    plot_top_words(freq)

if __name__ == "__main__":
    main()
