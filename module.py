#first way
import math
import random
print("PI:", math.pi)
print("Random number:", random.randint(1, 10))

#second way
from math import pi
from random import randint
print("PI:", pi)
print("Random number:", randint(1, 10))

#third way
import math as m
import random as r
print("PI:", m.pi)
print("Random number:", r.randint(1, 10))

#os module
import os
folder = "demo"
if not os.path.exists(folder):
    os.makedirs(folder)
    print(f"Folder '{folder}' created.")
else:
    print(f"Folder '{folder}' already exists.")

file_path = os.path.join(folder, "example.txt")
print(f"File path: {file_path}")

#time module

import time
now = time.ctime()
stamp = time.strftime("%Y-%m-%d %H:%M:%S")
print("Current time:", now)
print("Formatted time:", stamp)


#psutil module
import psutil
print("CPU Usage  (%): ", psutil.cpu_percent(interval=0.2))
memory=psutil.virtual_memory()
print("Memory Usage (%): ", memory.percent)
disk=psutil.disk_usage('/')
print("Disk Usage (%): ", disk.percent)


