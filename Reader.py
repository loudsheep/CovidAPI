from Connect import Connect
from Top import Top
from Country import Country


class Reader:
    def __init__(self, path):
        self.path = path
        self.connection = Connect(path)

    def get_top(self, key, num):
        self.connection = Connect(self.path + "summary")
        if self.connection.status_code() == 200:
            top = Top(self.connection.get_data_json(), key)

            return top.get(num)

    def get_country(self, name):
        self.connection = Connect(self.path + "dayone/country/" + name)
        if self.connection.status_code() == 200:
            country = Country(self.connection.get_data_json())

            return country
