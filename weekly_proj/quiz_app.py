# ---- Flash quiz card --------
def main():
    questions = {
        "Which keyword is used to create a class?": "class",
        "Which parameter refers to the current object inside an instance method": "self",
        "Which function is automatically called when an object is created?": "__init__",
        "What does the *args return?": "tuple",
        "Is tuple mutable?": "no",
        "Is dict ordered?": "yes",
        "Which method adds a key-value pair to a dictionary if the key doesn't already exist?": "setdefault()",
        "Which keyword is used to import module": "import"
    }

    def run_quiz() -> str:
        marks = 0
        q=1
        for key, value in questions.items():
            print(f"Q{q}: {key}")
            ans = input("Your answer: ").strip().lower()

            if ans == value:
                marks += 1
                print("✅ Correct!")
            else:
                print(f"❌ Wrong! Correct answer : {value}")
            q+=1

        per = marks / len(questions) * 100
        return f"Final Score: {marks} - {per:.2f}%"

    print(run_quiz())

if __name__ == "__main__":
    main()