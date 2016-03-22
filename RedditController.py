import curses
from keyCodes import *


class RedditController(object):
    """docstring for RedditController"""

    def __init__(self, view, bot):
        self.redditBot = bot
        self.screen = view
        self.screen.loadSubReddits(self.redditBot.favoriteSubReddits)
        self.code = KeyCodes()

    def processInput(self, command):
        # print command,
        if command == self.code.EXIT_CODE:
            self.screen.terminateWindow()
        if command == self.code.COMMAND_CODE:
            self.screen.commandWindow()
        if command == self.code.ENTER_CODE:
            self.screen.enter()
        if command in self.code.MOVEMENT:
            self.screen.move(command)
            self.screen.setCurrent
