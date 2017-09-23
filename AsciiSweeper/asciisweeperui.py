import sys
import curses
import pexpect

size = 0
diff = 0
cursor_pos = [1, 1]

def init(stdscr):
    #Ground colour
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    global size
    global cursor_pos
    stdscr.border()
    child = pexpect.spawn("python asciisweeper.py " + str(size) + " " + str(diff))
    child.expect("Generated new board")
    for line in child:
        stdscr.addstr(line)
    stdscr.move(cursor_pos[0], cursor_pos[1])
    stdscr.refresh()
    update(stdscr.getch(), stdscr)
def update(input, stdscr):
    if (input == 27):
        exit()
    elif (input == 259):
        cursor_pos[0] -= 1
        stdscr.move(cursor_pos[0], cursor_pos[1])
    elif (input == 258):
        cursor_pos[0] += 1
        stdscr.move(cursor_pos[0], cursor_pos[1])
    elif (input == 260):
        cursor_pos[1] -= 1
        stdscr.move(cursor_pos[0], cursor_pos[1])
    elif (input == 261):
        cursor_pos[1] += 1
        stdscr.move(cursor_pos[0], cursor_pos[1])
    update(stdscr.getch(), stdscr)
    
  
if (len(sys.argv) != 3):
    print ("Incorrect arguments")
    print ("First arg is size, second is difficulty")
    exit()
size = int(sys.argv[1])
diff = int(sys.argv[2])
curses.wrapper(init)