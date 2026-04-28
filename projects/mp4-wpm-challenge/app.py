import time
import random

def get_random_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Typing speed improves with practice and patience.",
        "Python is a great language for beginners.",
        "Consistency is the key to getting better at anything."
    ]
    return random.choice(sentences)

def start_timer():
    return time.time()

def main():
    print("Welcome to the WPM Challenge.")
    sentence = get_random_sentence()
    print("\nType the following sentence:")
    print(sentence)

    input("\nPress Enter when you are ready to start.")
    start = start_timer()

    user_input = input("\nBegin typing:\n")

    end = time.time()
    elapsed = end - start

    print("\nTime recorded.")
    print(f"Seconds: {elapsed:.2f}")

if __name__ == "__main__":
    main()
