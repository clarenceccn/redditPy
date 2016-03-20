import curses
from RedditView import *
# import RedditPrawler
from RedditController import *


class RedditMain(object):
    """docstring for RedditMain"""

    def __init__(self):
        self.view = RedditView()
        self.controller = RedditController(self.view)
        # self.bot = RedditPrawler()

    def begin(self):
        while (1):
            self.controller.processInput(self.view.getInput())


test = RedditMain()
test.begin()
