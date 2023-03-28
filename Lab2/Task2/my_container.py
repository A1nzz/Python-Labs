import re
import json
import os


class MyContainer:
    def __init__(self, username):
        self.username = username
        self.storage = set()
        self.switch(username)

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
                print(f"{key}")
                is_something_match = True
        if not is_something_match:
            print("No such elements")

    def save(self):
        os.makedirs(os.path.dirname(f'./containers/{self.username}.json'), exist_ok=True)
        with open(f'./containers/{self.username}.json', 'w') as fp:
            json.dump(list(self.storage), fp)

    def load(self):
        if os.path.exists(f'./containers/{self.username}.json'):
            with open(f'./containers/{self.username}.json', 'r') as fp:
                self.storage.update(set(json.load(fp)))
        else:
            print(f"There is no such user! Created new container for user {self.username}")

    def switch(self, username):
        self.username = username
        self.storage.clear()
        if os.path.exists(f'./containers/{self.username}.json'):
            answer = input("Do you want to load the container?(y,n): ")
            if answer.lower() == "y":
                self.load()
        else:
            print(f"Created new container for user {self.username}")
