from Reader import Reader

path = "https://api.covid19api.com/"

r = Reader(path)

print(r.get_top("NewConfirmed", 3))
print(r.get_country("poland").get_avg_new_confirmed())
