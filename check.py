import sys
import termios
import tty
import signal




ff = open(f'replays/{sys.argv[1]}', "r")
lines = ff.readlines()
for i in range(1,len(lines)):
    print(lines[i])

print(lines[0])
