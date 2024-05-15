class LocalRemoteMapper:
    def __init__(self, local=None, remote=None):
        self.local = local
        self.remote = remote
    
    def get_local(self):
        return self.local
    
    def set_local(self, local):
        self.local = local
    
    def get_remote(self):
        return self.remote
    
    def set_remote(self, remote):
        self.remote = remote
    
    def __str__(self):
        return f"{self.local} : {self.remote}"