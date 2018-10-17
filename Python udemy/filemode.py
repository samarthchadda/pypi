with open("haiku.txt","r+") as file:
	file.write("Hello")
	file.seek(10)
	file.write("Manu")
	
	