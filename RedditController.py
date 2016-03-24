import curses
from keyCodes import *


class RedditController(object):
    """docstring for RedditController"""

    def __init__(self, view, bot):
        self.redditBot = bot
        self.screen = view
        self.screen.loadSubReddits(self.redditBot.favoriteSubReddits)
        self.screen.loadPosts(self.redditBot.getSubmissions(
            self.screen.window.getyx()[0], 35))
        self.screen.window.move(2, 0)
        self.code = KeyCodes()

    def processInput(self, command):
        if command == self.code.EXIT_CODE:
            self.screen.terminateWindow()
        if command == self.code.COMMAND_CODE:
            self.screen.commandWindow()
        if command == self.code.ENTER_CODE:
            self.screen.enter()
        if command in self.code.MOVEMENT:
            self.screen.move(command)
            self.screen.reloadPosts(self.redditBot.getSubmissions(
                self.screen.window.getyx()[0], 35))
            # self.redditBot.updateSubmissionCursor()
            # self.screen.loadPosts(self.redditBot.getSubmissions(
            # self.screen.window.getyx()[0] - 2, 30))
