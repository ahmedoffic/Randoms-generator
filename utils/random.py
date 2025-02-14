from . import hardware

class Simple:
    def __init__(self,GEN=True,Range=1):
        self.GEN = GEN
        self.Range = Range
        if self.GEN:self.value = self.Generate()
    # def cpu_temp(self):return hardware.Cpu.temp()
    def type(self):
        print("TYPE: hardware.SYS().disckIOCounters() ",type(hardware.SYS().disckIOCounters()))
    def Generate(self):
        self.cpu_syscalls = hardware.Cpu().sysCalls()
        self.diskIo = hardware.SYS().disckIOCounters()
        self.ram_used = hardware.Ram().used()
        self.internet = hardware.Internet().port()
        self.eq = (self.cpu_syscalls * self.diskIo % self.ram_used)/(self.internet)
        return hardware.TestRandom().batteryConnection()

if __name__ == "__main__":
    print(Simple().Generate())