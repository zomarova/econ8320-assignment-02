import unittest
import json

with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-prime" in j:
            exec("".join(i['source']))


class testCases(unittest.TestCase):
    def test99(self):
        self.assertTrue(not isPrime(99) & isPrime(97), "Does your function provide the correct output for 97 and 99?")