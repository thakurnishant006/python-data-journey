#----- Day 1 - Python Fundamentals----
#Variables & Datatypes

name = "Nishant"
age = 28
salary = 1200000
is_learning = True
print(name)
print(age)
print(salary)
print(is_learning)

#F-strings
print(f"My name is {name} and I am {age} years old")
print(f"In 5 years i will be {age+5}")

#Strings Methods
course = "Python Programming"
print(course.upper())
print(course.capitalize())
print(course.replace("python","data"))
print(len(course))
print(course.find("Pro"))

#In operator
print("python" in course)
print("java" in course)

#String Multiplication
print("-"*30)#print -- 30 times
print("Go! "*3)#gogogo

#slicing
language = "Python"
print(language[0:3])#Pyt
print(language[-1])#n
print(language[-3:])#hon
print(language[::-1])#reverse string nohtyP
#-------------------------------------------------------
#List 
skills = ["Python","SQL", "Excel","Power BI"]

#Acessing Items 
print(skills[0])#Python
print(skills[-1])#Power Bi
print(skills[1:3])#SQL , Excel

#list Info
print(len(skills))#4

#Modifying list
skills.append("Azure")#add azure in last
skills.remove("Excel")#remove the excel
print(skills)

#Change specific item
skills.sort()#sort in alphabetically
print(skills)
skills.reverse() #reverse the items

#check existence
print("SQL" in skills)#True
print("Tableau" in skills)#False

#------------Dictionaries-------------
employee = {
    "name": "Nishant",
    "age": 27,
    "city":"Gurgaon",
    "salary":1200000
}

#-------Accessing the dictionaries-----------
print(employee["name"])#Nishant
print(employee["salary"])#1200000

# Safe acess with default value
print(employee.get("bonus",0))

#Adding a new key
employee["role"] = "Data analyst"
print(employee)# Print the dict

#Updating the key
employee["salary"]= 1500000
print(employee["salary"])

#Check if key exist
print("name" in employee)#True
print("bonus" in employee)#False

#Get all keys and values
print(employee.keys())
print(employee.values())

#Delete a key 
del employee["city"]
print(employee)

#Q1 : Diff between List and dict 
# List We use the list when we want to store the sequence of data and 
# Dict : we use the dictionary when we want to store the related data using key-value
# List : We can access the element using the index; Search may require scanning; It allows duplicates
# Dict : We can acces the element using the keys; Search is faster using the keys: Keys must be unique

#Q2 : .get() do that [] doesn't
# .get() can safely return default value when key is not present and can be used when we are not sure if key is present or not.
# [] raises key error , must be used when we are sure about a key is present

#Q3 : why are strings immutable and list mutable
# String are immutable so that they they can be reused and used as hash map
# List are used when data is subject to change , we can update , insert , delete data without creating new list.