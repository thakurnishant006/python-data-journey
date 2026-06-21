#-------- Tuple--------------#
num = (1,23,4)
print(type(num))
# Acess the the tuple item
print(num[0])
#----------- Unpacking------------
coordinate = [1,2,3]
x , y, z = coordinate
print(x)
print(y)
print(z)

#-----------------------Functions--------------#
# Function - is a container for a few lines of code make code modular amd reusable chunks to better organise the code
#1
def clean_name(name:str) -> str:
    """Cleans raw name string for database insertion."""
    name = name.strip().title() # Method chaining
    return name

#2
def calculate_bonus(salary: float , rating: int,bonus_rate : float = 0.10) -> float:
    """Rating below 3 returns 0 . Default rate 10%."""
    if rating >= 3:
        return salary*bonus_rate
    else:
        return 0

#3
def safe_divide(a: float , b: float):
    """Returns none if b is zero. Never crashes."""
    if b == 0:
        return None
    else:
        return a/b

#4
def greet(name: str, role: str = "Data Engineer", company: str = "Microsoft") -> str:
    """Returns : Hello Nishant , welcome to Microsoft as a Data engineer!"""
    return f"Hello {name} , welcome to {company} as a {role}! "

#5
def summarise(*numbers) -> dict:
    """Returns count , sum , min , max , avg of any numbers passed."""
    # Prevent the fallback if no number is provided
    if not numbers:
        return "No numbers provided"
    total = sum(numbers)
    count = len(numbers)
    mini = min(numbers)
    maxi = max(numbers)
    avg = total / len(numbers)
    return {
        "count": count,
        "sum": total,
        "min": mini,
        "max": maxi,
        "avg": avg
    }

if __name__ == "__main__":
    print(clean_name("   nishant thakur    "))
    print(calculate_bonus(100000 , 4))
    print(calculate_bonus(100000, 2))
    print(safe_divide(10,0))
    print(greet("Nishant"))
    print(summarise(10,20,30,40,50))