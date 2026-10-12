from operator import sub
import numpy as np

a = ("hello")  # <- a is not a tuple, but a string
b = ("hello",) # surprisingly, b is a tuple 


result = []

for i in range(2, 9, 2):
    result.append(2 ** i)


d = [1, 2, 3]
d.pop(1)

c = [1, 2, 3]
n = c[:]      # works as copy method, which means this is a shallow copy

person_infromation = {
    "name": "Roman",
    "last_name": "Nesterenko",
    "age": 19,
    "city": "Zaporizhye"
}

information = {"Roman": ["Python", "SQL"], "Veronika": ["english", "deutsch"]}
people = [information]


t = "acbed"
s = "abc"

g = t-s 
print(g)