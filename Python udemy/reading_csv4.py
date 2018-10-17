#using reader
from csv import reader
with open("address.csv") as f:
	csv_reader=reader(f)
	data=list(csv_reader)
	print(data)