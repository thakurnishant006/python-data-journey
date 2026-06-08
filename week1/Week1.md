## Day 1 — String Concepts

- Variables: name = "value"
  → No $ sign, no semicolon. Python is cleaner that way.

- Datatypes: int, float, string, boolean
  → boolean is True/False — capital T and F, always.

- F-string: f"Hello {name}, you are {age}"
  → Puts variables directly inside a string. {} is where the variable goes.
  → You can even do math inside: f"Next year: {age + 1}"

- len("python programming") → 18
  → Counts every character including spaces.

- find("pyt") → returns index number, -1 if not found
  → Tells you WHERE in the string something first appears.
  → Returns -1 means not found at all.

- "python" in course → True or False
  → Just checks if something EXISTS in the string. Yes or no.

- Slicing: course[0:3] → "pyt"
  → [start:stop] — start is included, stop is NOT included.
  → Think of it as "from position 0, up to but not including 3"

- course[-1] → last character
  → Negative index counts from the RIGHT side of the string.
  → -1 is last, -2 is second last, and so on.

- course[::-1] → reverses the string
  → The third number in slicing is the "step" — -1 means go backwards.

- "Go! " * 3 → Go! Go! Go!
  → Repeats the string that many times. Space inside quotes matters!

- methods don't change the original string
  → course.upper() gives you uppercase but course is still lowercase.
  → To save it: course = course.upper()

  ## Lists

- List = ordered[Can be accessed through index], mutable[Can be changed after creation] collection of items
## Mutable vs Immutable — The Key Rule

- List methods change the original directly
  → x.pop(1) → x is now changed, no reassignment needed

- String methods don't change the original
  → name.upper() → name is still lowercase
  → must do: name = name.upper() to save it
  → Like an Excel column — one variable, many values

- skills[0] → first item (counting starts at 0)
- skills[-1] → last item (negative counts from right)
- skills[1:3] → slice, gives positions 1 and 2 (stop not included)
- len(skills) → count of items in list

- skills.append("Azure") → adds to the END of list
- skills.remove("Excel") → removes by VALUE not position
- skills[0] = "Django" → changes item at specific position
- skills.sort() → sorts alphabetically or numerically
- skills.reverse() → reverses current order

- "SQL" in skills → True/False, checks if value exists

## Dictionaries

- Dictionary = key-value pairs, like one row in Excel
  → Access by name not position number

- employee["name"] → direct access, error if key missing
- employee.get("bonus", 0) → safe access, returns 0 if missing
  → Always use .get() when key might not exist

- employee["role"] = "Analyst" → adds new key
- employee["salary"] = 1500000 → updates existing key
- del employee["city"] → permanently removes key

- "name" in employee → checks if KEY exists (not value)
- employee.keys() → all keys
- employee.values() → all values

- List = Excel column (collection of same type items)
- Dictionary = Excel row (named properties of one thing)
- List of dictionaries = entire Excel sheet = database table

#----------Day2---------------------------------------
## Day 2 — Operators & Conditionals

- / always returns float: 10/3 = 3.333
- // floor division, removes decimal: 10//3 = 3
- % modulus, gives remainder: 10%3 = 1
- ** power: 10**3 = 1000

- Augmented assignment shortcuts:
  x += 5 → x = x + 5
  x *= 2 → x = x * 2

- == compares, = assigns (common mistake)

- if/elif/else → first true condition wins, rest skipped

- for item in list → loops each item automatically
- for i in range(1,6) → 1,2,3,4,5 (stop not included)
- for key,value in dict.items() → loops dictionary

- Indentation is critical in Python
  → 4 spaces inside if/for/while
  → Wrong indentation = crash

  