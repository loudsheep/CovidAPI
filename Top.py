from Country import Country


class Top:
    def __init__(self, data, key):
        self.data = data
        self.key = key

    def get(self, num):
        data = sorted(self.data["Countries"], key=lambda x: x[self.key], reverse=True)

        data2 = []
        for i in range(num) :
            data2.append(Country(data[i]))

        return data2
