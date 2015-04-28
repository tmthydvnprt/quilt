"""
quilt cli

command-line tool for quilt.py
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from quilt.QuiltingRoom import QuiltingRoom

#@profile
def main(args):
    """run when called from cli"""
    if len(args) > 1:
        room = QuiltingRoom(*args[1:])
        room.quilt()

if __name__ == "__main__":
    main(sys.argv)

