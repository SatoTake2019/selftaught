
import statistics
import random

list1 = []

for i in range(0, 10):
    list1.append(random.random())

print(statistics.stdev(list1))
