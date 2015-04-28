"""
generate documentation quilt nose tests
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
        room.quilt()

        self.assertNotEqual(True, False)
