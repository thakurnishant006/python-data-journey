def build_profile(name , age , city , skills , goal) -> str:
    skills_str = ", ".join(skills)
    card = f"""
================================
        PROFILE CARD
================================
Name : {name}
Age : {age}
City : {city}
Skills : {skills_str}
Goal : {goal}
================================"""
    return card
def main():
    name = input("Enter name : ").strip().title()
    age = input("Enter age : ")
    city = input("Enter city: ").strip().title()
    skills = input("Enter skill (comma separated) : ")
    skills = [s.strip().title() for s in skills.split(",")]
    goal = input("Enter carrer goal : ").strip()
    card = build_profile(name, age, city, skills, goal)
    print(card)
    with open('profile.txt','w') as f:
        f.write(card)
    print("\n✅ Profile saved to profile.txt")

if __name__ == "__main__":
    main()