from headers import *
from building import *
from king import *

class Board:

    #Creates the entire board for the game

    #constructor function
    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.grid = []
        self.__flag = 0

    #function to create the playing board
    def create_board(self):
        for i in range(self.__rows):
            self.temp = []
            for j in range(self.__cols):
                self.temp.append(" ")

            self.grid.append(self.temp)
        # self.grid=np.array(self.grid)

    #function to print the playing board
    def walls_board(self):
        for i in range(self.__rows):
            if(i == 10 ):
                for j in range(self.__cols):
                    if(j >= 0 and j <= 20 or j >= 50 and j <= 65 or j >= 90 and j <= 130 or j >= 170 and j <= 190):
                        self.grid[i][j] = Fore.WHITE + Back.RED + \
                            Style.BRIGHT + "#" + Style.RESET_ALL
            if(i == 32):
                for j in range(self.__cols):
                    if(j >= 50 and j <= 65 or j >= 90 and j <= 130 or j >= 170 and j <= 190):
                        self.grid[i][j] = Fore.WHITE + Back.RED + \
                            Style.BRIGHT + "#" + Style.RESET_ALL
            if(i == 25):
                for j in range(self.__cols):
                    if(j >= 5 and j <= 20 or j >= 185 and j <= 200):
                        self.grid[i][j] = Fore.WHITE + Back.RED + \
                            Style.BRIGHT + "#" + Style.RESET_ALL
            if(i == 19):
                for j in range(self.__cols):
                    if(j >= 20 and j <= 40):
                        self.grid[i][j] = Fore.WHITE + Back.RED + \
                            Style.BRIGHT + "#" + Style.RESET_ALL
            if(i == 24):
                for j in range(self.__cols):
                    if(j >= 65 and j <= 85):
                        self.grid[i][j] = Fore.WHITE + Back.RED + \
                            Style.BRIGHT + "#" + Style.RESET_ALL
            if(i == 15 or i == 28):
                for j in range(self.__cols):
                    if(j >= 130 and j <= 145):
                        self.grid[i][j] = Fore.WHITE + Back.RED + \
                            Style.BRIGHT + "#" + Style.RESET_ALL
            if(i == 21):
                for j in range(self.__cols):
                    if(j >= 90 and j <= 120):
                        self.grid[i][j] = Fore.WHITE + Back.RED + \
                            Style.BRIGHT + "#" + Style.RESET_ALL

        for i in range(self.__rows):
            if(i >= 10 and i <= 21):
                for j in range(self.__cols):
                    if(j == 20 or j == 90):
                        self.grid[i][j] = Fore.WHITE + Back.RED + \
                            Style.BRIGHT + "#" + Style.RESET_ALL
            if(i >= 10 and i <= 15):
                for j in range(self.__cols):
                    if(j == 50):
                        self.grid[i][j] = Fore.WHITE + Back.RED + \
                            Style.BRIGHT + "#" + Style.RESET_ALL
            if(i >= 8 and i <= 24):
                for j in range(self.__cols):
                    if(j == 65):
                        self.grid[i][j] = Fore.WHITE + Back.RED + \
                            Style.BRIGHT + "#" + Style.RESET_ALL
            if(i >= 6 and i <= 15 or i >= 28 and i <= 33):
                for j in range(self.__cols):
                    if(j == 130):
                        self.grid[i][j] = Fore.WHITE + Back.RED + \
                            Style.BRIGHT + "#" + Style.RESET_ALL
            if(i >= 19 and i <= 24):
                for j in range(self.__cols):
                    if(j == 147):
                        self.grid[i][j] = Fore.WHITE + Back.RED + \
                            Style.BRIGHT + "#" + Style.RESET_ALL
            if(i >= 10 and i <= 21):
                for j in range(self.__cols):
                    if(j == 120):
                        self.grid[i][j] = Fore.WHITE + Back.RED + \
                            Style.BRIGHT + "#" + Style.RESET_ALL

    def print_board(self, factor,strr):
        Str = ""
        for i in range(self.__rows):
            row = []
            for j in range(factor, SCREEN+factor):
                # gridCopy[i][j] = self.grid[i][j]
                Str += self.grid[i][j]
                # print(self.grid[i][j], end='')
            Str += '\n'
        
        file = open(file_name,"a")
        file.write(strr)
        file.write(Str)
        # file.write("\n".join(["".join(row) for row in self.grid]))
        # file.write("\n")
        file.close()
        # f.write("\n")
        # f.close()
            # print()
        print(Str, end='')


king_body = Din(4, 4)
huts_arr = []
cans_arr = []
wiz_arr = []
obj_hall = TownHall(110-len(townHall[0]), 20-len(townHall)-1)
hut_obj = Huts(15-len(Hut_design[0]), 10-len(Hut_design)-1, 0)
huts_arr.append(hut_obj)
hut_obj2 = Huts(165-len(Hut_design[0]), 10-len(Hut_design)-1, 1)
huts_arr.append(hut_obj2)
hut_obj3 = Huts(15-len(Hut_design[0]), 35-len(Hut_design)-1, 2)
huts_arr.append(hut_obj3)
hut_obj4 = Huts(165-len(Hut_design[0]), 35-len(Hut_design)-1, 3)
huts_arr.append(hut_obj4)
hut_obj5 = Huts(45-len(Hut_design[0]), 25-len(Hut_design)-1, 4)
huts_arr.append(hut_obj5)
hut_obj6 = Huts(115-len(Hut_design[0]), 30-len(Hut_design)-1, 5)
huts_arr.append(hut_obj6)
can1 = cannon(26, 28, 6)
cans_arr.append(can1)
can2 = cannon(70, 21, 7)
cans_arr.append(can2)
can3 = cannon(135, 12, 8)
# cans_arr.append(can3)
can4 = cannon(135,25,9)
# cans_arr.append(can4)
#headers of the game
wiz1 = Wizard(12,12,'a')
wiz2 = Wizard(50,25,'b')
wiz3 = Wizard(90,27,'c')
wiz4 = Wizard(125,24,'d')

wiz_arr.append(wiz1)
wiz_arr.append(wiz2)
def print_header(newtime,lev,poor):
    global BUILDING_REMAINING
    strik = ""
    strik += Fore.WHITE + Back.LIGHTBLUE_EX + Style.BRIGHT +"             ".center(SCREEN)+Style.RESET_ALL
    print(Fore.WHITE + Back.LIGHTBLUE_EX + Style.BRIGHT +
          "               ".center(SCREEN)+Style.RESET_ALL)
    strik += Fore.WHITE + Back.LIGHTBLUE_EX + Style.BRIGHT +"CLASH OF CLANS LITE".center(SCREEN)+Style.RESET_ALL
    print(Fore.WHITE + Back.LIGHTBLUE_EX + Style.BRIGHT +
          "CLASH OF CLANS LITE".center(SCREEN)+Style.RESET_ALL)
   
    print(Fore.WHITE + Back.LIGHTBLUE_EX + Style.BRIGHT +
          "               ".center(SCREEN)+Style.RESET_ALL)
    strik += Fore.WHITE + Back.LIGHTBLUE_EX + Style.BRIGHT +"             ".center(SCREEN)+Style.RESET_ALL
    lvl = str("LEVEL: " + str(lev))
    print(Fore.WHITE + Back.LIGHTRED_EX + Style.BRIGHT 
           + lvl.center(SCREEN)+Style.RESET_ALL)
    strik+= Fore.WHITE + Back.LIGHTRED_EX + Style.BRIGHT+ lvl.center(SCREEN)+Style.RESET_ALL
    remaining = 10-obj_hall.get_destroy_flag()-hut_obj.get_destroy_flag()-hut_obj2.get_destroy_flag()-hut_obj3.get_destroy_flag()-hut_obj4.get_destroy_flag() - \
        hut_obj5.get_destroy_flag()-hut_obj6.get_destroy_flag()-can1.get_destroy_flag() - \
        can2.get_destroy_flag()-can3.get_destroy_flag()
    stats = str("King Life : " + str(king_body.show_lives()) +
                " |   BUILDINGS: " + str(poor))
    strik += Fore.WHITE + Back.LIGHTRED_EX + Style.BRIGHT +stats.center(SCREEN)
    strik += Fore.WHITE + Back.LIGHTBLUE_EX + Style.BRIGHT + \
        "               ".center(SCREEN)+Style.RESET_ALL
    print(Fore.WHITE + Back.LIGHTRED_EX + Style.BRIGHT + stats.center(SCREEN))
    print(Fore.WHITE + Back.LIGHTBLUE_EX + Style.BRIGHT +
          "               ".center(SCREEN)+Style.RESET_ALL)
    living_bar = '$' * int(int(king_body.show_lives())/10)
    neg_bar = '$' * (15 - int(king_body.show_lives()/10))

    strik += Fore.WHITE + Back.RED + Style.BRIGHT + "Health Bar" + Style.RESET_ALL+'|' + Fore.GREEN + Back.GREEN + living_bar + \
        Back.RESET + Fore.RED + neg_bar + Fore.RESET + '|'
    print(Fore.WHITE + Back.RED + Style.BRIGHT + "Health Bar" + Style.RESET_ALL+
          '|' + Fore.GREEN + Back.GREEN+ living_bar + Back.RESET + Fore.RED + neg_bar + Fore.RESET + '|')
    
    return strik

def cord_set():
    cord_build = []

    if obj_hall.get_destroy_flag() == 0:
        # cord_build.append([18,100])
        for i in range(14, 19):
            for j in range(99, 110):
                cord_build.append([i, j])
    
    for k in range(len(huts_arr)):
        if huts_arr[k].get_destroy_flag() == 0:
            for i in range(huts_arr[k].gety(), huts_arr[k].gety()+3):
                for j in range(huts_arr[k].getx(), huts_arr[k].getx()+7):
                    cord_build.append([i, j])

    for k in range(len(cans_arr)):
        if cans_arr[k].get_destroy_flag() == 0:
            for i in range(cans_arr[k].gety(), cans_arr[k].gety()+2):
                for j in range(cans_arr[k].getx(), cans_arr[k].getx()+5):
                    cord_build.append([i, j])   
   

    for k in range(len(wiz_arr)):
        if wiz_arr[k].get_destroy_flag() == 0:
            for i in range(wiz_arr[k].gety(), wiz_arr[k].gety()+2):
                for j in range(wiz_arr[k].getx(), wiz_arr[k].getx()+5):
                    cord_build.append([i, j])
    return cord_build
    
def bal_set():
    bal_se = []

    for k in range(len(wiz_arr)):
        if wiz_arr[k].get_destroy_flag() == 0:
           bal_se.append([wiz_arr[k].gety()+1, wiz_arr[k].getx()+2])
           bal_se.append([wiz_arr[k].gety(), wiz_arr[k].getx()+1])
           bal_se.append([wiz_arr[k].gety(), wiz_arr[k].getx()+3])
 


    for k in range(len(cans_arr)):
        if cans_arr[k].get_destroy_flag() == 0:
            bal_se.append([cans_arr[k].gety(), cans_arr[k].getx()+3])
            # bal_se.append([cans_arr[k].gety()+1, cans_arr[k].getx()+2])
            bal_se.append([cans_arr[k].gety(), cans_arr[k].getx()+1])


    x = 0
    for k in range(len(wiz_arr)):
        x += wiz_arr[k].get_destroy_flag()
    for k in range(len(cans_arr)):
        x += cans_arr[k].get_destroy_flag()

    if(x == len(wiz_arr)+len(cans_arr)):
        if obj_hall.get_destroy_flag() == 0:

            for i in range(15, 17):
                for j in range(105, 107):
                    bal_se.append([i, j])

        for k in range(len(huts_arr)):
            if huts_arr[k].get_destroy_flag() == 0:
                bal_se.append([huts_arr[k].gety()+1, huts_arr[k].getx()+4])


    return bal_se
