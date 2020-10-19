class Day:
    def __init__(self, line):
        self.line = line
        self.country = line['Country']
        self.confirmed = line['Confirmed']
        self.deaths = line['Deaths']
        self.recovered = line['Recovered']
        self.active = line['Active']
        self.date = line['Date']

    def __str__(self):
        return "Country: " + self.country + " Confirmed: " + str(self.confirmed) + " Deaths: " + str(self.deaths)

    def __repr__(self):
        return self.__str__()


class Country:
    def __init__(self, data):
        self.data = data
        self.days = []

        for i in range(len(data)):
            self.days.append(Day(data[i]))

    def get_max_new_confirmed(self):
        max_diff = -1
        for i in range(1, len(self.days)):
            diff = int(self.days[i].confirmed) - int(self.days[i - 1].confirmed)
            if diff > max_diff:
                max_diff = diff
        return max_diff

    def get_avg_new_confirmed(self):
        s = 0
        for i in range(1, len(self.days)):
            diff = int(self.days[i].confirmed) - int(self.days[i - 1].confirmed)
            s += diff

        return s / len(self.days)

    def __str__(self):
        return str([x.__str__() for x in self.days])

    def __repr__(self):
        return str([x.country + " " + x.date for x in self.days])
