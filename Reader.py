from Connect import Connect
from Top import Top


class Reader:
    def __init__(self, path):
        self.path = path
        self.connection = Connect(path)

    def get_top(self, key, num):
        self.connection = Connect(self.path + "summary")
        top = Top(self.connection.get_data(), key)

        return top.get(num)
