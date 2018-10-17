#using DictReader
from csv import DictReader
with open("address.csv") as f:
	csv_reader=DictReader(f)
	for row in csv_reader:
		#print(f"{nm[0]} is from {nm[2]} ")
		#each row is an OrderedDict(dictionary that has order to it)
		print(row['Fname'])
		# print(row)