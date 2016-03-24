class KeyCodes(object):
    """docstring for KeyCodes"""
    EXIT_CODE = 113  # q
    COMMAND_CODE = 58  # :
    ENTER_CODE = 10  # enter key
    MOVE_LEFT = 104  # h key left
    MOVE_DOWN = 106  # j key down
    MOVE_UP = 107  # k key up
    MOVE_RIGHT = 108  # l key right

    MOVEMENT = [260, 261, 258, 259, 106, 107, 108, 104]

    def __init__(self):
        self.create = True


# TODO: Refactor all boundary settings in here
class Settings(object):
    """docstring for Settings"""

    SUBREDDIT_BOUNDS = [0]
    POST_BOUNDS = []
    COMMENT_BOUNDS = []

    def __init__(self, win):
        self.window = win
        self.params = self.window.getmaxyx()
