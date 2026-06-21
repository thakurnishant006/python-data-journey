#  ============================================================
#  DAY 4 — OOP: Classes, Inheritance, Dunder Methods
#  Concepts used: __init__, self, class variables, instance
#  variables, inheritance, super(), method overriding,
#  __repr__, __str__, composition (Manager holds Employees)
#  ============================================================

class Employee:
    """Base class — represents a generic employee."""

    raise_amt = 1.04  # CLASS variable — shared by every instance
                       # unless a subclass overrides it (see Developer)

    def __init__(self, first, last, pay):
        # __init__ = constructor, runs automatically when an
        # instance is created. self = reference to THIS instance.
        self.first = first   # instance variable — unique per object
        self.last = last
        self.pay = pay
        self.email = f"{self.first}.{self.last}@company.com"

    def apply_raise(self):
        # Accessing the class variable through `self`, NOT through
        # the class name directly (`Employee.raise_amt`).
        # This matters for inheritance: self.raise_amt looks up the
        # value on the INSTANCE's actual class first (e.g. Developer's
        # 1.10), only falling back to Employee's 1.04 if no override
        # exists. Hardcoding `Employee.raise_amt` would have ignored
        # any subclass override — this was a real bug caught while
        # building Developer below.
        self.pay = self.pay * self.raise_amt

    def __repr__(self):
        # Dunder method for DEVELOPERS / debugging / logs.
        # Should look like valid code that could rebuild the object.
        return f" Employee({self.first}, {self.last},{self.pay})"

    def __str__(self):
        # Dunder method for END USERS — readable output.
        # print(obj) uses __str__ if it exists, falls back to
        # __repr__ if __str__ is missing.
        return f'{self.first}{self.last} - {self.email}'


class Developer(Employee):
    """Inherits from Employee. Adds a programming language and
    gets a better raise rate than a generic Employee."""

    raise_amt = 1.10  # overrides Employee's 1.04 — ONLY for Developer
                       # instances. Employee.raise_amt itself is untouched.

    def __init__(self, first, last, pay, prog_lang):
        # super().__init__() calls Employee's constructor so we don't
        # repeat the same first/last/pay/email assignment logic here.
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang  # new attribute, Developer-only


class Manager(Employee):
    """Inherits from Employee. Also HOLDS a list of Employee objects
    (composition) — a Manager manages other Employee/Developer instances."""

    def __init__(self, first, last, pay, employees=None):
        # Why default to None instead of employees=[] directly?
        # Mutable default arguments (like a list) are created ONCE
        # when the function is defined, and then SHARED across every
        # instance that doesn't pass their own value — a classic
        # Python trap. Defaulting to None and building a fresh list
        # inside __init__ avoids that shared-state bug.
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        # Guard against duplicate entries before appending.
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        # Guard against trying to remove someone not in the list.
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        # `i` is each actual Employee/Developer OBJECT in the list,
        # not a string — so we reach its real attributes via i.first,
        # i.last, exactly like dev_1.first would work directly.
        for i in self.employees:
            print(f"{i.first} {i.last}")


if __name__ == "__main__":
    # Only runs when this file is executed directly — not if imported.

    emp_1 = Employee("Nishant", "Thakur", 50000)
    print(repr(emp_1))   # calls __repr__ explicitly
    print(str(emp_1))    # calls __str__ explicitly
    print(emp_1)         # print() automatically uses __str__

    dev_1 = Developer("Nishant", "Thakur", 95000, "Python")
    print(dev_1.email)
    print(dev_1.pay)
    print(dev_1.prog_lang)
    dev_1.apply_raise()
    print(f"{dev_1.pay:.2f}")   # uses Developer's 1.10, not Employee's 1.04
    print(dev_1)                 # inherited __str__ from Employee

    mgr_1 = Manager("Priya", "Sharma", 120000, [dev_1])
    mgr_1.print_emps()           # just Nishant

    dev_2 = Developer("Rohan", "Verma", 80000, "Java")
    mgr_1.add_emp(dev_2)
    mgr_1.print_emps()           # Nishant + Rohan

    mgr_1.remove_emp(dev_1)
    mgr_1.print_emps()           # just Rohan