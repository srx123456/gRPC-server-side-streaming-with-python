class SorMsg:
    def __init__(self, cpu, mem, bw):
        self.bw = bw
        self.mem = mem
        self.cpu = cpu
    
    def getBw(self):
        return self.bw
    def getMem(self):
       return self.mem
    def getCpu(self):
        return self.cpu
    def setBw(self, bw):
        self.bw = bw
    def setMem(self, mem):
        self.mem = mem
    def setCpu(self, cpu):
        self.cpu = cpu

    def __str__(self):
        return f"CPU:{self.cpu},Mem:{self.mem},Bw:{self.bw}"