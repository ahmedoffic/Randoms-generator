import hardware
class Simple:
    def __ini__(self):pass
    def mouse_inputs(self):pass
    def cpu_temp(self):return hardware.Cpu.temp()

simpleR = Simple()
print(simpleR.cpu_temp)