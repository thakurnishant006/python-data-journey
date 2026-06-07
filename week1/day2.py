#---------- Day 2 --------------------------------
# Operators , Conditionals , Loops

# Operators::
x=10
y=3

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)
print(x**y)

# Augmented Assignment
score = 100
score +=10
print(score)
score *=2
print(score)

#Comparision Operator
print(x>y)
print(x<y)
print(x==y)
print(x!=y)
print(x>=y)

# Logical Operator
age = 27
salary = 1500000
print(age > 18 and salary > 1000000)
print(age > 18 or salary > 1000000)
print(not age>30)

# Section 2-------------- If / elif / else-----------------

salary = 1500000


if salary >= 20000000:
    print("Target achieved!")
elif salary >= 1500000:
    print("Almost there , keep pushing!")
else:
    print("keep working hard")


#Practical example
marks = 85
if marks >= 90:
    grade = "A"
elif marks >=80:
    grade = "B"
elif marks >=70:
    grade = "C"
else:
    grade = "F"
print(f"Marks: {marks}, Grade: {grade}")

# Combining Cond :
age = 27
experience = 3
if age <30 and experience >=2:
    print("Young professional with good experience")
else:
    print("Different category")

#For Loop
# Loop over a list
skills = ["Python", "SQL", "Excel", "PowerBI", "Azure"]
for skill in skills:
    print(skill)

print('-'*30)

#loop with range
for i in range(1,6):
    print(f"Day {i} of learning")

print('-'*30)

# Loop over list with condition
salaries = [120000,150000,98000,200000,175000]
for i in salaries:
    if i >= 150000:
        print(f"High: {i}")
    else:
        print(f"Low: {i}")
print('-'*30)

#loop over dictionary
employee = {
    "name": "Nishant",
    "age": 27,
    "role": "Data Analyst",
    "salary": 1500000
}
for key , value in employee.items():
    print(f"{key} : {value}")