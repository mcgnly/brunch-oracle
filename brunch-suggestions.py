import json
from random import randint

lines = open('bahn.txt').read().splitlines()
value = randint(0, len(lines))
print(lines[value])