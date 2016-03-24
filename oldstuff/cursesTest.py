import curses


# class KeyCodes(object):
#     """docstring for KeyCodes"""
#     EXIT_CODE = 113
#     COMMAND_CODE = 58
#     ENTER_CODE = 10

#     def __init__(self):


# Init window
window = curses.initscr()
window.hline(window.getmaxyx()[0] - 2, 0, '-', window.getmaxyx()[1] - 1)
window.move(window.getbegyx()[0], window.getbegyx()[1])
window.keypad(True)
# window.attron(curses.A_REVERSE) #HIGHLIGHT MODE
# window.attron(curses.A_STANDOUT) #HIGHLIGHTMODE too
curses.noecho()
curses.cbreak()
input = 0
savedPos = 0
EXIT_CODE = 113
COMMAND_CODE = 58
ENTER_CODE = 10

# Start input reading
while (input != EXIT_CODE):  # Checks if input is q
    input = window.getch()
    # print window.getmaxyx(),
    # print input,

    if input == ENTER_CODE:
        if window.getyx()[0] == window.getmaxyx()[0] - 1:
            window.move(window.getyx()[0], 0)
            window.clrtoeol()
            window.move(savedPos[0], savedPos[1])
            pass
        window.move(window.getyx()[0] + 1, 0)

    if input == COMMAND_CODE:
        savedPos = window.getyx()
        window.move(window.getmaxyx()[0] - 1, 0)
        window.addch(':')
        curses.echo()

    # MAKE SURE IT DOESNT GO OUT OF BOUNDS
    if input == curses.KEY_RIGHT:
        window.move(window.getyx()[0], window.getyx()[1] + 1)
    if input == curses.KEY_LEFT:
        window.move(window.getyx()[0], window.getyx()[1] - 1)
    if input == curses.KEY_UP:
        window.move(window.getyx()[0] - 1, window.getyx()[1])
    if input == curses.KEY_DOWN:
        window.move(window.getyx()[0] + 1, window.getyx()[1])
# Terminate window
window.clear()
curses.nocbreak()
window.keypad(False)
curses.echo()
curses.endwin()
