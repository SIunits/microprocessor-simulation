# utility script for generating samples
import random
from main import *

OPS = ['add', 'mul', 'gt', 'or', 'nand', 'min', 'shift'] 

def randop():
    return random.choice(OPS)

def a():
    return random.randint(-100, 200)

def b():
    return random.randint(0, 40)

def line():
    return f"{randop()} {a()} {b()}"

def gen_sample():
    print("---sample---")
    lines = []
    for i in range(random.randint(3, 30)):
        l = line()
        lines.append(l)
        print(l)
    print("---solution---")
    for l in lines:
        process(l)

gen_sample()
