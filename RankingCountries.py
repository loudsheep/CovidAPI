class RankingCountries:
    def __init__(self, data):
        self.data = data
        # json.dump(data, sort_keys=False, fp=self.data)
        self.country = self.data['Country']
        self.country_code = self.data['CountryCode']
        self.slug = self.data['Slug']
        self.new_confirmed = self.data['NewConfirmed']
        self.total_confirmed = self.data['TotalConfirmed']
        self.new_deaths = self.data['NewDeaths']
        self.total_deaths = self.data['TotalDeaths']
        self.date = self.data['Date']

    def __str__(self):
        return "Country: " + self.country + ", New Confirmed: " + str(self.new_confirmed) + ", New Deaths: " + str(
            self.new_deaths) + ", Date: " + str(self.date) + "\n"

    def __repr__(self):
        return "Country & new confirmed: " + self.country + " - " + str(self.new_confirmed)

    def get_country(self):
        return self.country

    def get_new_confirmed(self):
        return self.new_confirmed

    def get_country_code(self):
        return self.country_code

    def get_slug(self):
        return self.slug

    def get_total_confirmed(self):
        return self.total_confirmed

    def get_new_deaths(self):
        return self.new_deaths

    def get_total_deaths(self):
        return self.total_deaths

    def get_date(self):
        return self.date
