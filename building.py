from person import *
from headers import *
# from board import *
from king import *


townHall = [
            list(" _   |~  _ "),
            list("TOWN| |HALL"),
            list("[_]--'--[_]"),
            list("| | /^\ | |"),
            list("|_|_|I|_|_|")
]

Hut_design = [
    list("|-HUT-|"),
    list("|     |"),
    list("_|_|_|_")

]

Cannon_design = [
    list("^-__^"),
    list("|CAN|")

]

Wizard_design = [
    list("^-__^"),
    list("|WIZ|")

]




# TOWNHALL HAS 150 VALUE WHICH IS DIVIDED IN 4 PARTS 
# NORMAL HUT HAS 100 VALUE WHICH IS DIVIDED IN 3 PARTS
# Cannon has 80 value which is divided in 3 parts

# boundar coordinates of all buildings 

    





BUILDING_REMAINING = 10



class TownHall(Person):

        def __init__(self, x, y):
            Person.__init__(self,x,y)
            self.__lives=150
         
            self.__destroy_flag = 0
            self.__id = "T"
        def set_destroy_flag(self):
            self.__destroy_flag = 1
        def get_destroy_flag(self):
            return self.__destroy_flag
        def reset_destroy_flag(self):
            self.__destroy_flag = 0
        def set_lives(self,x):
            self.__lives=x
        def get_lives(self):
            return self.__lives
    
        def hall_show(self, grid):
            x = self.getx()
            y = self.gety()
            # print(x)
            # print(y)
            for i in range(y, y+len(townHall)):
                row = []
                for j in range(x, x+len(townHall[0])):
                    
                    # print(i,j)
                    # print(i-y,j-x)
                    gridCopy[i][j] = 'T'
                    grid[i][j] = Fore.WHITE + Back.GREEN + Style.BRIGHT + townHall[i-y][j-x] + Style.RESET_ALL

        def color_town(self,grid):
            x = self.getx()
            y = self.gety()
            if(self.__lives<=100 and self.__lives>=50):

                for i in range(y, y+len(townHall)):
                    for j in range(x, x+len(townHall[0])):
                        grid[i][j] = Fore.WHITE + Back.CYAN + Style.BRIGHT + townHall[i-y][j-x] + Style.RESET_ALL
                        # fuck.append(grid
            if(self.__lives<50 and self.__lives>=20):
                for i in range(y, y+len(townHall)):
                    for j in range(x, x+len(townHall[0])):
                        grid[i][j] = Fore.BLACK + Back.YELLOW + Style.BRIGHT + townHall[i-y][j-x] + Style.RESET_ALL
                        # fuck.append(grid[i][j])

            if(self.__lives<20):
                for i in range(y, y+len(townHall)):
                    for j in range(x, x+len(townHall[0])):
                        grid[i][j] = Fore.WHITE + Back.RED + Style.BRIGHT + townHall[i-y][j-x] + Style.RESET_ALL

        def destroy(self, grid, arr):
            x = self.getx()
            y = self.gety()
            global BUILDING_REMAINING
            BUILDING_REMAINING = BUILDING_REMAINING-1
            for i in range(y, y+len(arr)):
                for j in range(x, x+len(arr[0])):
                    grid[i][j] = " "

        def tabbah(self,grid,obj):
            self.set_lives(self.get_lives() -
                               obj.show_damage_value())
            os.system('aplay -q ./sounds/barbar_attack.wav&')
            self.color_town(grid)
            if(self.get_lives() <= 0):
                self.destroy(grid,townHall)
                clear_copy(ch=self.__id)
                self.set_destroy_flag()

        def balattck(self, grid, obj):
            self.set_lives(self.get_lives()-obj.show_damage_value())
            os.system('aplay -q ./sounds/bal_bomb.wav&')
            self.color_town(grid)
            if(self.get_lives() <= 0):
                self.destroy(grid, townHall)
                clear_copy(ch=self.__id)
                self.set_destroy_flag()

        def arrowattck(self, grid, obj):
            self.set_lives(self.get_lives()-obj.show_damage_value())
            os.system('aplay -q ./sounds/arrow.wav&')
            self.color_town(grid)
            if(self.get_lives() <= 0):
                self.destroy(grid, townHall)
                clear_copy(ch=self.__id)
                self.set_destroy_flag()

        

class Huts(Person):

        def __init__(self, x, y,id):
            Person.__init__(self, x, y)
            self.__lives = 100
          
            self.__id = id
            self.__destroy_flag = 0

        def set_destroy_flag(self):
            self.__destroy_flag = 1

        def get_destroy_flag(self):
            return self.__destroy_flag

        def reset_destroy_flag(self):
            self.__destroy_flag = 0

        def get_id(self):
            return self.__id

        def set_lives(self, x):
            self.__lives = x

        def get_lives(self):
            return self.__lives

        def hut_show(self, grid):
            x = self.getx()
            y = self.gety()
            # print(x)
            # print(y)
            for i in range(y, y+len(Hut_design)):
                for j in range(x, x+len(Hut_design[0])):
                    # print(i, j)
                    # print(i-y, j-x)
                    gridCopy[i][j] = self.get_id()
                    grid[i][j] = Fore.WHITE + Back.GREEN + Style.BRIGHT + \
                        Hut_design[i-y][j-x] + Style.RESET_ALL
        
        def color_hut(self,grid):
            x = self.getx()
            y = self.gety()
            if(self.__lives<50 and self.__lives>=20):
                for i in range(y, y+len(Hut_design)):
                    for j in range(x, x+len(Hut_design[0])):
                        grid[i][j] = Fore.BLACK + Back.YELLOW + Style.BRIGHT + \
                            Hut_design[i-y][j-x] + Style.RESET_ALL
            if(self.__lives<20):
                for i in range(y, y+len(Hut_design)):
                    for j in range(x, x+len(Hut_design[0])):
                        grid[i][j] = Fore.WHITE + Back.RED + Style.BRIGHT + \
                            Hut_design[i-y][j-x] + Style.RESET_ALL
 # Polymorphism
        def destroy(self,grid,arr):
            x = self.getx()
            y = self.gety()
            global BUILDING_REMAINING
            BUILDING_REMAINING = BUILDING_REMAINING-1
            for i in range(y, y+len(arr)):
                for j in range(x, x+len(arr[0])):
                    grid[i][j] = " "

        def barbad(self,grid,obj):
            self.set_lives(self.get_lives()-obj.show_damage_value())
            os.system('aplay -q ./sounds/area_of_effect.wav&')
            self.color_hut(grid)
            if(self.get_lives() <= 0):
                self.destroy(grid,Hut_design)
                clear_copy(ch=self.__id)
                self.set_destroy_flag()

        def tabbah(self,grid,obj):
            self.set_lives(self.get_lives() -
                               obj.show_damage_value())
            os.system('aplay -q ./sounds/barbar_attack.wav&')
            self.color_hut(grid)
            if(self.get_lives() <= 0):
                self.destroy(grid,Hut_design)
                clear_copy(ch=self.__id)
                self.set_destroy_flag()

        def balattck(self, grid, obj):
            self.set_lives(self.get_lives()-obj.show_damage_value())
            os.system('aplay -q ./sounds/bal_bomb.wav&')
            self.color_hut(grid)
            if(self.get_lives() <= 0):
                self.destroy(grid, Hut_design)
                clear_copy(ch=self.__id)
                self.set_destroy_flag()

        def arrowattck(self, grid, obj):
            self.set_lives(self.get_lives()-obj.show_damage_value())
            os.system('aplay -q ./sounds/arrow.wav&')
            self.color_hut(grid)
            if(self.get_lives() <= 0):
                self.destroy(grid, Hut_design)
                clear_copy(ch=self.__id)
                self.set_destroy_flag()
       
        
class cannon(Huts):
    def __init__(self, x, y,id):
        Huts.__init__(self, x, y,id)
        self.__range = 8
        self.__damageValue = 10
        self.__lives = 80
        self.__id = id
        self.__destroy_flag = 0

    def set_destroy_flag(self):
        self.__destroy_flag = 1
    def reset_destroy_flag(self):
        self.__destroy_flag = 0
    def get_destroy_flag(self):
        return self.__destroy_flag
    def set_lives(self, x):
        self.__lives = x
    
    def get_lives(self):
        return self.__lives
    
    def get_id(self):
        return self.__id
    
    def get_range(self):
        return self.__range
    
    def get_damageValue(self):
        return self.__damageValue
    
    

    def cannon_show(self, grid):
        x = self.getx()
        y = self.gety()
        for i in range(y, y+len(Cannon_design)):
            for j in range(x, x+len(Cannon_design[0])):
                gridCopy[i][j] = self.get_id()
                grid[i][j] = Fore.BLACK + Back.WHITE + Style.BRIGHT + \
                    Cannon_design[i-y][j-x] + Style.RESET_ALL

    # def destroy(self,grid):
    #     x = self.getx()
    #     y = self.gety()
    #     global BUILDING_REMAINING
    #     BUILDING_REMAINING = BUILDING_REMAINING-1
    #     for i in range(y, y+len(Cannon_design)):
    #         for j in range(x, x+len(Cannon_design[0])):
    #             grid[i][j] = " "
            
    def color_cannon(self,grid):
        x = self.getx()
        y = self.gety()
        if(self.__lives<60 and self.__lives>=30):
            for i in range(y, y+len(Cannon_design)):
                for j in range(x, x+len(Cannon_design[0])):
                    grid[i][j] = Fore.BLACK + Back.YELLOW + Style.BRIGHT + \
                        Cannon_design[i-y][j-x] + Style.RESET_ALL
        if(self.__lives<30):
            for i in range(y, y+len(Cannon_design)):
                for j in range(x, x+len(Cannon_design[0])):
                    grid[i][j] = Fore.WHITE + Back.RED + Style.BRIGHT + \
                        Cannon_design[i-y][j-x] + Style.RESET_ALL
    
    
    def attack_can(self,grid,arr):
        x = self.getx()
        y = self.gety()
        if(self.__lives>0):
            dist = math.sqrt((x-arr.getx())**2 + (y-arr.gety())**2)
            # fuck.append(dist)
            if(dist<=self.__range):
                if(arr.show_lives()>0):
                    os.system('aplay -q ./sounds/shoot.wav&')

                    arr.set_lives(arr.show_lives()-self.__damageValue)
                    
                    if(arr.show_lives()<=0):
                        arr.set_destroy_flag()
                        grid[arr.gety()][arr.getx()] = " "

    def barbad(self, grid, obj):
        self.set_lives(self.get_lives()-obj.show_damage_value())
        os.system('aplay -q ./sounds/area_of_effect.wav&')
        self.color_cannon(grid)
        if(self.get_lives() <= 0):
            self.destroy(grid,Cannon_design)
            clear_copy(ch=self.__id)
            self.set_destroy_flag()

    def tabbah(self, grid, obj):
        self.set_lives(self.get_lives() -
                        obj.show_damage_value())
        os.system('aplay -q ./sounds/barbar_attack.wav&')
        self.color_cannon(grid)
        if(self.get_lives() <= 0):
            self.destroy(grid,Cannon_design)
            clear_copy(ch=self.__id)
            self.set_destroy_flag()
    
    def balattck(self,grid,obj):
        self.set_lives(self.get_lives()-obj.show_damage_value())
        os.system('aplay -q ./sounds/bal_bomb.wav&')
        self.color_cannon(grid)
        if(self.get_lives() <= 0):
            self.destroy(grid,Cannon_design)
            clear_copy(ch=self.__id)
            self.set_destroy_flag()

    def arrowattck(self,grid,obj):
        self.set_lives(self.get_lives()-obj.show_damage_value())
        os.system('aplay -q ./sounds/arrow.wav&')
        self.color_cannon(grid)
        if(self.get_lives() <= 0):
            self.destroy(grid,Cannon_design)
            clear_copy(ch=self.__id)
            self.set_destroy_flag()
               

class Barbarian(Person):
    def __init__(self, x,y):
        Person.__init__(self, x, y)
        self.__health = 100
        self.__body = np.array(['+'])
        self.__damage_value = 10
        self.__destroy_flag = 0
        self.__mode = 0
        self.__speed = 1

    def set_destroy_flag(self):
        self.__destroy_flag = 1

    def get_destroy_flag(self):
        return self.__destroy_flag

    def get_speed(self):
        return self.__speed

    def set_speed(self):
        self.__speed = 2*self.__speed

    def show_lives(self):
        return self.__health

    def set_lives(self, x):
        self.__health = x

    def show_damage_value(self):
        return self.__damage_value

    def set_mode(self, x):
        self.__mode = x

    def show_mode(self):
        return self.__mode

    def bar_clear(self, grid):
        x = self.getx()
        y = self.gety()
        # print(x)

        grid[y][x] = " "

    def bar_jump(self,grid,ch):
        x = self.getx()
        y = self.gety()
        # print(x)

        grid[y][x] = ch
        

    def start_bar(self, grid):
        x = self.getx()
        y = self.gety()
        for i in range(y, y+1):
            for j in range(x, x+1):
                grid[i][j] = self.__body[0][0]

    def bar_show(self, grid, x, y):
        # ch = grid[y][x]
        self.bar_clear(grid)

        self.setx(x)
        self.sety(y)
        #  if(self.show_shield_flag() == 0):
        for i in range(y, y+1):
            for j in range(x, x+1):
                grid[i][j] = self.__body[0][0]

    def new_bar(self, grid):
        # grid[self.getx()][self.gety()] = " "
        self.sety(self.gety())
        self.setx(self.getx())

        self.bar_show(grid, self.getx(), self.gety(), self.show_mode())

    def color_change(self,grid):
        x = self.getx()
        y = self.gety()
        if(self.__health<=60 and self.__health>=30):
            for i in range(y, y+1):
                for j in range(x, x+1):
                    grid[i][j] = Fore.BLACK + Back.YELLOW + Style.BRIGHT + \
                        self.__body[0][0] + Style.RESET_ALL
        if(self.__health<30):
            for i in range(y, y+1):
                for j in range(x, x+1):
                    grid[i][j] = Fore.WHITE + Back.RED + Style.BRIGHT + \
                        self.__body[0][0] + Style.RESET_ALL
        if(self.__health<=0):
            for i in range(y, y+1):
                for j in range(x, x+1):
                    grid[i][j] = " " 

    def move(self, grid, array_cord, att):
        ans = 100000
        tarx = -1
        tary = -1
        x = self.getx()
        y = self.gety()

        # sx.append(Barb_arr[i].show_damage_value)
        if(self.show_lives() > 0):
            # array_cord = sorted(array_cord, key=lambda x: x[0]**2+x[1]**2)
            for j in range(len(array_cord)):

                    dist = math.sqrt(
                        (y-array_cord[j][0])**2 + (x-array_cord[j][1])**2)
                    if dist < ans:
                        tarx = array_cord[j][0]
                        tary = array_cord[j][1]
                        ans = dist
                # now barbaruan has min distance
            if (abs(tarx-y) > abs(tary-x)):
                # first remove the position of barbarian
                # then set to new position tary (modified) tarx
                self.bar_clear(grid)
                if(tarx < y and y > 2 and y < 38):
                    if att == 0:
                        
                            self.sety(y-self.get_speed())
                            # ch = grid[y-self.get_speed()][x]
                            self.bar_show(
                                grid, x, y-self.get_speed())

                    else:
                        self.bar_show(grid, x, y)
                elif(tarx > y and y > 2 and y < 37):
                    if att == 0:
                        
                            self.sety(y+self.get_speed())
                            self.bar_show(
                                grid, x, y+self.get_speed())

                    else:
                        self.bar_show(grid, x, y)
            else:
                # first remove the position of barbarian
                # then set to new position tarx (modified) tary
                self.bar_clear(grid)
                if(tary > x and x > 1 and x < 197):
                    if att == 0:
                        
                            self.setx(x+self.get_speed())
                            self.bar_show(
                                grid, x+self.get_speed(), y)

                    else:
                        self.bar_show(grid, x, y)
                elif(tary < x and x > 1 and x < 198):
                    if att == 0:
                        
                            self.setx(x-self.get_speed())
                            self.bar_show(
                                grid, x-self.get_speed(), y)

                    else:
                        self.bar_show(grid, x, y)


class Wizard(Huts):
    def __init__(self,x,y,id):
        Huts.__init__(self,x,y,id)
        self.__range = 8
        self.__damage_value = 10
        self.__health = 80
        self.__id = id
        self.__destroy_flag = 0

    def set_destroy_flag(self):
        self.__destroy_flag = 1
    
    def get_destroy_flag(self):
        return self.__destroy_flag
    def reset_destroy_flag(self):
        self.__destroy_flag = 0
    def set_lives(self, x):
        self.__lives = x

    def get_lives(self):
        return self.__lives

    def get_id(self):
        return self.__id

    def get_range(self):
        return self.__range

    def show_damage_value(self):
        return self.__damage_value
    

    def wizzard_show(self,grid):
        x = self.getx()
        y = self.gety()

        for i in range(y, y+len(Wizard_design)):
            for j in range(x, x+len(Wizard_design[0])):
                gridCopy[i][j] = self.get_id()
                grid[i][j] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT + \
                    Wizard_design[i-y][j-x] + Style.RESET_ALL

    def color_wizard(self, grid):
        x = self.getx()
        y = self.gety()
        if(self.__lives < 60 and self.__lives >= 30):
            for i in range(y, y+len(Wizard_design)):
                for j in range(x, x+len(Wizard_design[0])):
                    grid[i][j] = Fore.BLACK + Back.YELLOW + Style.BRIGHT + \
                        Wizard_design[i-y][j-x] + Style.RESET_ALL
        if(self.__lives < 30):
            for i in range(y, y+len(Wizard_design)):
                for j in range(x, x+len(Wizard_design[0])):
                    grid[i][j] = Fore.WHITE + Back.RED + Style.BRIGHT + \
                        Wizard_design[i-y][j-x] + Style.RESET_ALL

    def attack_wiz(self, grid, arr):
        x = self.getx()
        y = self.gety()

        flg = 0
        if(arr.getx()>=x and arr.getx()<=x+len(Wizard_design[0]) and arr.gety()>=y and arr.gety()<=y+len(Wizard_design)):
            flg = 1

        if(self.__lives > 0 and flg == 0):
            dist = math.sqrt((x-arr.getx())**2 + (y-arr.gety())**2) 
            trx = arr.getx()
            tryy = arr.gety()
            cnt =0;
            if(dist <= self.__range):
                for k in range(len(Barb_arr)):
                    if(Barb_arr[k].getx()==trx and Barb_arr[k].gety()==tryy):
                        cnt = cnt+1
                for k in range(len(Arch_arr)):
                    if(Arch_arr[k].getx()==trx and Arch_arr[k].gety()==tryy):
                        cnt = cnt+1

                if(cnt > 4):
                    for k in range(len(Barb_arr)):
                        if(Barb_arr[k].getx() == trx and Barb_arr[k].gety() == tryy):
                            Barb_arr[k].set_lives(0)
                            Barb_arr[k].set_destroy_flag()
                        
                    for k in range(len(Arch_arr)):
                        if(Arch_arr[k].getx() == trx and Arch_arr[k].gety() == tryy):
                            Arch_arr[k].set_lives(0)
                            Arch_arr[k].set_destroy_flag()
                    


                
            # fuck.append(dist)
            if(dist <= self.__range):
                if(arr.show_lives() > 0):
                    os.system('aplay -q ./sounds/shoot.wav&')

                    arr.set_lives(arr.show_lives()-self.__damage_value)

                    if(arr.show_lives() <= 0):
                        arr.set_destroy_flag()
                        grid[arr.gety()][arr.getx()] = " "

    def barbad(self, grid, obj):
        self.set_lives(self.get_lives()-obj.show_damage_value())
        os.system('aplay -q ./sounds/area_of_effect.wav&')
        self.color_wizard(grid)
        if(self.get_lives() <= 0):
            self.destroy(grid, Wizard_design)
            clear_copy(ch=self.__id)
            self.set_destroy_flag()

    def tabbah(self, grid, obj):
        self.set_lives(self.get_lives() -
                       obj.show_damage_value())
        os.system('aplay -q ./sounds/barbar_attack.wav&')
        self.color_wizard(grid)
        if(self.get_lives() <= 0):
            self.destroy(grid, Wizard_design)
            clear_copy(ch=self.__id)
            self.set_destroy_flag()
    
    def balattck(self, grid, obj):
        self.set_lives(self.get_lives()-obj.show_damage_value())
        os.system('aplay -q ./sounds/bal_bomb.wav&')
        self.color_wizard(grid)
        if(self.get_lives() <= 0):
            self.destroy(grid, Wizard_design)
            clear_copy(ch=self.__id)
            self.set_destroy_flag()

    def arrowattck(self, grid, obj):
        self.set_lives(self.get_lives()-obj.show_damage_value())
        os.system('aplay -q ./sounds/arrow.wav&')
        self.color_wizard(grid)
        if(self.get_lives() <= 0):
            self.destroy(grid, Wizard_design)
            clear_copy(ch=self.__id)
            self.set_destroy_flag()



class Ballon(Person):
    def __init__(self, x, y):
        Person.__init__(self, x, y)
        self.__health = 100
        self.__body = np.array(['@'])
        self.__damage_value = 20
        self.__destroy_flag = 0
        self.__mode = 0
        self.__speed = 2

    def set_destroy_flag(self):
        self.__destroy_flag = 1

    def get_destroy_flag(self):
        return self.__destroy_flag

    def get_speed(self):
        return self.__speed

    def set_speed(self):
        self.__speed = 2*self.__speed

    def show_lives(self):
        return self.__health

    def set_lives(self, x):
        self.__health = x

    def show_damage_value(self):
        return self.__damage_value

    def set_mode(self, x):
        self.__mode = x

    def show_mode(self):
        return self.__mode

    def bal_clear(self, grid):
        x = self.getx()
        y = self.gety()
        # print(x)
        
        grid[y][x] = " "

    def start_bal(self, grid):
        x = self.getx()
        y = self.gety()
        for i in range(y, y+1):
            for j in range(x, x+1):
                grid[i][j] = self.__body[0][0]

    def bal_show(self, grid, x, y):
   
        self.bal_clear(grid)

        self.setx(x)
        self.sety(y)
        #  if(self.show_shield_flag() == 0):
        for i in range(y, y+1):
            for j in range(x, x+1):
                grid[i][j] = self.__body[0][0]

    def new_bal(self, grid):
        # grid[self.getx()][self.gety()] = " "
        self.sety(self.gety())
        self.setx(self.getx())
        
        self.bal_show(grid, self.getx(), self.gety(), self.show_mode())

    def color_change(self, grid):
        x = self.getx()
        y = self.gety()
        if(self.__health <= 60 and self.__health >= 30):
            for i in range(y, y+1):
                for j in range(x, x+1):
                    grid[i][j] = Fore.BLACK + Back.CYAN + Style.BRIGHT + \
                        self.__body[0][0] + Style.RESET_ALL
        if(self.__health < 30):
            for i in range(y, y+1):
                for j in range(x, x+1):
                    grid[i][j] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT + \
                        self.__body[0][0] + Style.RESET_ALL
        if(self.__health <= 0):
            for i in range(y, y+1):
                for j in range(x, x+1):
                    grid[i][j] = " "

    def move(self, grid, array_cord, att):
        ans = 100000
        tarx = -1
        tary = -1
        x = self.getx()
        y = self.gety()
        array_cord = sorted(array_cord, key=lambda ar: (y-ar[0])**2 + (x-ar[1])**2)



        # sx.append(Barb_arr[i].show_damage_value)
        if(self.show_lives() > 0):
            tarx = array_cord[0][0]
            tary = array_cord[0][1]
            
            if (abs(tarx-y) > abs(tary-x)):
                # first remove the position of barbarian
                # then set to new position tary (modified) tarx
                self.bal_clear(grid)
                if(tarx < y and y > 2 and y < 38):
                    if att == 0:
                        # self.sety(y-self.get_speed())
                        if(grid[y-3][x] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL and grid[y-2][x] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL and grid[y-1][x] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL):
                            self.bal_show(
                                grid, x-1, y)
                        elif(grid[y-1][x] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL):
                            self.bal_show(
                                grid, x, y-2)
                        elif(grid[y-2][x] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL):
                            self.bal_show(
                                grid, x, y-3)
                        else:
                            self.bal_show(grid, x, y-self.get_speed())
                        
                    else:
                        self.bal_show(grid, x, y)
                elif(tarx > y and y > 2 and y < 37):
                    if att == 0:
                        if(grid[y+3][x] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL and grid[y+2][x] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL and grid[y+1][x] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL):
                            self.bal_show(
                                grid, x+1, y)
                        
                        elif(grid[y+1][x] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL):
                            self.bal_show(
                                grid, x, y+2)
                        elif(grid[y+2][x] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL):
                            self.bal_show(
                                grid, x, y+3)
                        else:
                            self.bal_show(grid, x, y+self.get_speed())
                    else:
                        self.bal_show(grid, x, y)
            else:
                # first remove the position of barbarian
                # then set to new position tarx (modified) tary
                self.bal_clear(grid)
                if(tary > x and x > 1 and x < 197):
                    if att == 0:
                        if(grid[y][x+3] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL and grid[y][x+2] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL and grid[y][x+1] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL):
                            self.bal_show(
                                grid, x, y+1)
                        elif(grid[y][x+1] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL):
                            self.bal_show(
                                grid, x+2, y)
                        elif(grid[y][x+2] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL):
                            self.bal_show(
                                grid, x+3, y)
                        else:
                            self.bal_show(grid, x + self.get_speed(), y)
                    else:
                        self.bal_show(grid, x, y)
                elif(tary < x and x > 1 and x < 198):
                    if att == 0:
                       if (grid[y][x-3] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL and grid[y][x-2] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL and grid[y][x-1] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL):
                            self.bal_show(
                                grid, x, y-1)
                       elif(grid[y][x-1] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL):
                            self.bal_show(
                                grid, x-2, y)
                       elif(grid[y][x-2] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL):
                            self.bal_show(
                                grid, x-3, y)
                       else:
                           self.bal_show(grid,x-self.get_speed(), y)
                    else:
                        self.bal_show(grid, x, y)


class Archer(Person):
    def __init__(self, x, y):
        Person.__init__(self, x, y)
        self.__health = 50
        self.__body = np.array(['*'])
        self.__damage_value = 5
        self.__destroy_flag = 0
        self.__mode = 0
        self.__speed = 2

    def set_destroy_flag(self):
        self.__destroy_flag = 1

    def get_destroy_flag(self):
        return self.__destroy_flag

    def get_speed(self):
        return self.__speed

    def set_speed(self):
        self.__speed = 2*self.__speed

    def show_lives(self):
        return self.__health

    def set_lives(self, x):
        self.__health = x

    def show_damage_value(self):
        return self.__damage_value

    def set_mode(self, x):
        self.__mode = x

    def show_mode(self):
        return self.__mode

    def arch_clear(self, grid):
        x = self.getx()
        y = self.gety()
        # print(x)

        grid[y][x] = " "


    def start_arch(self, grid):
        x = self.getx()
        y = self.gety()
        for i in range(y, y+1):
            for j in range(x, x+1):
                grid[i][j] = self.__body[0][0]

    def arch_show(self, grid, x, y):
        # ch = grid[y][x]
        self.arch_clear(grid)

        self.setx(x)
        self.sety(y)
        #  if(self.show_shield_flag() == 0):
        for i in range(y, y+1):
            for j in range(x, x+1):
                grid[i][j] = self.__body[0][0]

    def new_arch(self, grid):
        # grid[self.getx()][self.gety()] = " "
        self.sety(self.gety())
        self.setx(self.getx())

        self.arch_show(grid, self.getx(), self.gety(), self.show_mode())

    def color_change(self, grid):
        x = self.getx()
        y = self.gety()
        if(self.__health <= 30 and self.__health >= 15):
            for i in range(y, y+1):
                for j in range(x, x+1):
                    grid[i][j] = Fore.WHITE + Back.GREEN + Style.BRIGHT + \
                        self.__body[0][0] + Style.RESET_ALL
        if(self.__health < 15):
            for i in range(y, y+1):
                for j in range(x, x+1):
                    grid[i][j] = Fore.WHITE + Back.RED + Style.BRIGHT + \
                        self.__body[0][0] + Style.RESET_ALL
        if(self.__health <= 0):
            for i in range(y, y+1):
                for j in range(x, x+1):
                    grid[i][j] = " "

    def move(self, grid, array_cord, att):
        ans = 100000
        tarx = -1
        tary = -1
        x = self.getx()
        y = self.gety()

        # sx.append(Barb_arr[i].show_damage_value)
        if(self.show_lives() > 0):
            for j in range(len(array_cord)):

                dist = math.sqrt(
                    (y-array_cord[j][0])**2 + (x-array_cord[j][1])**2)
                if dist < ans:
                    tarx = array_cord[j][0]
                    tary = array_cord[j][1]
                    ans = dist
            # now barbaruan has min distance
            if (abs(tarx-y) > abs(tary-x)):
                # first remove the position of barbarian
                # then set to new position tary (modified) tarx
                self.arch_clear(grid)
                if(tarx < y and y > 2 and y < 38):
                    if att == 0:
                        if(grid[y-3][x] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL and grid[y-2][x] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL and grid[y-1][x] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL):
                            self.arch_show(grid, x-1, y)
                        else:
                            grid[y-1][x] = " "
                            grid[y-2][x] = " "
                            self.arch_show(
                                grid, x, y-self.get_speed())
                        # ch = grid[y-self.get_speed()][x]
                        

                    else:
                        self.arch_show(grid, x, y)
                elif(tarx > y and y > 2 and y < 37):
                    if att == 0:
                        if(grid[y+3][x] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL and grid[y+2][x] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL and grid[y+1][x] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL):
                            self.arch_show(grid, x+1, y)
                        else:
                            grid[y+1][x] = " "
                            grid[y+2][x] = " "
                            self.sety(y+self.get_speed())
                            self.arch_show(
                                grid, x, y+self.get_speed())

                    else:
                        self.arch_show(grid, x, y)
            else:
                # first remove the position of barbarian
                # then set to new position tarx (modified) tary
                self.arch_clear(grid)
                if(tary > x and x > 1 and x < 197):
                    if att == 0:
                        if(grid[y][x+3] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL and grid[y][x+2] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL and grid[y][x+1] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL):
                            self.arch_show(grid, x, y-1)
                        else:
                            grid[y][x+1] = " "
                            grid[y][x+2] = " "
                            self.setx(x+self.get_speed())
                            self.arch_show(
                                grid, x+self.get_speed(), y)

                    else:
                        self.arch_show(grid, x, y)
                elif(tary < x and x > 1 and x < 198):
                    if att == 0:
                        if(grid[y][x-3] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL and grid[y][x-2] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL and grid[y][x-1] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL):
                            self.arch_show(grid, x, y+1)
                        else:
                            grid[y][x-1] = " "
                            grid[y][x-2] = " "
                            self.setx(x-self.get_speed())
                            self.arch_show(
                                grid, x-self.get_speed(), y)

                    else:
                        self.arch_show(grid, x, y)
