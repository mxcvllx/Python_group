import json

computers = [
    {
        "id": 1,
        "name": "Asus",
        "color": "black"
    },

    {
        "id": 2,
        "name": "Victus",
        "color": "black"
    },
    {
        "id": 3,
        "name": "HP",
        "color": "black"
    },
    {
        "id": 4,
        "name": "Lenovo",
        "color": "black"
    }
]

arr = json.dumps(computers, indent=1)

with open('computer.json', 'w') as f:
    json.dump(computers, f, indent=1)

# print(type(json.loads(arr)[0:]))
with open("computer.json") as f:
    computers = json.load(f)

print(computers)
