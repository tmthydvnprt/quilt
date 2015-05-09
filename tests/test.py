"""
generate documentation quilt nose tests

project    : quilt
version    : 0.1.0
status     : development
modifydate : 2015-05-09 08:51:00 -0700
createdate : 2015-04-28 07:23:00 -0700
website    : https://github.com/tmthydvnprt/quilt
author     : tmthydvnprt
email      : tmthydvnprt@users.noreply.github.com
maintainer : tmthydvnprt
license    : MIT
copyright  : Copyright 2015, quilt
credits    :

"""

# test dependancies
import os
import unittest

# testing dependancies
from quilt.QuiltingRoom import QuiltingRoom

# test inputs
CURRENT_PATH = os.path.dirname(__file__)
SOURCE_PATH = os.path.join(CURRENT_PATH, 'source')
OUTPUT_PATH = os.path.join(CURRENT_PATH, 'output')

# test cases
class GenerateSite(unittest.TestCase):
    """test by generating quilt site"""

    def test1(self):
        """generate site"""

        room = QuiltingRoom(SOURCE_PATH, OUTPUT_PATH)
        status = room.quilt()

        self.assertEqual(status, False)
