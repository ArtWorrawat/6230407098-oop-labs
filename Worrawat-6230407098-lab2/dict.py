directory = {"Jane Doe":"+27 555 5367", "John Smith":"+27 555 6254", "Bob Stone":"+27 555 5689"}
directory["Jane Doe"] = "+27 555 1024"
directory["Anna Cooper"] = "+27 555 3237"
print(directory["Bob Stone"])
print(directory.get("Bob Stone"))
print(directory.keys())
print(directory.values())
