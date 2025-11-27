from Singleton import ISingleton

class Singleton_application(ISingleton):
    def __init__(self, name):
        self.name = name
        self.logger = ISingleton()

    def process_name(self):
        self.logger.log(f"Processing {self.name}")
        return "[LOGS] {self.name}"