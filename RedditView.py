import curses


class RedditView(object):
    """docstring for MainWindow"""

    def __init__(self):
        self.currentInput = 0
        self.tempCursorPos = 0
        self.window = curses.initscr()
        self.window.hline(self.window.getmaxyx()[0] - 2, 0,
                          '-', self.window.getmaxyx()[1] - 1)
        self.window.move(self.window.getbegyx()[0], self.window.getbegyx()[1])
        self.window.keypad(True)
        curses.noecho()
        curses.cbreak()

    def terminateWindow(self):
        self.window.clear()
        curses.nocbreak()
        self.window.keypad(False)
        curses.echo()
        curses.endwin()
        exit()

    def commandWindow(self):
        self.tempCursorPos = self.window.getyx()
        self.window.move(self.window.getmaxyx()[0] - 1, 0)
        self.window.addch(':')
        curses.echo()

    def enter(self):
        if self.window.getyx()[0] == self.window.getmaxyx()[0] - 1:
            self.window.move(self.window.getyx()[0], 0)
            self.window.clrtoeol()
            self.window.move(self.tempCursorPos[0], self.tempCursorPos[1])
        self.window.move(self.window.getyx()[0] + 1, 0)

    def getInput(self):
        return self.window.getch()
