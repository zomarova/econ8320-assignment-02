import unittest
import json

with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-fours" in j:
            exec("".join(i['source']))


class testCases(unittest.TestCase):
    def testFours(self):
        truth = [i for i in range(1000) if '4' in str(i)]
        self.assertTrue(truth==sorted(fours), "Your list is either missing some numbers with 4 in them, or has too many numbers.")