"""
quilt cli

command-line tool for quilt.py

project    : quilt
version    : 0.1.1
status     : development
modifydate : 2015-05-13 07:09:00 -0700
createdate : 2015-04-28 06:02:00 -0700
website    : https://github.com/tmthydvnprt/quilt
author     : tmthydvnprt
email      : tmthydvnprt@users.noreply.github.com
maintainer : tmthydvnprt
license    : MIT
copyright  : Copyright 2015, quilt
credits    :

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

