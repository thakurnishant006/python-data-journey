## Things I understood clearly:
oops - Classes and instances (Tutorial 1)
clases -> They allow us to logically group data and function in a way thats easy to reuse and also easy to build upon.
data and function -> attributes and methods
class (keyword) class_name:


diff between class and Instance of class:
Class is a blueprint for creating instances.
each new objects we create using the class is the instance of the class
-- emp_1 = class_name() # instance 

- __init__ is a constructor that runs automatically when an object is created.
- self = reference to the current instance of the class , used to access attributes and methods. ( self is the parameter used to receive the object that Python automatically passes when an instance method is called. )
- the argument should be same like put in the parameter.
-  when we run the instance with the class name we need to add instance in the arguments ( because the class doesnt know which instance this suppose to run)

-----Tutorial 2 ( Class Variable)---------------------
class variables are the variables that are shared by all the instances of the class , instance var can be unique but class var must be same.(It is a global variable that can be used any where inside the class )

---------- Tutorial 3 ( Class methods and static methods)


## Things that confused me:
he used +=1 init method used the class name however if he would have used self then what would have happen.
- What is the benefit of the using the class method instead of the regular method
## Things I want to try in code:
decorators
## New words I heard (write them even if you don't know them yet):
decorators - > want to know it deeply
### New thinks i learnd form the corey video
class variables are the variables that are shared by all the instances of the class , instance var can be unique but class var must be same.(It is a global variable that can be used any where inside the class ) we can access it outside of the class

print(emp1.__dict__) -> shows attributes and the values in key value pair.
- if we use class.class_var and changes the value it will be changed for all the methods 
- if we use instance.class_var and changes its value the value will be changed for only the particular instance -> it create a new namespace inside particular methods.
- By default the regular method takes the instance as the first argument in the form of 'self'
- the class method takes the class as the first argument 

- To turn the regular methods into the class methods we use the decorators.
- @classmethod
to use the class method there is a common convetion that we use : cls instead of self -> it will change the value for all the instance as we are using it for the class.
