import time

class UniqueIDGenerator:
    def __init__(self):
        self.counter = 0

    def generate_id(self):
        current_time = int(time.time() * 1000)
        unique_id = int(str(current_time) + str(self.counter))
        self.counter += 1
        return unique_id

id_generator = UniqueIDGenerator()

