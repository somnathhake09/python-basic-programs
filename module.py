# #first way
# import math
# import random
# print("PI:", math.pi)
# print("Random number:", random.randint(1, 10))

# #second way
# from math import pi
# from random import randint
# print("PI:", pi)
# print("Random number:", randint(1, 10))

# #third way
# import math as m
# import random as r
# print("PI:", m.pi)
# print("Random number:", r.randint(1, 10))

# #os module
# import os
# folder = "demo"
# if not os.path.exists(folder):
#     os.makedirs(folder)
#     print(f"Folder '{folder}' created.")
# else:
#     print(f"Folder '{folder}' already exists.")

# file_path = os.path.join(folder, "example.txt")
# print(f"File path: {file_path}")

# #time module

# import time
# now = time.ctime()
# stamp = time.strftime("%Y-%m-%d %H:%M:%S")
# print("Current time:", now)
# print("Formatted time:", stamp)


# #psutil module
# import psutil
# print("CPU Usage  (%): ", psutil.cpu_percent(interval=0.2))
# memory=psutil.virtual_memory()
# print("Memory Usage (%): ", memory.percent)
# disk=psutil.disk_usage('/')
# print("Disk Usage (%): ", disk.percent)

# #sys module
# import sys
# if len(sys.argv) != 3:
#     print("Invalid arguments")
# else:
#     interval = sys.argv[1]
#     folder_name = sys.argv[2]

#     print("Interval (minutes) : ",interval)
#     print(type(int(interval)))
#     print("Folder Name : ",folder_name)



# # python commandlineargs1.py 60 log

# # argv[0] = commandlineargs1.py
# # argv[1] = 60
# # argv[2] = log

# #scheduler module

# import schedule
# import time

# def job():
#     print("Jay Ganesh : ",time.strftime("%H:%M:%S"))



# schedule.every(3).seconds.do(job)


# # s = schedule.every(3)
# # ss = s.seconds
# # d = ss.do(job)


# print("TO stop execution press ctrl + c")

# while True:
#     schedule.run_pending()
#     time.sleep(3)


#*************chatgpties code****************
import math
import random
import os
import time
import psutil
import sys
import schedule

print("PI:", math.pi)
print("Random number:", random.randint(1, 10))

folder = "demo"
if not os.path.exists(folder):
    os.makedirs(folder)
    print(f"Folder '{folder}' created.")
else:
    print(f"Folder '{folder}' already exists.")

file_path = os.path.join(folder, "example.txt")
print(f"File path: {file_path}")

now = time.ctime()
stamp = time.strftime("%Y-%m-%d %H:%M:%S")
print("Current time:", now)
print("Formatted time:", stamp)

print("CPU Usage (%):", psutil.cpu_percent(interval=0.2))
memory = psutil.virtual_memory()
print("Memory Usage (%):", memory.percent)

disk = psutil.disk_usage('C:\\')   # ✅ fixed
print("Disk Usage (%):", disk.percent)

if len(sys.argv) != 3:
    print("Invalid arguments")
else:
    interval = sys.argv[1]
    folder_name = sys.argv[2]
    print("Interval:", interval)
    print("Folder Name:", folder_name)

def job():
    print("Jay Ganesh:", time.strftime("%H:%M:%S"))

schedule.every(3).seconds.do(job)

print("Press Ctrl + C to stop")

for _ in range(5):   # ✅ avoid infinite loop for testing
    schedule.run_pending()
    time.sleep(3)