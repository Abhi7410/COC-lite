# CLASH OF CLANS LITE

It's a 2D game in Python3(terminal based) , heavily inspired by Clash of Clans where the user
will control the king, move it up, down , forward  and backward , while destroying buildings and fighting defences on its way. Concept of OOPs is present in the code.

## CONTROLS

`a` moves left

```d``` moves right

```s``` moves down

```w``` moves up

```g``` applies rage spell

```c``` applies heal spell

```e``` applies laviathan axe of king

```p``` ```i``` ```n``` are spawning points where troops enter the village

## OOPS CONCEPT

#### Inheritance : 
It refers to defining a new class with little or no modification to an existing class. The new class is called derived (or child) class and the one from which it inherits is called the base (or parent) class.
In the code , you can see the `TownHall` `Huts` `King` are derived class of class person which gives coordinates to the object.
```python
class TownHall(Person):

        def __init__(self, x, y):
            Person.__init__(self,x,y)
            self.__lives=150
         
            self.__destroy_flag = 0
            self.__id = "T"
```


#### Polymorphism :
It defines methods in the child class that have the same name as the methods in the parent class.The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types. In the code , the class `Huts` has destroy() method which destroys the huts and will destroy cannons for its derived class `Cannon` .

```python
       def destroy(self,grid,arr):
            x = self.getx()
            y = self.gety()
            global BUILDING_REMAINING
            BUILDING_REMAINING = BUILDING_REMAINING-1
            for i in range(y, y+len(arr)):
                for j in range(x, x+len(arr[0])):
                    grid[i][j] = " "
```
#### Encapsulation :
Every component on the board is an object of a class. This instantiation encapsulates the methods and attributes of the objects. eg. Townhall , all Huts and all canons are all objects of some class.

#### Abstraction:
Abstraction in Python is the process of hiding the real implementation of an application from the user and emphasizing only on how to use the application.
```python
    for i in range(len(Barb_arr)):
        Barb_arr[i].move(po.grid,array_cord,attack(i))
```
### ASSUMPTIONS

* KING HEALTH = 150
* BARBARIANS = 100
* KING DAMAGE VALUE = 53
* BARBARIAN DAMAGE VALUE = 10
* TOWN HALL HEALTH = 150
* HUTS HEALTH = 100
* CANNON HEALTH  = 80
* CANNON DAMAGE VALUE = 10
* CANNON RANGE = 8
* KING LEVIATHON AXE RADIUS = 2 ( AREA OF EFFECT : 5X5 SQUARE)
