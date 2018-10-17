from csv import reader,writer
with open("address.csv") as file:
	csv_reader=reader(file)
	address=[[s.upper() for s in row] for row in csv_reader]    #list comprehension
	for row in address:
		print(row)


with open("scream_address.csv","w") as file:
	csv_writer=writer(file)
	for addr in address:
		csv_writer.writerow(addr)