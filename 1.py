import json

max_count = 0
max_group = 0

with open('group_people.json') as file:
    data = json.load(file)

for elem in data:
    id = elem["id_group"]
    count = 0
    for people in elem["people"]:
        if people["gender"] == 'Female' and people["year"] > 1977:
            count += 1
    if count > max_count:
        max_count = count
        max_group = id

print(f'{max_group} {max_count}')