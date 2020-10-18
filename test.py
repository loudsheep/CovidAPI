from Reader import Reader

path = "https://api.covid19api.com/"

r = Reader(path)

print(r.get_top("NewConfirmed", 10))