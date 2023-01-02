# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import logging
import sys
from typing import Any, List

from util.gc_setup import gc_set_threshold

if sys.version_info < (3, 8):  # pragma: no cover
    sys.exit("Freqtrade requires Python version >= 3.8")

logger = logging.getLogger('tradinngbot')

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
