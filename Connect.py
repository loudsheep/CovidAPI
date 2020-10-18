import requests


class Connect:
    def __init__(self, path):
        self.path = path
        self.connection = requests.get(path)

    def get_data(self):
        return self.connection.json()
