import curses
from RedditView import *
from RedditController import *
from Pyeddit import *


class RedditMain(object):
    """docstring for RedditMain"""

    def __init__(self):
        self.bot = RedditPrawler()
        self.view = RedditView()
        self.controller = RedditController(self.view, self.bot)

    def begin(self):
        while (1):
            self.controller.processInput(self.view.getInput())


test = RedditMain()
test.begin()
