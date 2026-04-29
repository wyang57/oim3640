def run_quiz():
    print("Welcome to the Career Quiz.")
    print("Answer the questions to get a career suggestion.\n")

    score = 0

    q1 = input("Do you prefer steady tasks or shifting tasks. ").strip().lower()
    if "steady" in q1:
        score += 1

    q2 = input("Do you enjoy people work or data work. ").strip().lower()
    if "data" in q2:
        score += 1

    q3 = input("Do you like planning or adjusting. ").strip().lower()
    if "planning" in q3:
        score += 1

    q4 = input("Do you prefer structured tasks or open tasks. ").strip().lower()
    if "structured" in q4:
        score += 1

    q5 = input("Do you enjoy logic problems or communication problems. ").strip().lower()
    if "logic" in q5:
        score += 1

    if score >= 3:
        return "analysis"
    else:
        return "creative"
