def ask(question):
    answer = input(question + " (yes/no): ").strip().lower()
    return answer == "yes"

def main():
    scores = {
        "Sales": 0,
        "Coding": 0,
        "Operations": 0,
        "Creative": 0
    }

    if ask("Do you enjoy talking to clients?"):
        scores["Sales"] += 1
    else:
        scores["Coding"] += 1
        scores["Operations"] += 1

    if ask("Do you like working on a computer for long periods?"):
        scores["Coding"] += 1
    else:
        scores["Sales"] += 1
        scores["Creative"] += 1

    if ask("Do you prefer structured tasks?"):
        scores["Operations"] += 1
    else:
        scores["Creative"] += 1

    if ask("Do you enjoy solving technical problems?"):
        scores["Coding"] += 1
    else:
        scores["Sales"] += 1
    best = max(scores, key=scores.get)
    print("\nYour recommended job category is:", best)

if __name__ == "__main__":
    main()
