import csv
import uuid
import json


def write_file(name, result):
    f = open(f"{name}_usersays_en.json", "w")
    f.write(json.dumps(result, indent=2))
    f.close()


with open("test.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    result = []
    name = ""

    for row in csv_reader:
        if row[1] != "":
            if len(result) != 0:
                write_file(name, result)
                result = []

            name = str(row[1]).lower()
            question = {
                "updated": 0,
                "count": 0,
                "isTemplate": 0,
                "id": str(uuid.uuid4()),
                "data": {
                    "text": row[2],
                    "userDefined": False
                }
            }
            result.append(question)
        else:
            question = {
                "updated": 0,
                "count": 0,
                "isTemplate": 0,
                "id": str(uuid.uuid4()),
                "data": {
                    "text": row[2],
                    "userDefined": False
                }
            }
            result.append(question)

    if len(result) != 0:
        write_file(name, result)
