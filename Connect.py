import requests


class Connect:
    def __init__(self, path):
        self.path = path
        self.connection = requests.get(path)

    def status_code(self):
        return self.connection.status_code

    def get_data_json(self):
        return self.connection.json()

    def get_data_original(self):
        return self.connection
