import curses

def key(stdscr):
    char = stdscr.getch()
    if (char == 27):
        #exit when esc is pressed
        exit()
    print(char)
    key(stdscr)
curses.wrapper(key)

#Up = 259
#Down = 258
#Left = 260
#Right = 261
#Space = 32
#Enter = 10
#Escape = 27