from sshkeyboard import listen_keyboard, stop_listening

from tests.basics.basics_001 import test_basics
from utils.monitor import Monitor


class StartCommand:
    pass


def press(key):
    if key == "q":
        stop_listening()
    if key == "r":
        Monitor().show(test_basics(), "No hints", 2, 10)


if __name__=="__main__":
    Monitor().show(test_basics(), "No hints", 2, 10)
    listen_keyboard(on_press=press)
