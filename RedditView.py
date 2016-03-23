import curses
from keyCodes import *


# This class defines the main terminal screen
class RedditView(object):
    """docstring for MainWindow"""

    # Initialize main terminal window
    def __init__(self):
        self.code = KeyCodes()
        self.currentInput = 0
        self.tempCursorPos = 0
        self.window = curses.initscr()
        # self.post =
        self.window.hline(self.window.getmaxyx()[0] - 2, 0,
                          curses.ACS_HLINE, self.window.getmaxyx()[1] - 1)
        self.window.move(self.window.getbegyx()[0], self.window.getbegyx()[1])
        self.window.keypad(True)
        self.window.attroff(curses.A_NORMAL)
        curses.curs_set(0)
        curses.noecho()
        curses.cbreak()
        curses.halfdelay(20)

    # Method to destroy main window
    def terminateWindow(self):
        self.window.clear()
        curses.nocbreak()
        self.window.keypad(False)
        curses.echo()
        curses.endwin()
        exit()

    # Method to create the left subreddit bar view
    def loadSubReddits(self, feed):
        self.sub = SubRedditView(self.window, feed)
        self.sub.populate()

    # Method to go to command mode
    def commandWindow(self):
        self.tempCursorPos = self.window.getyx()
        self.window.move(self.window.getmaxyx()[0] - 1, 0)
        self.window.addch(':')
        curses.echo()

    # Method to choose how enter key works
    def enter(self):
        if self.window.getyx()[0] == self.window.getmaxyx()[0] - 1:
            self.window.move(self.window.getyx()[0], 0)
            self.window.clrtoeol()
            self.window.move(self.tempCursorPos[0], self.tempCursorPos[1])
        self.window.move(self.window.getyx()[0] + 1, 0)

    # Method to get input from keyboard
    def getInput(self):
        return self.window.getch()

    # Method to update left sidebar current highlight
    def update(self):
        self.sub.update()

    # Method to move cursor on screen
    def move(self, direction):
        self.sub.move(direction)

    ###########################################################################
    ##### Methods to control cursor direction using h,j,k,l or arrow keys #####
    ###########################################################################
    def moveLeft(self):
        currentPosition = self.window.getyx()
        LEFT_BOUNDS = 0
        if currentPosition[1] == LEFT_BOUNDS:
            return

        self.window.move(self.window.getyx()[0], self.window.getyx()[1] - 1)

    def moveRight(self):
        currentPosition = self.window.getyx()
        RIGHT_BOUNDS = self.window.getmaxyx()[1]
        if currentPosition[1] == RIGHT_BOUNDS:
            return

        self.window.move(self.window.getyx()[0], self.window.getyx()[1] + 1)

    def moveUp(self):
        currentPosition = self.window.getyx()
        UPPER_BOUNDS = 0
        if currentPosition[0] == UPPER_BOUNDS:
            return

        self.window.move(self.window.getyx()[0] - 1, self.window.getyx()[1])

    def moveDown(self):
        currentPosition = self.window.getyx()
        BOTTOM_BOUNDS = self.window.getmaxyx()[0] - 3
        if currentPosition[0] == BOTTOM_BOUNDS:
            return

        self.window.move(self.window.getyx()[0] + 1, self.window.getyx()[1])
    ##########################################################################
    ##########################################################################


# This defines the left sidebar view of subreddits which is inside the Main
# Window
class SubRedditView(RedditView):
    """docstring for SubRedditView"""

    # Initialize left sidebar with vertical/horizontal lines, header
    def __init__(self, win, feed):
        self.code = KeyCodes()
        self.dict = {'-1': 'SubReddits'}
        self.submissions = feed
        self.window = win
        self.LEFT_BOUNDS = 0
        self.RIGHT_BOUNDS = self.getRightBounds() + 2
        self.TOP_BOUNDS = 0
        self.BOTTOM_BOUNDS = self.window.getmaxyx()[0] - 2
        self.BEGINNING = 2
        self.size = len(feed)
        self.window.vline(0, self.RIGHT_BOUNDS,
                          curses.ACS_VLINE, self.BOTTOM_BOUNDS)

    # Populates left sidebar with subreddit lists from the reddit bot
    def populate(self):
        self.window.addstr(0, 0, "SubReddits")
        self.window.hline(1, 0, curses.ACS_HLINE, self.RIGHT_BOUNDS)
        STARTING_POS = 2
        for sub in self.submissions:
            self.window.addstr(STARTING_POS, 0, sub)
            self.dict[STARTING_POS] = sub
            STARTING_POS += 1
        self.window.move(self.BEGINNING, 0)
        self.setCurrentCursor()

    # Helper method to get the subreddit from the indexing system
    # This is used as a means of highlighting current subreddit cursor position
    def getSubRedditAtIndex(self, index):
        if index in self.dict:
            return self.dict[index]
        return 0

    # Sets the subreddit to be highlighted when cursor is at its location
    def setCurrentCursor(self):
        sub = self.getSubRedditAtIndex(self.window.getyx()[0])
        if sub == 0:
            return
        length = len(str(sub))
        self.window.chgat(self.window.getyx()[0], 0, length, curses.A_STANDOUT)

    # This method resets the previous highlighted subreddit so the new cursor
    # position can highlight its current location
    def updateReset(self):
        sub = self.getSubRedditAtIndex(self.window.getyx()[0])
        if sub == 0:
            return
        length = len(str(sub))
        self.window.chgat(self.window.getyx()[0], 0, length, curses.A_NORMAL)

    # This method updates current cursor location
    def update(self):
        self.setCurrentCursor()

    # Move only up and down
    # TODO: Implement right arrow key to move to post view (middle screen)
    def move(self, direction):
        # if direction == curses.KEY_LEFT or direction == self.code.MOVE_LEFT:
            # self.moveLeft()
        # if direction == curses.KEY_RIGHT or direction == self.code.MOVE_RIGHT:
            # self.moveRight()
        if direction == curses.KEY_UP or direction == self.code.MOVE_UP:
            self.updateReset()
            self.moveUp()
            self.update()
        if direction == curses.KEY_DOWN or direction == self.code.MOVE_DOWN:
            self.updateReset()
            self.moveDown()
            self.update()

    # This defines the right boundaries of the left sidebar view
    def getRightBounds(self):
        limit = 0
        for sub in self.submissions:
            if len(sub) > limit:
                limit = len(sub)
        return limit
