#using reader
from csv import reader
with open("address.csv") as f:
	csv_reader=reader(f)
	for row in csv_reader:
		#each row is a list
		print(row)