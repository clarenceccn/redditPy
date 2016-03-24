import curses
import time
from keyCodes import *


# Defines the interface of which all the views should inherit from
class ViewInterface(object):
    """docstring for ViewInterface"""

    def __init__(self):
        self.create = True

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

############################## END OF CLASS ###################################


# This class defines the main terminal screen that initializes all views
class RedditView(object):
    """docstring for MainWindow"""

    # Initialize main terminal window
    def __init__(self):
        self.code = KeyCodes()
        self.currentInput = 0
        self.tempCursorPos = 0
        self.window = curses.initscr()
        self.window.hline(self.window.getmaxyx()[0] - 2, 0,
                          curses.ACS_HLINE, self.window.getmaxyx()[1] - 1)
        self.window.move(self.window.getbegyx()[0], self.window.getbegyx()[1])
        self.window.keypad(True)
        self.window.attroff(curses.A_NORMAL)
        # curses.curs_set(0)
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
    # TODO: Fix this, create commands, and ensure that it does not echo back
    # to screen
    def commandWindow(self):
        self.tempCursorPos = self.window.getyx()
        self.window.move(self.window.getmaxyx()[0] - 1, 0)
        self.window.addch(':')
        curses.echo()

    # Method to choose how enter key works
    # TODO: Fix the situation when this is needed
    def enter(self):
        if self.window.getyx()[0] == self.window.getmaxyx()[0] - 1:
            self.window.move(self.window.getyx()[0], 0)
            self.window.clrtoeol()
            self.window.move(self.tempCursorPos[0], self.tempCursorPos[1])
        self.window.move(self.window.getyx()[0] + 1, 0)

    # Method to get input from keyboard
    def getInput(self):
        return self.window.getch()

    def loadPosts(self, feed):
        self.currPostView = PostView(
            self.window, self.sub.getRightBounds(), feed)
        self.currPostView.displayPost(feed)

    def reloadPosts(self, feed):
        self.currPostView.displayPost(feed)

    def updatePosts(self, feed):
        self.currPostView.switch(feed)

    # Method to update left sidebar current highlight
    def update(self):
        self.sub.update()

    # Method to move cursor on screen
    # TODO: check where cursor is so it calls the correct move on the certain
    # view
    def move(self, direction):
        self.sub.move(direction)

############################## END OF CLASS ###################################


# This defines the left sidebar view of subreddits which is inside the Main
# Window
class SubRedditView(ViewInterface):
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
        self.currentSubReddit = self.window.getyx()[0]
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
    # TODO: Fix that it can only go up or down while there is a dict[index] at
    # that location
    def move(self, direction):
        # if direction == curses.KEY_LEFT or direction == self.code.MOVE_LEFT:
            # self.moveLeft()
        # if direction == curses.KEY_RIGHT or direction == self.code.MOVE_RIGHT:
            # self.moveRight()
        if direction == curses.KEY_UP or direction == self.code.MOVE_UP:
            if self.boundsCheck(-1) == -1:
                return False
            self.updateReset()
            self.moveUp()
            self.update()
            return True
        if direction == curses.KEY_DOWN or direction == self.code.MOVE_DOWN:
            if self.boundsCheck(1) == -1:
                return False
            self.updateReset()
            self.moveDown()
            self.update()
            return True

    # This defines the right boundaries of the left sidebar view
    # The right boundary is the highest character count of subreddit's name
    def getRightBounds(self):
        limit = 0
        for sub in self.submissions:
            if len(sub) > limit:
                limit = len(sub)
        return limit

    # CHECK YOSELF
    def boundsCheck(self, direction):
        if self.getSubRedditAtIndex(self.window.getyx()[0] + direction) == 0:
            return -1
        return 1


############################## END OF CLASS ###################################


# TODO: Create the middle view with bounds that shows all the posts in a
# subreddit
# REQUIREMENTS: This should contain a list of subviews of each post
#               SubView: Should contain preview-image of post, along with title
class PostView(ViewInterface):
    """docstring for PostView"""

    def __init__(self, win, left, feed):
        self.LEFT_BOUNDS = left + 3
        self.window = win
        self.RIGHT_BOUNDS = left + (3 * self.window.getmaxyx()[1]) / 6
        self.BOTTOM_BOUNDS = self.window.getmaxyx()[0] - 2
        self.window.vline(0, self.RIGHT_BOUNDS,
                          curses.ACS_VLINE, self.BOTTOM_BOUNDS)
        self.window.addstr(
            0, ((self.RIGHT_BOUNDS + self.LEFT_BOUNDS) / 2) - 3, "Posts")
        self.window.hline(1, self.LEFT_BOUNDS,
                          curses.ACS_HLINE, self.RIGHT_BOUNDS - self.LEFT_BOUNDS)
        self.posts = feed
        self.currentFeed = []
        self.index = 0
        # self.getCurrentFeed(self.index)

    def getCurrentFeed(self, index):
        for post in self.posts[index]:
            self.currentFeed.append(post)
        return

    def switch(self, feed):
        self.updatePost(feed)

    def clearScreen(self):
        self.window.move(2, self.LEFT_BOUNDS)
        self.window.cleartoeol()

    def updatePost(self, feed):
        oldPos = self.window.getyx()[0]
        STARTING_POS = 2
        for post in feed:
            if STARTING_POS + 1 > self.BOTTOM_BOUNDS:
                # self.window.move(oldPos, 0)
                return
            self.window.addnstr(STARTING_POS, self.LEFT_BOUNDS,
                                post,  self.RIGHT_BOUNDS - self.LEFT_BOUNDS)
            STARTING_POS += 1

    def displayPost(self, feed):
        oldPos = self.window.getyx()[0]
        STARTING_POS = 2
        for post in feed:
            if STARTING_POS + 1 > self.BOTTOM_BOUNDS:
                self.window.move(oldPos, 0)
                return
            self.window.addnstr(STARTING_POS, self.LEFT_BOUNDS,
                                post,  self.RIGHT_BOUNDS - self.LEFT_BOUNDS)
            STARTING_POS += 1
        self.window.move(oldPos, 0)

############################## END OF CLASS ###################################


# TODO: Create the further right view that shows the post, and all the comments
# in that post
class DetailView(ViewInterface):
    """docstring for DetailView"""

    def __init__(self, arg):
        super(DetailView, self).__init__()
        self.arg = arg


############################## END OF CLASS ###################################
