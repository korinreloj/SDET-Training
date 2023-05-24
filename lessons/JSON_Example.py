json_data = {
    "firstName": "Timmy",
    "lastName": "Aguilar",
    "address": "test address",
    "city": "Princeton",
    "state": "NJ",
    "zipcode": "123",
    "nation": "USA",
    "hobbies": ["cricket", "football", "tennis"],
    "age": 29,
    "child": [
        {
            "firstName": "Kim",
            "age": 19
        },
        {
            "firstName": "Ezra",
            "age": 17
        }
    ]
}

print(json_data["hobbies"])

import json
#w+ to write and create a file
with open("TestFile2.json", "w+")  as write_file:
    json.dump(json_data, write_file)
    print(json_data["age"])
    print(json_data["child"])