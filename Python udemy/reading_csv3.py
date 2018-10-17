#using reader
from csv import reader
with open("address.csv") as f:
	csv_reader=reader(f)
	next(csv_reader)   #to avoid the header
	for nm in csv_reader:
		print(f"{nm[0]} is from {nm[2]} ")
		#each row is a list
		# print(row)