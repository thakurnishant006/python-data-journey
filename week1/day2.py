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

# ----------Section 3 For Loop-------------------------
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

#----------Section 4 For loop -------------------
count = 1
while count<=5:
    print(f"count: {count}")
    count +=1

print("-"*30)

#Practical example - saving money
saving = 0
target = 1000000
month = 0

while saving < target:
    saving+=50000
    month+=1
    print(f"Month {month}: savings = {saving}")
print(f"Reached target in {month} months")

print("-"*30)

#While with break
number = [10,25,3,47,8,99,12]

for numbers in number:
    if numbers > 50:
        print(f"First number above 50: {numbers}")
        break

salaries = [80000, 150000, 200000, 95000, 175000, 60000]

for sal in salaries:
    if sal >= 150000:
        print(f"Above target: {sal}")
    else:
        print(f"Below target: {sal}")

#9
count = 1
while count <= 5:
    print(count)
    count+=1

#10
balance = 5000
while balance !=0:
    balance -= 1000
print("Account empty")

# Find the greatest number in the List
max_num = [12,3,4,5,6,77,7]
chk = max_num[0]
for i in max_num:
    if chk < i:
        chk = i
print(chk)

# Remove a duplicate from the list 
lst1 = [1,2,3,4,5,1,2,34,5]
unq = []
for i in lst1:
    if unq not in lst1:
        unq.append(i)
print(unq)

# Write a program to translate word into digits
# 1234 => one two three four
mapp = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine"
}
phone = input("Phone: ")
out = ""
for i in phone:
    out+= mapp.get(i,"!") + " "
print(out)
# 1234 => symbol to emoji
emoji = { 
    ":)": "😊", 
    ":(": "🙁", 
    ":|": "😡", 
    ":/": "😕" 
}
# Split => split the list to string
txt = input("> ")
word = txt.split()
out = ""
for i in word:
    out += emoji.get(i, i) + " "
print(out)
