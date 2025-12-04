from BE import BE
from Deploy import Deploy
from FE import FE
from Testing import Testing

class Total:
    def __init__(self):
        self.backend = BE()
        self.frontend = FE()
        self.deployment = Deploy()
        self.tester = Testing()

    def implement(self):
        self.backend.code()
        self.frontend.design()
        self.deployment.server()
        self.tester.checking()
    
    