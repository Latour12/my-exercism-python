import string
import random

class Robot():
    def __init__(self):
        self.used_names = set()
        self.reset()

    def generate_name(self):
        while True:
            random_name = self.generator(2, string.ascii_uppercase) + str(self.generator(3, string.digits))
            if random_name not in self.used_names:
                return random_name

    def generator(self, size, chars):
        return ''.join(random.choice(chars) for _ in range(size))

    def reset(self):
        self.name = self.generate_name()
        self.used_names.add(self.name)