import unittest
import json

with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-fibonacci" in j:
            exec("".join(i['source']))


class testCases(unittest.TestCase):

    def testFib5(self):       
        self.assertEqual(fib(5), 5, "Your function does not correctly calculate Fibonacci(5)")

    def testFib10(self):       
        self.assertEqual(fib(10), 55, "Your function does not correctly calculate Fibonacci(10)")