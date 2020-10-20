from RankingCountries import RankingCountries


class Top:
    def __init__(self, data, key):
        self.data = data
        self.key = key

    def get(self, num):
        data = sorted(self.data["Countries"], key=lambda x: x[self.key], reverse=True)

        countries = []
        if num == "ALL":
            for i in data:
                countries.append(RankingCountries(i))
        else:
            for i in range(num):
                countries.append(RankingCountries(data[i]))

        return countries
