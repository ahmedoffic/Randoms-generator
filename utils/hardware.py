import pyautogui
class Cpu:
    def __init__(self):
        pass
    def sysCalls(self):return psutil.cpu_stats().syscalls
class SYS:
    def time(self):pass
    def storage(self):pass
class Mouse:
    def location(self):x,y=pyautogui.position();return x*y

import psutil
import os 
import sys 
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

print("boot_time : ",str(psutil.boot_time()).split('.'))
print("cpu_count",psutil.cpu_count())
print("cpu_stats",psutil.cpu_stats())
# print("net_connections",psutil.net_connections())
print("cpu_times",psutil.cpu_times())
print("disk_io_counters",psutil.disk_io_counters(True)['PhysicalDrive0'].write_bytes)