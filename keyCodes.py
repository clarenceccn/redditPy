class KeyCodes(object):
    """docstring for KeyCodes"""
    EXIT_CODE = 113  # q
    COMMAND_CODE = 58  # :
    ENTER_CODE = 10  # enter key
    MOVE_LEFT = 260
    MOVE_RIGHT = 261
    MOVE_UP = 259
    MOVE_DOWN = 258

    MOVEMENT = [260, 261, 258, 259]

    def __init__(self):
        self.create = True
