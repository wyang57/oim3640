from quiz.engine import run_quiz
from api.client import fetch_careers

def main():
    keyword = run_quiz()
    results = fetch_careers(keyword)
    print("\nCareer Matches\n")
    for job in results:
        print(job)

if __name__ == "__main__":
    main()
