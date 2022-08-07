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



<img width="507" alt="image" src="https://user-images.githubusercontent.com/35987583/183267153-1efc371b-6fab-497f-81b2-1ff22b635110.png">


<img width="775" alt="image" src="https://user-images.githubusercontent.com/35987583/183267869-253f6c11-b63f-49bd-9eba-7153d5f6ba9b.png">
<img width="1017" alt="image" src="https://user-images.githubusercontent.com/35987583/183269040-85ba5ae1-c489-4ff1-b0a5-5e78b6eb9ba3.png">

```diff
+ Adding Properties in one class should not affect the functionality of other class.
+ Use Open (For extension ) - close (For modificaiton) Principal
+ Single Responcibility Principle
```



<img width="1171" alt="image" src="https://user-images.githubusercontent.com/35987583/183269471-c949ac8c-7029-45f0-9b24-edc0b2ad2685.png">

```java
// This enum is used to specify the builder of a guitar
public enum Builder { 

  FENDER, MARTIN, GIBSON, COLLINGS, OLSON, RYAN, PRS, ANY;

  public String toString() {
    switch(this) {
      case FENDER:   return "Fender";
      case MARTIN:   return "Martin";
      case GIBSON:   return "Gibson";
      case COLLINGS: return "Collings";
      case OLSON:    return "Olson";
      case RYAN:     return "Ryan";
      case PRS :     return "PRS";
      default:       return "Unspecified";
    }
  }
}

// This enum is used to specify the type of a guitar
public enum Type { 

  ACOUSTIC, ELECTRIC;

  public String toString() {
    switch(this) {
      case ACOUSTIC: return "acoustic";
      case ELECTRIC: return "electric";
      default:       return "unspecified";
    }
  }
}

// This enum is used to specify the wood of a guitar
public enum Wood { 

  INDIAN_ROSEWOOD, BRAZILIAN_ROSEWOOD, MAHOGANY, MAPLE,
  COCOBOLO, CEDAR, ADIRONDACK, ALDER, SITKA;

  public String toString() {
    switch(this) {
      case INDIAN_ROSEWOOD:    return "Indian Rosewood";
      case BRAZILIAN_ROSEWOOD: return "Brazilian Rosewood";
      case MAHOGANY:           return "Mahogany";
      case MAPLE:              return "Maple";
      case COCOBOLO:           return "Cocobolo";
      case CEDAR:              return "Cedar";
      case ADIRONDACK:         return "Adirondack";
      case ALDER:              return "Alder";
      case SITKA:              return "Sitka";
      default:  return "unspecified";
    }
  }
}

// This class represents a guitar
public class Guitar {

  private String serialNumber;
  private double price;
  GuitarSpec spec;  // GuitarSpec is used to specify a guitar

  public Guitar(String serialNumber, double price, GuitarSpec spec) {
    this.serialNumber = serialNumber;
    this.price = price;
    this.spec = spec;
  }

  public String getSerialNumber() {
    return serialNumber;
  }

  public double getPrice() {
    return price;
  }

  public void setPrice(float newPrice) {
    this.price = newPrice;
  }

  public GuitarSpec getSpec() {
    return spec;
  }
}

// GuitarSpec is used to specify a guitar
// We will use this class to search a guitar in the inventory
public class GuitarSpec {
 
  private Builder builder; 
  private String model;
  private Type type;
  private int numStrings;
  private Wood backWood;
  private Wood topWood;

  public GuitarSpec(Builder builder, String model, Type type,
                    int numStrings, Wood backWood, Wood topWood) {
    this.builder = builder;
    this.model = model;
    this.type = type;
    this.numStrings = numStrings;
    this.backWood = backWood;
    this.topWood = topWood;
  }

  public Builder getBuilder() {
    return builder;
  }

  public String getModel() {
    return model;
  }

  public Type getType() {
    return type;
  }

  public int getNumStrings() {
    return numStrings;
  }

  public Wood getBackWood() {
    return backWood;
  }

  public Wood getTopWood() {
    return topWood;
  }

  public boolean matches(GuitarSpec otherSpec) {
    if (builder != otherSpec.builder)
      return false;
    if ((model != null) && (!model.equals("")) &&
        (!model.toLowerCase().equals(otherSpec.model.toLowerCase())))
      return false;
    if (type != otherSpec.type)
      return false;
    if (numStrings != otherSpec.numStrings)
      return false;
    if (backWood != otherSpec.backWood)
      return false;
    if (topWood != otherSpec.topWood)
      return false;
    return true;
  }
}

// The inventory class
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

public class Inventory {
  private List guitars;

  public Inventory() {
    guitars = new LinkedList();
  }

  public void addGuitar(String serialNumber, double price,
                        GuitarSpec spec) {
    Guitar guitar = new Guitar(serialNumber, price, spec);
    guitars.add(guitar);
  }

  public Guitar getGuitar(String serialNumber) {
    for (Iterator i = guitars.iterator(); i.hasNext(); ) {
      Guitar guitar = (Guitar)i.next();
      if (guitar.getSerialNumber().equals(serialNumber)) {
        return guitar;
      }
    }
    return null;
  }

/* This method returns a list of guitars that matches with the specification 
of searchSpec object */
  public List search(GuitarSpec searchSpec) {
    List matchingGuitars = new LinkedList();
    for (Iterator i = guitars.iterator(); i.hasNext(); ) {
      Guitar guitar = (Guitar)i.next();
      if (guitar.getSpec().matches(searchSpec))
        matchingGuitars.add(guitar);
    }
    return matchingGuitars;
  }
}

// This class is used for testing the Application

import java.util.Iterator;
import java.util.List;

public class AppTester {

  public static void main(String[] args) {
    // Set up Rick's guitar inventory
    Inventory inventory = new Inventory();
    initializeInventory(inventory);

    GuitarSpec whatErinLikes = 
      new GuitarSpec(Builder.FENDER, "Stratocastor", 
                     Type.ELECTRIC, 6, Wood.ALDER, Wood.ALDER);
    List matchingGuitars = inventory.search(whatErinLikes);
    if (!matchingGuitars.isEmpty()) {
      System.out.println("Erin, you might like these guitars:");
      for (Iterator i = matchingGuitars.iterator(); i.hasNext(); ) {
        Guitar guitar = (Guitar)i.next();
        GuitarSpec spec = guitar.getSpec();
        System.out.println("  We have a " +
          spec.getBuilder() + " " + spec.getModel() + " " +
          spec.getType() + " guitar:\n     " +
          spec.getBackWood() + " back and sides,\n     " +
          spec.getTopWood() + " top.\n  You can have it for only $" +
          guitar.getPrice() + "!\n  ----");
      }
    } else {
      System.out.println("Sorry, Erin, we have nothing for you.");
    }
  }

  private static void initializeInventory(Inventory inventory) {
    inventory.addGuitar("11277", 3999.95, 
      new GuitarSpec(Builder.COLLINGS, "CJ", Type.ACOUSTIC, 6,
                     Wood.INDIAN_ROSEWOOD, Wood.SITKA));
    inventory.addGuitar("V95693", 1499.95, 
      new GuitarSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC, 6,
                     Wood.ALDER, Wood.ALDER));
    inventory.addGuitar("V9512", 1549.95, 
      new GuitarSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC, 6,
                     Wood.ALDER, Wood.ALDER));
    inventory.addGuitar("122784", 5495.95, 
      new GuitarSpec(Builder.MARTIN, "D-18", Type.ACOUSTIC, 6,
                     Wood.MAHOGANY, Wood.ADIRONDACK));
    inventory.addGuitar("76531", 6295.95, 
      new GuitarSpec(Builder.MARTIN, "OM-28", Type.ACOUSTIC, 6,
                     Wood.BRAZILIAN_ROSEWOOD, Wood.ADIRONDACK));
    inventory.addGuitar("70108276", 2295.95, 
      new GuitarSpec(Builder.GIBSON, "Les Paul", Type.ELECTRIC, 6,
                     Wood.MAHOGANY, Wood.MAHOGANY));
    inventory.addGuitar("82765501", 1890.95, 
      new GuitarSpec(Builder.GIBSON, "SG '61 Reissue", Type.ELECTRIC, 6,
                     Wood.MAHOGANY, Wood.MAHOGANY));
    inventory.addGuitar("77023", 6275.95, 
      new GuitarSpec(Builder.MARTIN, "D-28", Type.ACOUSTIC, 6,
                     Wood.BRAZILIAN_ROSEWOOD, Wood.ADIRONDACK));
    inventory.addGuitar("1092", 12995.95, 
      new GuitarSpec(Builder.OLSON, "SJ", Type.ACOUSTIC, 12,
                     Wood.INDIAN_ROSEWOOD, Wood.CEDAR));
    inventory.addGuitar("566-62", 8999.95, 
      new GuitarSpec(Builder.RYAN, "Cathedral", Type.ACOUSTIC, 12,
                     Wood.COCOBOLO, Wood.CEDAR));
    inventory.addGuitar("6 29584", 2100.95, 
      new GuitarSpec(Builder.PRS, "Dave Navarro Signature", Type.ELECTRIC, 
                     6, Wood.MAHOGANY, Wood.MAPLE));
  }
}
```

