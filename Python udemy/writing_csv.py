from csv import writer
with open("testing.csv","w") as f:
	csv_writer=writer(f)
	csv_writer.writerow(["Name","Age"])
	csv_writer.writerow(["Blue",3])
	csv_writer.writerow(["Kitty",1])
	