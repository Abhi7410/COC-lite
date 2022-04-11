from headers import *
from person import *


class Din(Person):

    #Attributes inherited from Person class

    #personal attributes for din
    def __init__(self, x_cood, y_cood):
        self.__body = np.array(['K'])  # 3x3 matrix
        self.__body_fly = np.array([[" ", " ", "O", " ", " "], [
                                   "{", "|", " ", "|", "}"], [" ", "/", " ", "\\", " "]])
        self.__body_shield = np.array([["-", "-", "-", "-", "-", "-", "-"], ["|", " ", " ", "O", " ", " ", "|"], [
                                      "|", " ", "{", "|", "}", " ", "|"], ["|", " ", "/", " ", "\\", " ", "|"], ["-", "-", "-", "-", "-", "-", "-"]])
        self.__body_s = [[Fore.LIGHTCYAN_EX+" "+Style.RESET_ALL, Fore.LIGHTCYAN_EX+"O"+Style.RESET_ALL, Fore.LIGHTCYAN_EX+" "+Style.RESET_ALL], [Fore.LIGHTCYAN_EX +
                                                                                                                                                 "{"+Style.RESET_ALL, Fore.LIGHTCYAN_EX+"|"+Style.RESET_ALL, Fore.LIGHTCYAN_EX+"}"+Style.RESET_ALL], [Fore.LIGHTCYAN_EX+"/"+Style.RESET_ALL, Fore.LIGHTCYAN_EX+" "+Style.RESET_ALL, Fore.LIGHTCYAN_EX+"\\"+Style.RESET_ALL]]
        self.__lives = 150
        self.__damage = 53
        self.__speed = 1
        self.__mode = 0
        self.__destroy_flag = 0
        self.__attack_time = 0

        Person.__init__(self, x_cood, y_cood)
    def set_attack_time(self,x):
        self.__attack_time = x

    def get_attack_time(self):
        return self.__attack_time
    def show_body(self):
        return self.__body[0][0]

    def change_body(self,ch):
        ar = np.array([ch])
        self.__body = ar
   
    def set_damage_value(self,x):
        self.__damage = x

    def show_damage_value(self):
        return self.__damage
    def set_destroy_flag(self):
        self.__destroy_flag = 1
    def get_destroy_flag(self):
        return self.__destroy_flag
    def set_mode(self, x):
        self.__mode = x

    def show_mode(self):
        return self.__mode

    def show_lives(self):
        return self.__lives

    def get_speed(self):
        return self.__speed
    
    def set_speed(self):
        self.__speed = 2*self.__speed
        
    def set_lives(self, x):
        self.__lives = x


    #Function to place din correctly in the beginning
    def start_pos(self, grid):
        grid[self.gety()][self.getx()] = " "
        self.setx(4);
        self.sety(4);
        x = self.getx()
        y = self.gety()

        for i in range(x, x+1):
            for j in range(y,y+1):
                grid[i][j] = self.__body[i-x][j-y]

    def new_din(self, grid):
        # grid[self.getx()][self.gety()] = " "
        self.sety(self.gety())
        self.setx(self.getx())
        self.set_lives(self.show_lives()+2)
        self.din_show(grid, self.getx(), self.gety(), self.show_mode())

    # #Clearing the position of din as he moves

    def din_clear(self, grid):
        x = self.getx()
        y = self.gety()
        # print(x)
        
        grid[y][x]= " "
    #New position of din as he moves
    def din_show(self, grid, x, y, mode):
         self.din_clear(grid)
       
         self.setx(x)
         self.sety(y)
        #  if(self.show_shield_flag() == 0):
         for i in range(y, y+1):
            for j in range(x, x+1):
                grid[i][j] = self.__body[0][0]

            # if mode == 0:
    



