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

# Terminate window
window.clear()
curses.nocbreak()
window.keypad(False)
curses.echo()
curses.endwin()
