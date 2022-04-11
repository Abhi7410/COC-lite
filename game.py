
# from tkinter.tix import Balloon
from click import getchar, progressbar
from matplotlib.pyplot import grid
from headers import *
from board import *
from colorama import init, Fore, Back, Style
from king import *
from building import *
from alarmexception import AlarmException
import time
import math

import sys
import termios
import tty
import signal

HT = 40
SCREEN = 200
WIDTH = 500
# king life deni h kiya nhi 100 h abi
os.system('clear')
start_time = time.time()
screen_time = time.time()
items = list(range(0,100))
walls = []
move = 1
level = 1
x = time.time()
movements = []
BUILDING_REMAINING = 10

po = Board(HT, WIDTH)
po.create_board()
Barb_arr = []
Bal_arr = []
Arch_arr = []



def movekey():
    def alarmhandler(signum, frame):
        raise AlarmException
    
    def user_input(timeout=0.2):
        signal.signal(signal.SIGALRM, alarmhandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            text = getChar()()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''
    INPUT_CHAR = user_input()
    char = INPUT_CHAR

    
    

    if char == 'q' or char == 'Q':
        os.system('tput reset')
        quit()
    if(char=='n'):
        if(len(Barb_arr)<=(level+2)*2):
            bar_obj = Barbarian(100,3)
            bar_obj.set_lives(60)
            Barb_arr.append(bar_obj)

            bar_obj.start_bar(po.grid)


    elif char == 'i':
        if(len(Barb_arr) <= (level+2)*2):

            bar_obj = Barbarian(2,15)
            bar_obj.set_lives(60)
            Barb_arr.append(bar_obj)
            bar_obj.start_bar(po.grid)
        # bar_obj.bar_show(po.grid)
      
    elif char == 'p':
        if(len(Barb_arr) <= (level+2)*2):


            bar_obj = Barbarian(197,9)
            bar_obj.set_lives(60)
            bar_obj.start_bar(po.grid)
            Barb_arr.append(bar_obj)
    
    elif char == 'h':
        if(len(Bal_arr) <= (level+2)):
            bal_obj = Ballon(197,20)
            bal_obj.set_lives(60)
            bal_obj.start_bal(po.grid)
            Bal_arr.append(bal_obj)


    elif char == 'j':
        if(len(Bal_arr)<= level+2):
            bal_obj = Ballon(21,3)
            bal_obj.set_lives(60)
            bal_obj.start_bal(po.grid)
            Bal_arr.append(bal_obj)

    elif char == 'u':
        if(len(Bal_arr)<= level+2):
            bal_obj = Ballon(30,37)
            bal_obj.set_lives(60)
            Bal_arr.append(bal_obj)
            bal_obj.start_bal(po.grid)
    
    elif char == 'k':
        if(len(Arch_arr)<= (level+2)*2):
            arch_obj = Archer(2,23)
            arch_obj.set_lives(30)
            arch_obj.start_arch(po.grid)
            Arch_arr.append(arch_obj)
        
    elif char == 'l':
        if(len(Arch_arr)<= (level+2)*2):
            arch_obj = Archer(140,3)
            arch_obj.set_lives(30)
            arch_obj.start_arch(po.grid)
            Arch_arr.append(arch_obj)
    
    elif char == 'm':
        if(len(Arch_arr)<= (level+2)*2):
            arch_obj = Archer(80,37)
            arch_obj.set_lives(30)
            arch_obj.start_arch(po.grid)
            Arch_arr.append(arch_obj)



    elif char == 'c':
        king_body.set_lives(min(1.5*(king_body.show_lives()),150))
        for i in range(len(Barb_arr)):
            Barb_arr[i].set_lives(min(100,1.5*(Barb_arr[i].show_lives())))
    elif char=='g':
        king_body.set_speed()
        for i in range(len(Barb_arr)):
            Barb_arr[i].set_speed()
    
        # for area of effect sword radius 4 cm
        

     # for rage spell g for heal spell c

    if(king_body.show_lives()<=0):
        return
    
    if char == 'a':
        if(king_body.getx()-1>=2 and po.grid[king_body.gety()][king_body.getx()-1]==" " ):
            movements.append(char)
            king_body.din_clear(po.grid)
            king_body.setx(king_body.getx()-king_body.get_speed())
          
            
            king_body.din_show(po.grid,king_body.getx(),king_body.gety(),king_body.show_mode())
    elif char == 'd':
        if(king_body.getx()+1<=SCREEN-2 and po.grid[king_body.gety()][king_body.getx()+1]==" " ):
            movements.append(char)

            king_body.din_clear(po.grid)
            king_body.setx(king_body.getx()+king_body.get_speed())
            
            king_body.din_show(po.grid,king_body.getx(),king_body.gety(),king_body.show_mode())
    elif char == 'w':
        if(king_body.gety()-1>=2 and po.grid[king_body.gety()-1][king_body.getx()]==" " ):
            movements.append(char)

            king_body.din_clear(po.grid)
            king_body.sety(king_body.gety()-king_body.get_speed())
            
            king_body.din_show(po.grid,king_body.getx(),king_body.gety(),king_body.show_mode())
    elif char== 's':
        if(king_body.gety()+1<=HT-2 and po.grid[king_body.gety()+1][king_body.getx()]==" " ):
            movements.append(char)

            king_body.din_clear(po.grid)
            king_body.sety(king_body.gety()+king_body.get_speed())
            
            king_body.din_show(po.grid,king_body.getx(),king_body.gety(),king_body.show_mode())
    
    elif char == "e":
        # like we have to checkl walls near by + town hut and cannon
        gx = king_body.getx()
        gy = king_body.gety()
        if(king_body.show_body() == 'K'):
            for i in range(gx-2,gx+3):
                for j in range(gy-2,gy+3):
                    if i>=2 and i<=SCREEN-2 and j>=2 and j<=HT-2:
                        if po.grid[j][i] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL :
                            po.grid[j][i] = " "
                        if gridCopy[j][i] == 'T':
                            obj_hall.set_lives(obj_hall.get_lives()-king_body.show_damage_value())
                            os.system('aplay -q ./sounds/area_of_effect.wav&')
                            obj_hall.color_town(po.grid)
                            if(obj_hall.get_lives() <= 0):
                                obj_hall.destroy(po.grid)
                                clear_copy(ch='T')
                                obj_hall.set_destroy_flag()
                        else:
                            for k in range(0,6):
                                if(gridCopy[j][i]==k):
                                    huts_arr[k].barbad(po.grid,king_body)
                            
                            for k in range(6,7+level):
                                if(gridCopy[j][i]==k):
                                    cans_arr[k-6].barbad(po.grid,king_body)
        else:
            last = movements[len(movements)-1]
            choice = {'a':[gx-16,gy],'d':[gx+16,gy],'w':[gx,gy-16],'s':[gx,gy+16]}
             
            if last in choice:
                tarx = choice[last][0]
                tary = choice[last][1]
                poor = 0
                os.system('aplay -q ./sounds/bal_bomb.wav&')
                king_body.set_attack_time(time.time())
                for i in range(tarx-4, tarx+4):
                    for j in range(tary-4, tary+4):
                        mols = 0
                        while(time.time()-king_body.get_attack_time() < 1):
                            mols = mols + 1
                        # if(abs(time.time()-king_body.get_attack_time())<1 and abs(time.time()-king_body.get_attack_time())>0.5):
                        if i >= 2 and i <= SCREEN-2 and j >= 2 and j <= HT-2:
                            if po.grid[j][i] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL:
                                po.grid[j][i] = " "
                            if gridCopy[j][i] == 'T':
                                obj_hall.set_lives(
                                    obj_hall.get_lives()-king_body.show_damage_value())
                                os.system(
                                    'aplay -q ./sounds/area_of_effect.wav&')
                                obj_hall.color_town(po.grid)
                                if(obj_hall.get_lives() <= 0):
                                    obj_hall.destroy(po.grid, townHall)
                                    clear_copy(ch='T')
                                    obj_hall.set_destroy_flag()
                                poor = 1
                                break
                            else:
                                for k in range(0, 6):
                                    if(gridCopy[j][i] == k):
                                        huts_arr[k].barbad(
                                            po.grid, king_body)
                                        poor = 1
                                        break
                                if poor == 1:
                                    break

                                for k in range(6, 7+level):
                                    if(gridCopy[j][i] == k):
                                        cans_arr[k -
                                                    6].barbad(po.grid, king_body)
                                        poor = 1
                                        break
                                if poor == 1:
                                    break
                    if poor == 1:
                        break


               
    elif char== " ":
     
        gx = king_body.getx()
        gy = king_body.gety()
        #to break the wall for king
        if(king_body.show_body()=='K'):
           
            last = movements[len(movements)-1]
            choice = {'a':[gx-1,gy],'d':[gx+1,gy],'w':[gx,gy-1],'s':[gx,gy+1]}
            if last in choice:
                tax = choice[last][0]
                tay = choice[last][1]
                if(po.grid[tay][tax] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL):
                    po.grid[tay][tax] = " "
                
                if(gridCopy[tay][tax] == "T"):
                    obj_hall.tabbah(po.grid,king_body)
                else:
                    for k in range(0,6):
                        if(gridCopy[tay][tax] == k ):
                            huts_arr[k].tabbah(po.grid,king_body)
                    
                    for k in range(6,7+level):
                        if(gridCopy[tay][tax] == k ):
                            cans_arr[k-6].tabbah(po.grid,king_body)
        else:
            last = movements[len(movements)-1]
            choice = {'a': [gx-8, gy], 'd': [gx+8, gy],
                      'w': [gx, gy-8], 's': [gx, gy+8]}

            if last in choice:
                tarx = choice[last][0]
                tary = choice[last][1]
                poor = 0
                for i in range(tarx-2, tarx+2):
                    for j in range(tary-2, tary+2):
                        if i >= 2 and i <= SCREEN-2 and j >= 2 and j <= HT-2:
                            if po.grid[j][i] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL:
                                po.grid[j][i] = " "
                            if gridCopy[j][i] == 'T':
                                obj_hall.set_lives(
                                    obj_hall.get_lives()-king_body.show_damage_value())
                                os.system(
                                    'aplay -q ./sounds/area_of_effect.wav&')
                                obj_hall.color_town(po.grid)
                                if(obj_hall.get_lives() <= 0):
                                    obj_hall.destroy(po.grid, townHall)
                                    clear_copy(ch='T')
                                    obj_hall.set_destroy_flag()
                                poor = 1
                                break
                            else:
                                for k in range(0, 6):
                                    if(gridCopy[j][i] == k):
                                        huts_arr[k].barbad(
                                            po.grid, king_body)
                                        poor = 1
                                        break
                                if poor == 1:
                                    break

                                for k in range(6, 7+level):
                                    if(gridCopy[j][i] == k):
                                        cans_arr[k -
                                                 6].barbad(po.grid, king_body)
                                        poor = 1
                                        break
                                if poor == 1:
                                    break
                    if poor == 1:
                        break

                             
   

# barbarian attack to the buildings
def attack(i):
    x = 0
    if (gridCopy[Barb_arr[i].gety()][Barb_arr[i].getx()+1] == "T" or gridCopy[Barb_arr[i].gety()][Barb_arr[i].getx()-1] == "T" or gridCopy[Barb_arr[i].gety()+1][Barb_arr[i].getx()] == "T" or gridCopy[Barb_arr[i].gety()-1][Barb_arr[i].getx()] == "T"):

        x = 1
        obj_hall.tabbah(po.grid,Barb_arr[i]) 
    else:
        for k in range(0,6):
            if(gridCopy[Barb_arr[i].gety()][Barb_arr[i].getx()+1] == k or gridCopy[Barb_arr[i].gety()][Barb_arr[i].getx()-1] == k or gridCopy[Barb_arr[i].gety()+1][Barb_arr[i].getx()] == k or gridCopy[Barb_arr[i].gety()-1][Barb_arr[i].getx()] == k):
                huts_arr[k].tabbah(po.grid,Barb_arr[i])
                x = 1
                break
        for k in range(6,7+level):
            if(gridCopy[Barb_arr[i].gety()][Barb_arr[i].getx()+1] == k or gridCopy[Barb_arr[i].gety()][Barb_arr[i].getx()-1] == k or gridCopy[Barb_arr[i].gety()+1][Barb_arr[i].getx()] == k or gridCopy[Barb_arr[i].gety()-1][Barb_arr[i].getx()] == k):
                cans_arr[k-6].tabbah(po.grid,Barb_arr[i])
                x = 1
                break
        for k in range(len(wiz_arr)):
            if(gridCopy[Barb_arr[i].gety()][Barb_arr[i].getx()+1] == chr(ord('a')+k) or gridCopy[Barb_arr[i].gety()][Barb_arr[i].getx()-1] == chr(ord('a')+k) or gridCopy[Barb_arr[i].gety()+1][Barb_arr[i].getx()] == chr(ord('a')+k) or gridCopy[Barb_arr[i].gety()-1][Barb_arr[i].getx()] == chr(ord('a')+k)):
                wiz_arr[k].tabbah(po.grid,Barb_arr[i])
                x = 1
                break

           
    return x

def balattack(i):
    x = 0
    for k in range(len(cans_arr)):
        if(cans_arr[k].get_destroy_flag()==0 and Bal_arr[i].gety() >= cans_arr[k].gety() and Bal_arr[i].gety() < cans_arr[k].gety()+2  and Bal_arr[i].getx() >= cans_arr[k].getx() and Bal_arr[i].getx() < cans_arr[k].getx()+4):
            cans_arr[k].balattck(po.grid,Bal_arr[i])
            x = 1
            return x
    
    for k in range(len(wiz_arr)):
        if(wiz_arr[k].get_destroy_flag()==0 and Bal_arr[i].gety() >= wiz_arr[k].gety() and Bal_arr[i].gety() < wiz_arr[k].gety()+2  and Bal_arr[i].getx() >= wiz_arr[k].getx() and Bal_arr[i].getx() < wiz_arr[k].getx()+4):
            wiz_arr[k].balattck(po.grid,Bal_arr[i])
            x = 1
            return x


    for k in range(6):
        if(huts_arr[k].get_destroy_flag()==0 and Bal_arr[i].gety() >= huts_arr[k].gety() and Bal_arr[i].gety() < huts_arr[k].gety()+3  and Bal_arr[i].getx() >= huts_arr[k].getx() and Bal_arr[i].getx() < huts_arr[k].getx()+7):
            huts_arr[k].balattck(po.grid,Bal_arr[i])
            x = 1
            return x

    
    if(obj_hall.get_destroy_flag()==0 and Bal_arr[i].gety() >= obj_hall.gety() and Bal_arr[i].gety() < obj_hall.gety()+5  and Bal_arr[i].getx() >= obj_hall.getx() and Bal_arr[i].getx() < obj_hall.getx()+11):
        obj_hall.balattck(po.grid,Bal_arr[i])
        x = 1

    return x


def Archattack(i):
    l = 0 
    x = Arch_arr[i].getx()
    y = Arch_arr[i].gety()
    if(obj_hall.get_destroy_flag()==0):
        for xx in range(obj_hall.getx(),obj_hall.getx()+11):
            for yy in range(obj_hall.gety(),obj_hall.gety()+5):
                dist = math.sqrt((xx-x)**2 + (yy-y)**2)
                if(dist <= 5):
                    obj_hall.arrowattck(po.grid,Arch_arr[i])
                    l = 1
                    return l
    
    for k in range(6):
        if(huts_arr[k].get_destroy_flag()==0):
            for xx in range(huts_arr[k].getx(),huts_arr[k].getx()+7):
                for yy in range(huts_arr[k].gety(),huts_arr[k].gety()+3):
                    dist = math.sqrt((xx-Arch_arr[i].getx())**2 + (yy-Arch_arr[i].gety())**2)
                    if(dist <= 5 ):
                        huts_arr[k].arrowattck(po.grid,Arch_arr[i])
                        l = 1
                        return l
           
    for k in range(len(cans_arr)):
        if(cans_arr[k].get_destroy_flag()==0):
            for xx in range(cans_arr[k].getx(),cans_arr[k].getx()+3):
                for yy in range(cans_arr[k].gety(),cans_arr[k].gety()+2):
                    dist = math.sqrt((xx-Arch_arr[i].getx())**2 + (yy-Arch_arr[i].gety())**2)
                    if(dist <= 5 ):
                        cans_arr[k].arrowattck(po.grid,Arch_arr[i])
                        l = 1
                        return l

    for k in range(len(wiz_arr)):
        if(wiz_arr[k].get_destroy_flag()==0):
            for xx in range(wiz_arr[k].getx(),wiz_arr[k].getx()+3):
                for yy in range(wiz_arr[k].gety(),wiz_arr[k].gety()+2):
                    dist = math.sqrt((xx-Arch_arr[i].getx())**2 + (yy-Arch_arr[i].gety())**2)
                    if(dist <= 5 ):
                        wiz_arr[k].arrowattck(po.grid,Arch_arr[i])
                        l = 1
                        return l

    return l

def level_grid(lev):
    bg = Background()
    bg.display_ceil(po.grid)
    bg.display_floor(po.grid)
    obj_hall.hall_show(po.grid)
    obj_hall.reset_destroy_flag()
    obj_hall.set_lives(300)
    for i in range(6):
        huts_arr[i].hut_show(po.grid)
        huts_arr[i].set_lives(100)
        huts_arr[i].reset_destroy_flag()
    for i in range(lev+1):
        cans_arr[i].cannon_show(po.grid)
        cans_arr[i].set_lives(80)
        cans_arr[i].reset_destroy_flag()
    bg.display_side(po.grid)
    bg.spawningpoint(po.grid)
    bg.spawningballon(po.grid)
    bg.spawningqueen(po.grid)
    king_body.set_lives(150)
    for i in range(len(wiz_arr)):
        wiz_arr[i].set_lives(80)
        wiz_arr[i].wizzard_show(po.grid)
        wiz_arr[i].reset_destroy_flag()
    king_body.start_pos(po.grid)
    
    Barb_arr.clear()
    Bal_arr.clear()
    Arch_arr.clear()
    po.walls_board()
    po.create_board()
    po.print_board(0,print_header(0,lev,9+ 2*lev))


def defeat():
    
    flag = king_body.get_destroy_flag()
    for i in range(len(Barb_arr)):
        flag = flag and Barb_arr[i].get_destroy_flag()
    
    return flag


def start():
    x = 0
    print(Fore.WHITE + Back.LIGHTRED_EX + Style.BRIGHT + "Which one you want to choose King or Archer Queen? 1 for King and 2 for Archer Queen".center(SCREEN) + Style.RESET_ALL)

    def alarmhandler(signum, frame):
        raise AlarmException

    def user_input(timeout=10):
        signal.signal(signal.SIGALRM, alarmhandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            text = getChar()()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''
    INPUT_CHAR = user_input()
    char = INPUT_CHAR
    if char == '1':
        x = 1
    elif char == '2':
        x = 2
    else:
        print("Invalid input")
        quit()

    # f.write(char)
    # f.write("\n")

    os.system('clear')
    return x
    
    

owner = start()
if(owner == 1 ):
    king_body.change_body('K')
else:
    king_body.change_body('Q')

level_grid(1)


while True:
    #remove cursor
    os.system('tput civis')
    reposition_cursor(0,0)
    newtime = GAMETIME - (round(time.time()) - round(start_time))
   
    """  """
    # winning condition
    tot = 11
    if(obj_hall.get_destroy_flag() == True):
        tot = tot - 1
    for i in range(2):
        tot = tot - cans_arr[i].get_destroy_flag()
    for i in range(6):
        tot = tot - huts_arr[i].get_destroy_flag()
    for i in range(2):
        tot = tot - wiz_arr[i].get_destroy_flag()
    

    if (level == 1 and tot == 0):
        # print("YOU WON")
        level = level + 1

        for i in range(len(Barb_arr)):
            Barb_arr[i].bar_clear(po.grid)
        
        for i in range(len(Bal_arr)):
            Bal_arr[i].bal_clear(po.grid)

        for i in range(len(Arch_arr)):
            Arch_arr[i].arch_clear(po.grid)

        
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT +"CONGRATULATIONS!".center(SCREEN)+Style.RESET_ALL)
        # print(level)
        time.sleep(1)

        os.system('clear')

        print(Fore.LIGHTGREEN_EX+Style.BRIGHT +
              "Do you want to play next Level ? ".center(SCREEN) +Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT +"1. Yes".center(SCREEN)+Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT +"2. No".center(SCREEN)+Style.RESET_ALL)
        # print(Fore.LIGHTGREEN_EX+Style.BRIGHT +"3. Quit".center(SCREEN)+Style.RESET_ALL)
        
        def alarmhandler(signum, frame):
            raise AlarmException

        def user_input(timeout=10):
            signal.signal(signal.SIGALRM, alarmhandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            try:
                text = getChar()()
                signal.alarm(0)
                return text
            except AlarmException:
                pass
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return ''
        INPUT_CHAR = user_input()
        char = INPUT_CHAR
        if(char == '1'):
            break
        elif(char == '2'):
            os.system('clear')
            quit()
        else:
            print("Invalid input")
            os.system('clear')
            quit()






        # print(gridCopy)
        # yay()
        # break
        
        # quit()
    if(defeat() == 1):
        os.system('clear')
        game_over()

        print()

        print(Fore.MAGENTA+Style.BRIGHT +
              "BETTER LUCK NEXT TIME!".center(SCREEN)+Style.RESET_ALL)

        quit()
    
    po.create_board()
    strik = print_header(newtime,level,tot)
    
    po.print_board(0,strik)
    # walls store
    for i in range(HT):
        for j in range(SCREEN):
            if(po.grid[i][j] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL):
                 walls.append([i,j])

    movekey()


    array_cord = cord_set()
    ar = bal_set()
    # print(array_cord)
    sx = []
    # loops on barbarian

    cans_arr[0].attack_can(po.grid,king_body)
    cans_arr[1].attack_can(po.grid,king_body)

    for i in range(len(wiz_arr)):
        wiz_arr[i].attack_wiz(po.grid,king_body)
    # attack for barbarian

    
    for i in range(len(Barb_arr)):
        Barb_arr[i].move(po.grid,array_cord,attack(i))
        Barb_arr[i].color_change(po.grid)     
    


    for i in range(len(Bal_arr)):
        for j in range(0,2):
            wiz_arr[j].attack_wiz(po.grid,Bal_arr[i])

    for i in range(len(Bal_arr)):
        Bal_arr[i].move(po.grid,ar,balattack(i))
        Bal_arr[i].color_change(po.grid)

    for i in range(len(Arch_arr)):
        Arch_arr[i].move(po.grid, array_cord, Archattack(i))
        Arch_arr[i].color_change(po.grid)

    # Archer attck
    for i in range(len(Arch_arr)):
        for j in range(0, 2):
            cans_arr[j].attack_can(po.grid, Arch_arr[i])

    for i in range(len(Arch_arr)):
        for j in range(0, 2):
            wiz_arr[j].attack_wiz(po.grid, Arch_arr[i])

    for i in range(len(Barb_arr)):
        for j in range(0, 2):
            cans_arr[j].attack_can(po.grid, Barb_arr[i])

    for i in range(len(Barb_arr)):
        for j in range(0, 2):
            wiz_arr[j].attack_wiz(po.grid, Barb_arr[i])

    os.system('clear')
   


if(level==2):
    # print("LEVEL 2")
    os.system('clear')
    reposition_cursor(0,0)
    wiz_arr.append(wiz3)
    cans_arr.append(can3)
    level_grid(2)
    # wiz_arr[2].reset_destroy_flag()
    # cans_arr[3].set_destroy_flag()
    

    while True:
        #remove cursor
        os.system('tput civis')
        # reposition_cursor(0,0)
        newtime = GAMETIME - (round(time.time()) - round(start_time))
        """  """
        # winning condition
        tot = 13
        if(obj_hall.get_destroy_flag() == True):
            tot = tot - 1
        for i in range(3):
            tot = tot - cans_arr[i].get_destroy_flag()
        for i in range(6):
            tot = tot - huts_arr[i].get_destroy_flag()
        for i in range(3):
            tot = tot - wiz_arr[i].get_destroy_flag()
        if (level == 2 and tot == 0):
           
            # print("YOU WON")
            level= level + 1
            print()

            for i in range(len(Barb_arr)):
                Barb_arr[i].bar_clear(po.grid)

            for i in range(len(Bal_arr)):
                Bal_arr[i].bal_clear(po.grid)

            for i in range(len(Arch_arr)):
                Arch_arr[i].arch_clear(po.grid)
            print(Fore.LIGHTGREEN_EX+Style.BRIGHT +
                  "CONGRATULATIONS!".center(SCREEN)+Style.RESET_ALL)
        # print(level)
            time.sleep(1)

            os.system('clear')

            print(Fore.LIGHTGREEN_EX+Style.BRIGHT +
                "Do you want to play next Level ?".center(SCREEN) + Style.RESET_ALL)
            print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT +
                "1. Yes".center(SCREEN)+Style.RESET_ALL)
            print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT +
                "2. No".center(SCREEN)+Style.RESET_ALL)
            # print(Fore.LIGHTGREEN_EX+Style.BRIGHT +"3. Quit".center(SCREEN)+Style.RESET_ALL)

            def alarmhandler(signum, frame):
                raise AlarmException

            def user_input(timeout=10):
                signal.signal(signal.SIGALRM, alarmhandler)
                signal.setitimer(signal.ITIMER_REAL, timeout)
                try:
                    text = getChar()()
                    signal.alarm(0)
                    return text
                except AlarmException:
                    pass
                signal.signal(signal.SIGALRM, signal.SIG_IGN)
                return ''
            INPUT_CHAR = user_input()
            char = INPUT_CHAR
            if(char == '1'):
                break
            elif(char == '2'):
                os.system('clear')
                quit()
            else:
                print("Invalid Input")
                os.system('clear')
                quit()
            
            # quit()
        if(defeat() == 1):
            os.system('clear')
            game_over()

            print()

            print(Fore.MAGENTA+Style.BRIGHT +
                  "BETTER LUCK NEXT TIME!".center(SCREEN)+Style.RESET_ALL)

            quit()
        
        po.create_board()
        strik = print_header(newtime,level,tot)
        
        po.print_board(0,strik)
        # walls store
        for i in range(HT):
            for j in range(SCREEN):
                if(po.grid[i][j] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL):
                     walls.append([i,j])

        movekey()


        array_cord = cord_set()
        ar = bal_set()

        sx = []
    # loops on barbarian
        for l in range(level+1):
            cans_arr[l].attack_can(po.grid,king_body)

        # attack for barbarian
        for i in range(len(wiz_arr)):
           wiz_arr[i].attack_wiz(po.grid, king_body)


        for i in range(len(Barb_arr)):
            Barb_arr[i].move(po.grid, array_cord, attack(i))
            Barb_arr[i].color_change(po.grid)

        for i in range(len(Bal_arr)):
            for j in range(0, 3):
                wiz_arr[j].attack_wiz(po.grid, Bal_arr[i])

        for i in range(len(Bal_arr)):
            Bal_arr[i].move(po.grid, ar, balattack(i))
            Bal_arr[i].color_change(po.grid)

        for i in range(len(Arch_arr)):
            Arch_arr[i].move(po.grid, array_cord, Archattack(i))
            Arch_arr[i].color_change(po.grid)

        # Archer attck
        for i in range(len(Arch_arr)):
            for j in range(0, 3):
                cans_arr[j].attack_can(po.grid, Arch_arr[i])

        for i in range(len(Arch_arr)):
            for j in range(0, 3):
                wiz_arr[j].attack_wiz(po.grid, Arch_arr[i])

        for i in range(len(Barb_arr)):
            for j in range(0, level+1):
                cans_arr[j].attack_can(po.grid, Barb_arr[i])
            for j in range(len(wiz_arr)):
                wiz_arr[j].attack_wiz(po.grid, Barb_arr[i])

        os.system('clear')
        

if(level == 3):
    # print("LEVEL 2")
    # os.system('clear')
    reposition_cursor(0,0)
    wiz_arr.append(wiz4)
    cans_arr.append(can4)
    level_grid(3)
    while True:
        #remove cursor
        os.system('tput civis')
        # reposition_cursor(0,0)
        newtime = GAMETIME - (round(time.time()) - round(start_time))
        """  """
        # winning condition
        tot = 15
        if(obj_hall.get_destroy_flag() == True):
            tot = tot - 1
        for i in range(4):
            tot = tot - cans_arr[i].get_destroy_flag()
        for i in range(6):
            tot = tot - huts_arr[i].get_destroy_flag()
        for i in range(4):
            tot = tot - wiz_arr[i].get_destroy_flag()
        if (level == 3 and tot == 0):
            os.system('clear')
            # print("YOU WON")
            print()
            print(Fore.LIGHTGREEN_EX+Style.BRIGHT +
                  "CONGRATULATIONS!".center(SCREEN)+Style.RESET_ALL)
            # print(gridCopy)
            yay()
            time.sleep(1)

            quit()
        if(defeat() == 1):
            os.system('clear')
            game_over()

            print()

            print(Fore.MAGENTA+Style.BRIGHT +
                  "BETTER LUCK NEXT TIME!".center(SCREEN)+Style.RESET_ALL)

            quit()

        po.create_board()
        strik = print_header(newtime, level,tot)

        po.print_board(0,strik)
        # walls store
        for i in range(HT):
            for j in range(SCREEN):
                if(po.grid[i][j] == Fore.WHITE + Back.RED + Style.BRIGHT + "#" + Style.RESET_ALL):
                    walls.append([i, j])

        movekey()

        array_cord = cord_set()
        ar = bal_set()

        sx = []
    # loops on barbarian
        for l in range(level+1):
            cans_arr[l].attack_can(po.grid, king_body)

        # attack for barbarian
        for i in range(len(wiz_arr)):
          wiz_arr[i].attack_wiz(po.grid, king_body)


        for i in range(len(Barb_arr)):
            Barb_arr[i].move(po.grid, array_cord, attack(i))
            Barb_arr[i].color_change(po.grid)

        for i in range(len(Bal_arr)):
            for j in range(0, 4):
                wiz_arr[j].attack_wiz(po.grid, Bal_arr[i])

        for i in range(len(Bal_arr)):
            Bal_arr[i].move(po.grid, ar, balattack(i))
            Bal_arr[i].color_change(po.grid)

        for i in range(len(Arch_arr)):
            Arch_arr[i].move(po.grid, array_cord, Archattack(i))
            Arch_arr[i].color_change(po.grid)

        # Archer attck
        for i in range(len(Arch_arr)):
            for j in range(0, 4):
                cans_arr[j].attack_can(po.grid, Arch_arr[i])

        for i in range(len(Arch_arr)):
            for j in range(0, 4):
                wiz_arr[j].attack_wiz(po.grid, Arch_arr[i])

        for i in range(len(Barb_arr)):
            for j in range(0, level+1):
                cans_arr[j].attack_can(po.grid, Barb_arr[i])
            for j in range(len(wiz_arr)):
                wiz_arr[j].attack_wiz(po.grid, Barb_arr[i])

        os.system('clear')
