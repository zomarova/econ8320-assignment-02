import unittest
import json

with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-taxi" in j:
            exec("".join(i['source']))


class testCases(unittest.TestCase):

    def truth(self, distance):
        return 4+0.25*(distance*(1000/140))

    def testPricing(self):
        dist = 5
        
        self.assertEqual(round(taxiPrice(dist), 2), round(self.truth(dist), 2), "Did you remember to convert the base rate from 140m to km?")