import re


class MyContainer:
    def __init__(self, username):
        self.username == username
        self.storage = set()

    def add(self, key):
        if key not in self.storage:
            self.storage.add(key)

    def remove(self, key):
        if key in self.storage:
            self.storage.remove(key)

    def find(self, key):
        if key in self.storage:
            print(f"{key}")
            return True
        else:
            print("No such elements")
            return False

    def list(self):
        for key in self.storage:
            print(f'{key}')

    def grep(self, regex):
        is_something_match = False
        for key in self.storage:
            if re.match(regex, key):
                print("key")
                is_something_match = True
        if is_something_match:
            print("No such elements")

    def save(self, filename: str):


    def load(self, filename: str):

