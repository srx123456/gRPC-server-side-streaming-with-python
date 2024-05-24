class SorMsg:
    def __init__(self, cpu, mem, sendbw, recvbw):
        self.sendbw = sendbw
        self.recvbw = recvbw
        self.mem = mem
        self.cpu = cpu
    
    def getSendBw(self):
        return self.sendbw
    def getRecvBw(self):
        return self.recvbw
    def getMem(self):
       return self.mem
    def getCpu(self):
        return self.cpu
    def setSendBw(self, sendbw):
        self.sendbw = sendbw
    def setRecvBw(self, recvbw):
        self.recvbw = recvbw
    def setMem(self, mem):
        self.mem = mem
    def setCpu(self, cpu):
        self.cpu = cpu

    def __str__(self):
        return f"CPU:{self.cpu},Mem:{self.mem},SendBw:{self.sendbw},RecvBw:{self.recvbw}"