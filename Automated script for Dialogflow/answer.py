import csv
import uuid
import json


def write_file(name, result):
    f = open(name + ".json", "w")
    f.write(json.dumps(result, indent=2))
    f.close()


def initialiseResult():
    return {
        "priority": 500000,
        "webhookUsed": False,
        "webhookForSlotFilling": False,
        "fallbackIntent": False,
        "events": [],
        "id": str(uuid.uuid4()),
        "auto": True,
        "contexts": [],
        "responses": {
            "resetContexts": False,
            "affectedContexts": [],
            "parameters": [],
            "defaultResponsePlatforms": {},
            "speech": []
        },
        "name": "",
        "responses": [
            {
                "resetContexts": False,
                "affectedContexts": [],
                "parameters": [],
                "defaultResponsePlatforms": {},
                "speech": [],
                "messages": []
            }
        ]
    }


with open("test.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    result = initialiseResult()
    name = ""

    for row in csv_reader:
        if row[1] != "":
            if result["name"] != "":
                write_file(name, result)
                result = initialiseResult()

            name = str(row[1]).lower()

            result["name"] = name
            result["responses"][0]["messages"].append({
                "type": 0,
                "platform": "facebook",
                "lang": "en",
                # check
                "speech": row[3]
            })
            result["responses"][0]["messages"].append({
                "type": 0,
                "lang": "en",
                "speech": row[3]
            })
        else:
            result["responses"][0]["messages"].append({
                "type": 0,
                "platform": "facebook",
                "lang": "en",
                "speech": row[3]
            })

    if len(result) != 0:
        write_file(name, result)
