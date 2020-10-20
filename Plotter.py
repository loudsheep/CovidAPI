import matplotlib.pyplot as plt


class Scatter:
    def __init__(self, values, ylabel, title):
        self.values = values
        self.range = list(range(len(values)))
        self.ylabel = ylabel
        self.title = title

    def plot(self):
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        ax.scatter(self.range, self.values, color='r', s=1)
        ax.set_xlabel('Days')
        ax.set_ylabel(self.ylabel)
        ax.set_title(self.title)
        plt.ylim(0, self.values[-1])
        plt.show()


class Pie:
    def __init__(self, values, labels, title):
        self.style = "fivethirtyeight"
        self.values = values
        self.labels = labels
        self.explode = [0 for i in range(len(values))]
        self.title = title

    def plot(self):
        plt.style.use(self.style)

        plt.pie(self.values, labels=self.labels, explode=self.explode, shadow=True,
                startangle=90, autopct='%1.1f%%',
                wedgeprops={'edgecolor': 'black'})

        plt.title(self.title)
        plt.tight_layout()

        plt.show()


class Column:
    pass