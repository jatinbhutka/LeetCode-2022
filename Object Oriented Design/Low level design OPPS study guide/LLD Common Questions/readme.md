# Common Example of LLD:

- Google Calender
- Hotem Management
- Car Parking System
- Elevator Management
- Tic Tac Toe Game design
- Ticket Booking System
- Vending Machin
- ATM
Note: while Doing this solution, Think about all the topics where SOLID principal is used, Class Diag. looks, Reln between classes.



```diff
+ Good Software design is when you tried and true design pattern and principle. 
- You kept objects loosely coupled.
- You code is open for extension but closed for modification.
- That helps code more reusable,
- You don't have to reowrk/code again to use part of the application over and over again.
- Robust Code=ing style: Your codebase needs to communicate its strength. You must write Python code in a way that reduces failure, even as future maintainers tear it apart and reconstruct it. Writing robust code means deliberately thinking about the future.
```

<img width="865" alt="image" src="https://user-images.githubusercontent.com/35987583/183242745-d5583362-7bef-47ab-ada5-ab7eec0e3279.png">

#### Enum:
![image](https://user-images.githubusercontent.com/35987583/183245427-5855e5d0-7db0-4e85-9038-7a63248b607a.png)

```python

# Python code to demonstrate enumerations
 
# importing enum for enumerations
import enum
 
# creating enumerations using class
class Animal(enum.Enum):
    dog = 1
    cat = 2
    lion = 3
 
# printing enum member as string
print ("The string representation of enum member is : ",end="")
print (Animal.dog)
 
# printing enum member as repr
print ("The repr representation of enum member is : ",end="")
print (repr(Animal.dog))
 
# printing the type of enum member using type()
print ("The type of enum member is : ",end ="")
print (type(Animal.dog))
 
# printing name of enum member using "name" keyword
print ("The name of enum member is : ",end ="")
print (Animal.dog.name)
```
![image](https://user-images.githubusercontent.com/35987583/183246443-f510d71a-dd88-4d31-88f5-e374b766400c.png)


