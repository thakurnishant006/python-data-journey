# Week 1 — Python Foundations
**Nishant's Data Engineering Journey | Days 1–4**

---

## Day 1 — Variables, Strings, Lists, Dicts

### Variables & Data Types
```python
name = "value"          # no $ sign, no semicolon
age = 25                # int
price = 99.99            # float
is_active = True         # boolean — capital T/F, always
```

### F-Strings
```python
f"Hello {name}, you are {age}"     # variables go inside {}
f"Next year: {age + 1}"            # math works directly inside {}
```

### Common String Methods
| Method | What it does |
|---|---|
| `len("python programming")` | `18` — counts every character including spaces |
| `"pyt" in course` | `True`/`False` — checks existence only |
| `course.find("pyt")` | returns index, or `-1` if not found |
| `course[0:3]` | slicing — `[start:stop]`, stop **not included** |
| `course[-1]` | last character — negative index counts from the right |
| `course[::-1]` | reverses the string (step = -1) |
| `"Go! " * 3` | `"Go! Go! Go! "` — repeats the string |

**Key rule:** String methods do **not** change the original.
```python
course.upper()          # returns new string, course unchanged
course = course.upper() # must reassign to save it
```

### Lists
- Ordered, mutable collection of items, accessed by index
- Think of it like one **Excel column**

```python
skills[0]          # first item
skills[-1]         # last item
skills[1:3]        # slice → positions 1 and 2 only
len(skills)        # count of items

skills.append("Azure")     # adds to the END
skills.remove("Excel")     # removes by VALUE, not position
skills[0] = "Django"       # changes item at a specific position
skills.sort()               # sorts in place
skills.reverse()            # reverses in place
"SQL" in skills              # True/False
```

**Key rule:** List methods **change the original directly** — no reassignment needed.
```python
x.pop(1)    # x is now changed
```

### Dictionaries
- Key-value pairs, accessed by **name**, not position
- Think of it like one **Excel row**

```python
employee["name"]            # direct access — errors if key missing
employee.get("bonus", 0)    # SAFE access — returns 0 if key missing
employee["role"] = "Analyst"  # adds new key
employee["salary"] = 1500000  # updates existing key
del employee["city"]        # permanently removes key

"name" in employee           # checks if KEY exists (not value)
employee.keys()              # all keys
employee.values()            # all values
```

**Mental model:**
```
List               = Excel column   (same-type items, ordered)
Dictionary         = Excel row      (named properties of one thing)
List of dicts      = Excel sheet    (a full database table)
```

---

## Day 2 — Operators & Conditionals

### Arithmetic Operators
| Operator | Meaning | Example |
|---|---|---|
| `/` | division — **always returns float** | `10/3 = 3.333` |
| `//` | floor division — drops decimal | `10//3 = 3` |
| `%` | modulus — remainder | `10%3 = 1` |
| `**` | power | `10**3 = 1000` |

### Augmented Assignment
```python
x += 5   # same as x = x + 5
x *= 2   # same as x = x * 2
```

### Common Mistake
```python
==   # compares two values
=    # assigns a value
```

### Conditionals
```python
if condition:
    ...
elif other_condition:
    ...
else:
    ...
# First TRUE condition wins — rest are skipped
```

### Loops
```python
for item in list:           # loops each item automatically
for i in range(1, 6):       # 1,2,3,4,5 — stop NOT included
for key, value in dict.items():   # loops a dictionary
```

**Indentation is critical in Python.** 4 spaces inside `if`/`for`/`while`. Wrong indentation = crash.

---

## Day 3 — Tuples, Functions, Error Handling

### Tuples
- Used to store items, **immutable** — cannot add or delete items once created

### Functions — Core Syntax
```python
def function_name(parameters):
    """Docstring — describes what the function does."""
    function_body
    return statement
```

- **Parameters** = placeholders in the function definition
- **Arguments** = the actual values supplied when calling the function
- Function must be **defined first**, then called

```python
def greet_user(x):
    print(f"Hi {x}")

greet_user("Nishant")
```

### Keyword Arguments
Value explicitly assigned to a parameter name during a call — so the **position no longer matters**.
```python
greet(role="Manager", name="Nishant")   # works fine, order doesn't matter
```

### Return vs Print
```python
def calc(x, y):
    return x + y

print(calc(20, 20))   # 40
```
- A function with no `return` statement returns `None` by default.
- `print()` displays something on screen — it does **not** hand a value back to the caller.
- `return` hands a value back so it can be stored/reused (`result = calc(20,20)`).

### `*args` and `**kwargs`
```python
*args     # unknown number of POSITIONAL arguments → arrives as a TUPLE
**kwargs  # unknown number of KEYWORD arguments    → arrives as a DICT
```

### Type Hints
```python
def clean_name(name: str) -> str:
```
Not strict enforcement — Python won't crash if types don't match. It's a **communication tool** for readability, teammates, and IDEs.

### `if __name__ == "__main__"`
- Every file has a built-in `__name__` variable.
- Running the file **directly** → `__name__` is `"__main__"`.
- **Importing** the file into another script → `__name__` is the filename instead.
- The guard means: *"only run this block if I am the file being executed directly — skip it if I'm being imported."*

### Comments
```python
# single line comment
""" This is NOT a comment — it's a string literal that Python ignores if unused """
```

### Error Handling — try/except
```python
try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Non integer value")
```
Prevents a crash — instead of an unhandled error, the program prints a friendly message and exits cleanly (exit code 0).

### `pass`
Does nothing, just lets execution continue without error. Useful as a placeholder.

---

## Day 4 — Object-Oriented Programming (OOP)

### Classes & Instances
- A **class** is a blueprint for creating objects.
- An **instance** is one actual object built from that blueprint.
```python
class Employee:
    pass

emp_1 = Employee()   # emp_1 is an instance of Employee
```
- **Attributes** = data stored on a class/instance
- **Methods** = functions defined inside a class

### `__init__` and `self`
```python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first # The name before = doesnt matter 
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"
```
- `__init__` is the **constructor** — runs automatically when an instance is created.
- `self` refers to the **current instance** — Python passes it automatically; it's how the method knows which object's data to use.

### Class Variables vs Instance Variables
```python
class Employee:
    raise_amt = 1.04   # CLASS variable — shared by ALL instances

    def __init__(self, first, last, pay):
        self.pay = pay   # INSTANCE variable — unique per object
```
- `Employee.raise_amt = 1.05` → changes it for **every** instance.
- `emp_1.raise_amt = 1.05` → creates a **new instance-level copy**, only affects `emp_1`.
- `emp_1.__dict__` → shows that instance's attributes as a dict.

**⚠️ Critical gotcha:**
```python
def apply_raise(self):
    self.pay = self.pay * self.raise_amt   # OK to READ via self
    self.raise_amt += 1                     # ❌ BUG — creates a new instance var,
                                              #     does NOT update the shared class value
Employee.raise_amt += 1                     # ✅ correct way to update for everyone
```

### Class Methods & Static Methods
```python
class Employee:
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount   # cls = the class itself, not an instance

    @staticmethod
    def is_workday(day):
        # doesn't use self OR cls — just a regular function
        # grouped here because it's logically related to Employee
        ...
```
- Regular method → first parameter is `self` (the instance).
- Class method → first parameter is `cls` (the class) — used for things affecting **all** instances, e.g. **alternative constructors**:
```python
@classmethod
def from_string(cls, emp_str):
    first, last, pay = emp_str.split('-')
    return cls(first, last, int(pay))
```
- Static method → no `self`/`cls` at all. Just a plain function that conceptually belongs inside the class.

### Inheritance
```python
class Developer(Employee):
    raise_amt = 1.10   # overrides parent's raise_amt — only for Developer instances

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)   # reuse parent's __init__, avoid repeating code
        self.prog_lang = prog_lang
```
- Child class inherits all attributes/methods from the parent.
- Can **override** or **add** functionality without ever touching/editing the parent class.
- `super().__init__(...)` calls the parent's constructor instead of rewriting the same assignment lines.
- `help(ClassName)` → shows full class info including inherited methods.

### Dunder (Magic) Methods
```python
def __repr__(self):
    return f"Employee('{self.first}', '{self.last}', {self.pay})"
    # for the DEVELOPER — unambiguous, debugging/logging

def __str__(self):
    return f"{self.first} {self.last} - {self.email}"
    # for the END USER — readable
```
- `print(obj)` uses `__str__` if defined; falls back to `__repr__` if `__str__` is missing.
- Rule of thumb: if defining only one, define `__repr__`.
- Both must use `return`, not `print` — `print` inside them returns `None` and breaks the output.

### Property Decorators
Lets a **method** be accessed like an **attribute** — with getter/setter/deleter control.
```python
@property
def full_name(self):
    return f"{self.first} {self.last}"

@full_name.setter
def full_name(self, name):
    self.first, self.last = name.split(' ')
```

---

## ⚠️ Flagged for Deeper Study (not yet covered in depth)
- Polymorphism, abstraction, encapsulation (the remaining OOP pillars)
- `__repr__` vs `__str__` — deeper edge cases
- Class methods vs static methods — needs more hands-on practice
- Property decorators — getters/setters/deleters in real use cases
- Decorators in general (custom `@decorator` syntax) — scheduled for Week 4

---
*Last updated: Day 4, Week 1*