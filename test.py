from Reader import Reader
from Country import DataType

path = "https://api.covid19api.com/"

r = Reader(path)

print(r.get_top("NewConfirmed", 3))
print(r.data_for_graph("poland", DataType.DEATHS))
print(r.data_for_graph("poland", DataType.NEW_DEATHS))
