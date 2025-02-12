import pyautogui
import psutil
import os 
import sys

class Cpu:
    def sysCalls(self):return psutil.cpu_stats().syscalls
    def systemTimes(self):return psutil.cpu_count()
    def count(self):return psutil.cpu_count()
    def count(self):return len(str((psutil.cpu_times().system)))-1

class SYS:
    def time(self):
        boot_time = str(psutil.boot_time()).split('.')
        sysTime = int(f"{boot_time[0]}{boot_time[1]}")
        return sysTime
    def disckIOCounters(self):return psutil.disk_io_counters(True)['PhysicalDrive0'].write_bytes

class Ram:
    def __init__(self):self.virtual_ram = psutil.virtual_memory()
    def totalRam(self):return self.virtual_ram.total
    def avaiable(self):return self.virtual_ram.available
    def used(self):return self.virtual_ram.used
    def percent(self):return self.virtual_ram.percent * 10
class Mouse:
    def location(self):x,y=pyautogui.position();return x*y

if __name__ == "__main__":
    # script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    # print("boot_time : ",str(psutil.boot_time()).split('.'))
    # print("cpu_count",psutil.cpu_count())
    # print("cpu_stats",psutil.cpu_stats().syscalls)
    # # print("net_connections",psutil.net_connections())
    # print("cpu_times",len(str((psutil.cpu_times().system)))-1)
    # print("disk_io_counters",psutil.disk_io_counters(True)['PhysicalDrive0'].write_bytes)
    # print("Mouse Location :",Mouse().location())
    # boot_time = str(psutil.boot_time()).split('.')
    # sysTime = int(f"{boot_time[0]}{boot_time[1]}")
    # print(sysTime)
    # try:
    #     ram_info = psutil.virtual_memory()
    #     print(f"Total: {ram_info.total} GB")
    #     print(f"Available: {ram_info.available} GB")
    #     print(f"Used: {ram_info.used} GB")
    #     print(f"Percentage usage: {int(ram_info.percent*10)}%")
    # except FileNotFoundError:
    #     print("Ram info not available on this system")
    # try:
    #     cpu_percent = psutil.cpu_percent()
    #     print(f"Percentage usage: {cpu_percent}%")
        
    #     # CPU frequency
    #     cpu_info = psutil.cpu_freq()
    #     print(f"Current frequency: {cpu_info.current:.2f} Mhz")
    #     print(f"Minimum frequency: {cpu_info.min:.2f} Mhz")
    #     print(f"Maximum frequency: {cpu_info.max:.2f} Mhz")
    #     print(f"Current frequency: {psutil.cpu_freq().current:.2f} ")
    
    # except FileNotFoundError:
    #     print("CPU info not available on this system")
    pass