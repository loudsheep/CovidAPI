class Top:
    def __init__(self, data, key):
        self.data = data
        self.key = key

    def get(self, num):
        data = sorted(self.data["Countries"], key=lambda x: x[self.key], reverse=True)

        return data[:num]