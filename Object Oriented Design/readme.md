# Object Oriented Design:


Is Your code,
- easy to reaad?
- Re-usuable? - No Need to write all the functionality again, just you can reuse code.
- maintainable? 

In Code Review / PR?
Below are the questions asked,
- If we want to add one more attribute, remove one attribute?
- Is your code maintainable? 
- Is your code Reusable?
- are you inherinting correct class?

This is where LOW LEVEL Design comes into picture. How do you create class,  how do you put classes together, how do you create objects, how they talk to each other, which class can see which class.  



#### Core components:
1. Encapsulations
2. Abstraction 
3. Inheritance 
4. Polymorphism (Poly-Many, morphism - forms)





example:

https://youtu.be/R8omJm-Wl34?t=982

Steps:



B. Define classes:

- Define main class (Lift) of system.
    - Think of what all properties main class will be having.
    - Is properties (sub Class eg. direction, state) is going to be use by any other class except lift?
    - can this properties is to be use by any part of the system apart from  lift class?
          - No?
              - Then, Its good idea to put it inside the Lift class. Use method to work on it
              - This will be the private properties of this class. Using getter setter.
          - Yes?
              - Put it in seperate class
    - System - That serve the request


- Should I start with design about the classes.
- Discuss about Decoupling of classes/System?

          






Example:

Low level Design of Elevator:

1. Gather requirements:

    i. Can add/remove elevator
    ii. One or multiple elevator (Service Elevator/ persons elevator)
    iii. Group of elevator
    iv. Number of floor is always fixed
2. Should I start with talking with classes and move forward with Classes?
    
    i. There can be different States of the elevator.
        - Lift State: Ideal / Moving / Not working -- This are the three states I am thinking of right now. If anything comes up we can always add later
        - Directions: Up/Down
       This are the 2 Enums/States, I am thinking this are possibe states (Python enums are useful to represent data that represent a finite set of states)
       
    ii. **Data:** Think about how you will strore Data?
    
        - Vector (Or hashMap, List)
        - There will be two hashMap (One will have going Up request, 2nd one will be of going down)
            - Question is where we want to store this data/Hashmap? System or class?
                - System: Because system is something that will serve requests. or we can create new class scheduler for assigning class.
                - Also, to simplify our system class complexity we will store Hashmap in different class (Schedular).
                - It will be easier, if we define it in other class , because lets say in future we got request/feedback to change something we can modify code of one class.
                - 

    iii. **Class 1: LIFT**   There will be Lift Class:
        - Data: State, Directions, LiftID
        - What all properties it can have?
        - One will be state
        - Also, Direction can be part of lift properties.
        Note: If any of the properties is not going to used by other class, then its better to places inside given class
        
        - This all properties are private properties, so we can define getter/setter method to access it. But I am not mentioning it./
    
    iv. **Class 2: System:** Which will serve the requests
        - Data: Vector <LiftID's >
        - Our system will take request and pass it to other system (Schedular). That will put request in up or down request based on given request
    
    
    v. **Class 3: Schedular/ Manager:** 
        - contains 2 hashmap:
            - 2 Level hashmap. 
            - 3 Level Hashmap looks ugly, not recommendated.
            - **Question**: What will you do if there is 3/4 level hashMap?. In Terms of Time complexity it will be O(1) but code readability will affect. So, I would suggest here to make seprate Object. We can make of composite Class. 
            - Think about the Functionality stack also, what all functionality stack (eg. add, get, set methods) each class will have?
            - 
        - <img width="650" alt="image" src="https://user-images.githubusercontent.com/35987583/180980806-97a9b574-d6d8-477d-b992-92716ab8671b.png">
        - <img width="611" alt="image" src="https://user-images.githubusercontent.com/35987583/180981914-60693481-dbaf-4305-9854-5c98bdf68bf6.png">



        - Once Class design is completed, Ask interview which class you would like me to implement and go into deeper?

        - There are multiple types of requests, and they are treated differently, when object is being treated different for properties it has, one thing we can do is make it seperate object. Here one can be Drop or Call object.
        
        - Explain the request moving from one system to other. with Data Strcture we defined.


        - Make assumption: If there is any other system that servce request. Just define functionality of it.

        - <img width="672" alt="image" src="https://user-images.githubusercontent.com/35987583/180985333-059d4777-951b-4190-9802-3717efe3815f.png">

        - Check if we can decouple any of the class, Like in this case we can get rid of System class and make life talks to schedular class.

4. Code:






