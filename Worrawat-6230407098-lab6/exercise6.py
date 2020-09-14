import json
with open("hobbies.json", "r") as read_file:
    data = json.load(read_file)
    firstName = data["firstName"]
    hobbies = data["hobbies"]
    print(f"{firstName} has hobbies as ", end="")
    print(", ".join(hobbies))
    read_file.close()