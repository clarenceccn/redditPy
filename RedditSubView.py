import curses


class SubRedditView(object):
    """docstring for SubRedditView"""

    def __init__(self, win, feed):
        self.submissions = feed
        self.window = win
        self.LEFT_BOUNDS = 0
        self.RIGHT_BOUNDS = self.getRightBounds() + 2
        self.TOP_BOUNDS = 0
        self.BOTTOM_BOUNDS = self.window.getmaxyx()[0] - 2
        self.BEGINNING = 2
        self.window.vline(0, self.RIGHT_BOUNDS,
                          curses.ACS_VLINE, self.BOTTOM_BOUNDS)

    def populate(self):
        self.window.addstr(0, 0, "SubReddits")
        self.window.hline(1, 0, curses.ACS_HLINE, self.RIGHT_BOUNDS)
        STARTING_POS = 2
        for sub in self.submissions:
            self.window.addstr(STARTING_POS, 0, sub)
            STARTING_POS += 1
        self.window.move(self.BEGINNING, 0)

    def getRightBounds(self):
        limit = 0
        for sub in self.submissions:
            if len(sub) > limit:
                limit = len(sub)
        return limit
