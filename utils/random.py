from . import hardware
class Simple:
    def __init__(self,GEN=True,Range=range(0,1)):
        self.GEN = GEN
        self.Range = Range
        if self.GEN:self.value = self.Generate()
    def mouse_inputs(self):return hardware.Mouse().location()
    # def cpu_temp(self):return hardware.Cpu.temp()
    def type(self):
        print("TYPE: hardware.SYS().disckIOCounters() ",type(hardware.SYS().disckIOCounters()))
    def Generate(self):
        self.seed = hardware.SYS().disckIOCounters()
        self.x = hardware.SYS().time() / ((1/3)*(hardware.SYS().time()))
        self.y = hardware.Cpu().sysCalls()
        self._eq = self.seed * ((self.x / self.mouse_inputs() )*self.y)*hardware.Cpu().count()
        return self._eq