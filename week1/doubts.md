## Things I understood clearly:
2d list 
tuple
unpacking
dict program logic--- > till  here previous days
---------- Functions----------
paramaters -> placeholder in the function to recieve information , arguments are the actual piece of information that we supply to the fucntion
def(keyword) function_name(parameters):
    function body
    return statement


add two blank lines

function_name(arguments for functions) => function call

def greet_user(x):
    print(f"Hi {x}")


greet_user("Nishant")
-> defines function first and then call them

Keyword arguments -> are like the value assigned to parameters so that position of argument doesnt matter.
Return statement -> fuction that returns some value

def calc(x,y):
    x = int(x)
    y = int(y)
    return x + y


print(calc(20,20)) # prints 40

- By default the fuction return none value if return keyword not present

- def emoji_con(txt):
    emoji = {
        ":)": "😊",
        ":(": "🙁",
        ":|": "😡",
        ":/": "😕"
    }
    word = txt.split()
    out = ""
    for i in word:
        out += emoji.get(i,i) + " "
    return out


message = input("> ")
print(emoji_con(message))

------------ Handle Error in python--------

Exceptions - try except

try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print("Non integer value")



 => this means instead of crashing the program type this error message on the program
 complete the program with exit code 0

 comments in pyhton => # -> one line """ string literals they are just ignored by python """
## Things that confused me:
unpacked in * and ** in functional call
## Things I want to try in code:

## New words I heard (write them even if you don't know them yet):

args and kwargs
### New thinks i learnd form the corey video
pass -> just continue the function execution ( We donot want to do anything right now but it will not throw any error)
*args - these are used when we dont know how many arguments are comming. 
**kwargs - keyword arguments where we give keyword during the function call
for the args we get the tuple 
for the kwargs we get the dictionable

doc string """ helps to document what the fuctions can do """