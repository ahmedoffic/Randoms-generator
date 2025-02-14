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
class Battery:
    def percent(self):percent,secLeft,powerPlugged = psutil.sensors_battery();return percent * secLeft
class Internet:
    def port(self):
        self.connections = psutil.net_connections("inet")
        for conn in self.connections:
            self.local_port = conn.laddr.port
            self.local_pid = conn.pid
        return self.local_pid*self.local_port
class Mouse:
    def location(self):x,y=pyautogui.position();return x*y
    def mouseClick(self):pyautogui.click(200,800)
class TestRandom:
    def batteryConnection(self):return Battery().percent()*Internet().port()
if __name__ == "__main__":
    print("BC",TestRandom().batteryConnection())