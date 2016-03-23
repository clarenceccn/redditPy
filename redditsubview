import curses


class SubRedditView(RedditView):
    """docstring for SubRedditView"""

    def __init__(self, win, feed):
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

    def getSubRedditAtIndex(self, index):
        if index in self.dict:
            return self.dict[index]
        return 0

    def setCurrentCursor(self):
        sub = self.getSubRedditAtIndex(self.window.getyx()[0])
        if sub == 0:
            return
        length = len(str(sub))
        self.window.chgat(self.window.getyx()[0], 0, length, curses.A_STANDOUT)

    def updateReset(self):
        sub = self.getSubRedditAtIndex(self.window.getyx()[0])
        if sub == 0:
            return
        length = len(str(sub))
        self.window.chgat(self.window.getyx()[0], 0, length, curses.A_NORMAL)

    def update(self):
        self.setCurrentCursor()

    def move(self, direction):
        if direction == curses.KEY_LEFT or direction == self.code.MOVE_LEFT:
            self.moveLeft()
        if direction == curses.KEY_RIGHT or direction == self.code.MOVE_RIGHT:
            self.moveRight()
        if direction == curses.KEY_UP or direction == self.code.MOVE_UP:
            self.sub.updateReset()
            self.moveUp()
            self.sub.update()
        if direction == curses.KEY_DOWN or direction == self.code.MOVE_DOWN:
            self.sub.updateReset()
            self.moveDown()
            self.sub.update()

    def getRightBounds(self):
        limit = 0
        for sub in self.submissions:
            if len(sub) > limit:
                limit = len(sub)
        return limit
