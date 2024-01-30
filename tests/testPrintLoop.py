import unittest
from unittest.mock import patch
import json
from contextlib import redirect_stdout
import io
import re

with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
for i in code:
    for j in i['source']:
        if "#si-print-loop" in j:
            print(i['source'])
            f = io.StringIO()
            with redirect_stdout(f):
                exec("".join(i['source']))
            s = f.getvalue()

class testCases(unittest.TestCase):
    def testPrintLoop(self):
        self.assertTrue(s=='A\nLong\nTime\nAgo\nIn\nA\nGalaxy\nFar\nFar\nAway\n', "Did you print the whole loop?")

