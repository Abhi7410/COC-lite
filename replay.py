import os
import sys

from headers import reposition_cursor

def Replay(file_name):
    with open(file_name,'r') as f:
        all_lines = f.readlines()
        frame = []
        check = 0
        for line in all_lines:
            frame.append(line)
            check += 1
            # os.system('clear')
            if check%40== 0 :
                # reposition_cursor(0,0)
                os.system('clear')
                print(''.join(frame))
                os.system('sleep 0.2')
                frame = []

replay_no = input("Enter replay file number: ")
Replay(f'replays/{replay_no}.txt')
