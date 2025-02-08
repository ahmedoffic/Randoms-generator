from . import hardware
class Simple:
    def __ini__(self):pass
    def mouse_inputs(self):return hardware.Mouse.location()
    def cpu_temp(self):return hardware.Cpu.temp()
    def Generate(self):
        return self.mouse_inputs + 1
    