#create one json file and dump the data into the file of one employee
employee = {
    "firstName": "Lisa",
    "lastName": "Manoban",
    "birthDate": "1997/03/27",
    "role": "Tester",
    "country": "Thailand",
    "currentProject": "International Bank",
    "pastProjects": [
        {
            "project": "ABC Enterprise",
            "year": 2012
        },
        {
            "project": "J&J Incorporated",
            "year": 2009
        }
    ],
    "employeeId": "EMP9202380"
}

import json
with open("Employee.json", "w+")  as write_file:
    json.dump(employee, write_file)
    print(employee)