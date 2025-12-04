class ISingleton:
    _instance = None

    def __new__(self, *args, **kwargs):
        if self._instance is None:
            print(f"Processing........")
            self._instance = super().__new__(self)
            self._instance.logs = []
        else:
            print (f"Existing instance!")

        return self._instance
        
    def log(self, message: str):
        self.logs.append(message)
        print(f"Was logged {message}")
    
    def show_logs(self):
        return self.logs
    