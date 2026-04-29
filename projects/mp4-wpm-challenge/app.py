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

def calculate_accuracy(target, typed):
    target_words = target.split()
    typed_words = typed.split()

    correct = 0
    for t, u in zip(target_words, typed_words):
        if t == u:
            correct += 1

    if len(target_words) == 0:
        return 0

    return (correct / len(target_words)) * 100

def calculate_wpm(typed, elapsed_seconds):
    words = len(typed.split())
    minutes = elapsed_seconds / 60
    if minutes == 0:
        return 0
    return words / minutes

def run_test():
    sentence = get_random_sentence()
    print("\nType the following sentence:")
    print(sentence)

    input("\nPress Enter when you are ready to start.")
    start = start_timer()

    user_input = input("\nBegin typing:\n")

    end = time.time()
    elapsed = end - start

    accuracy = calculate_accuracy(sentence, user_input)
    wpm = calculate_wpm(user_input, elapsed)

    print("\nResults:")
    print(f"Time: {elapsed:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"WPM: {wpm:.2f}")

def main():
    print("Welcome to the WPM Challenge.")

    while True:
        run_test()
        again = input("\nTry again? (yes/no): ").strip().lower()
        if again != "yes":
            print("\nThanks for playing.")
            break

if __name__ == "__main__":
    main()
