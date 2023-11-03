import json

with open("dataset.json", "r") as file:
    data = json.load(file)

while True:
    inp = input("Word: ")
    if inp == "/exit":
        break
    data.append(str(inp))
    
with open("dataset.json", "w") as file:
    json.dump(data, file)