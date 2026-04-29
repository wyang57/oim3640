from quiz.engine import run_quiz
from api.client import fetch_careers

def main():
    profile = run_quiz()
    results = fetch_careers(profile)
    print(results)

if __name__ == "__main__":
    main()
