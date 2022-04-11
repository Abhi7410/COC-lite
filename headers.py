# from getch import _getChUnix as getChar
# from alarmexception import AlarmException
import random
import time
import numpy as np
import signal
import os
import sys
from colorama import init, Fore, Back, Style
from getch import _getChUnix as getChar
import math

init()

HT = 40
SCREEN = 200
WIDTH = 500
GAMETIME = 100
STARTPOS = 25
GRAVITYVAL = 1
BEAM_SIZE = 20
INPUT_CHAR = ''
FIGHT_START = 0
factor = 0
NUMCOINS = 100
gridCopy = []
walls = []
Barb_arr = []
bal_walls = []
Arch_arr = []

listname = os.listdir("replays")  # dir is your directory path
number_files = len(listname)
print(number_files)

# f = open(f'replays/' + str(number_files+1)+'.txt', "a")
file_name = f'replays/{number_files+1}.txt'


for i in range(HT):
    gridCopy.append([' ']*SCREEN)


def reposition_cursor(x, y):
    print("\033[%d;%dH" % (x, y))

class Background:

    #constructor function
    def __init__(self):
        self.__ceil = Fore.BLACK + Back.LIGHTYELLOW_EX + Style.BRIGHT + \
            "_" + Style.RESET_ALL  # Private variables to ensure security
        self.__floor = Fore.WHITE + Back.MAGENTA + Style.BRIGHT + "/" + Style.RESET_ALL
        self.__middle = Fore.BLACK + Back.LIGHTYELLOW_EX + \
            Style.BRIGHT + "="+Style.RESET_ALL
        self.__side = Fore.BLACK + Back.LIGHTYELLOW_EX + \
            Style.BRIGHT + "|"+Style.RESET_ALL

    #function to create the floor
    def display_floor(self, boundary):
        for i in range(WIDTH-1):
            boundary[HT-1][i] = self.__floor
            boundary[HT-2][i] = self.__middle

    #function to create the ceil
    def display_ceil(self, boundary):
        for i in range(WIDTH-1):
            boundary[0][i] = self.__ceil
            boundary[1][i] = self.__middle

    def display_side(self, boundary):
        for i in range(HT):
            boundary[i][0] = self.__side
            boundary[i][1] = self.__side
            boundary[i][199] = self.__side
            boundary[i][198] = self.__side

    def spawningpoint(self, boundary):
        boundary[9][198] = Fore.LIGHTYELLOW_EX + "P" + Style.RESET_ALL
        boundary[15][1] = Fore.LIGHTYELLOW_EX + "I" + Style.RESET_ALL
        boundary[1][100] = Fore.LIGHTYELLOW_EX + "N" + Style.RESET_ALL

    def spawningballon(self,boundary):
        boundary[20][198] = Fore.LIGHTYELLOW_EX + "H" + Style.RESET_ALL
        boundary[38][30] = Fore.LIGHTYELLOW_EX + "U" + Style.RESET_ALL
        boundary[1][21] = Fore.LIGHTYELLOW_EX + "J" + Style.RESET_ALL
     
    def spawningqueen(self,boundary):
        boundary[23][1] = Fore.LIGHTYELLOW_EX + "K" + Style.RESET_ALL
        boundary[38][80] = Fore.LIGHTYELLOW_EX + "M" + Style.RESET_ALL
        boundary[1][140] = Fore.LIGHTYELLOW_EX + "L" + Style.RESET_ALL
        



def clear_copy(ch):
    for i in range(HT):
        for j in range(SCREEN):
            if(gridCopy[i][j] == ch):
                gridCopy[i][j] = " "
    







def game_over():
    os.system('aplay -q ./sounds/game_over.wav&')

    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + 
      "░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
      "██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
      "██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
      "██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
      "╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
      "░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝".center(SCREEN)+Style.RESET_ALL)



def yay():
    os.system('aplay -q ./sounds/win.wav&')
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
          "██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗░█████╗░███╗░░██╗".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
        "╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██╔══██╗████╗░██║".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
        "░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║░░██║██╔██╗██║".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
        "░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║░░██║██║╚████║".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
        "░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░╚█████╔╝██║░╚███║".center(SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
        "░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚══╝".center(SCREEN) + Style.RESET_ALL)
    
