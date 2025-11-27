class Factory_Builder:
    def __init__(self):
        self.name = None
        self. material = None
        self.cost = None
        self.level = None
    
    def __str__(self):
        return f"The factory builder {self.name}, {self.material}, {self.cost}, {self.level}"