import unittest
import json

with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-while-loop" in j:
            exec("".join(i['source']))


class testCases(unittest.TestCase):
    def testWhile(self):
        self.assertTrue(x==92, "Your while loop did not arrive at the correct value of 'x'.")