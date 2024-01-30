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
        if "#si-decibel" in j:
            print(i['source'])
            f = io.StringIO()
            with redirect_stdout(f):
                exec("".join(i['source']))
            s = f.getvalue()

class testCases(unittest.TestCase):
    
    # input will return '112' during this test
    @patch('builtins.input', return_value='112')
    def testSoundLevel(self, input):
        self.assertTrue(bool(re.search('[Jj]ackhammer', s)) & bool(re.search('[Ll]awnmower', s)), "The test value is between two sounds. Make sure you're describing that!")