
'''
x = {
    "name" : "batuhan",
    "age": 27,
    "city": "poznan"
}
print(x)


import json 

data = {
    "name": "batuhan",
    "surname": "talisca",
    "age":   27,
    "city": "poznan", 
    "hobbies": ["football", "mma", "box", "adam dovme"] 
}

json_string = json.dumps(data, indent=4)
print("JSON STRING:")
print(json_string)

parsed_data = json.loads(json_string)
print("\nParsed Data:")
print(parsed_data)

print("\nName:", parsed_data["name"])
print("Surname:", parsed_data["surname"])
print("Age:", parsed_data["age"])
print("City:", parsed_data["city"])
print("Hobbies:", parsed_data["hobbies"])
'''


import json 

data = {
    "students": [
        {
            "name": "Ali",
            "age": 20,
            "major": "Computer Science",
            "address" :{
                "street": "123 tech st.",
                "city": "Tech town", 
                "zipzode": "54321",
            }, 
            "hobbies": ["coding", "gaming"]
        },
    ]
}

json_string = json.dumps(data, indent=4)

print("JSON STRING:")
print(json_string)

parsed_data = json.loads(json_string)

print("\nStudent Information:")
for student in parsed_data["students"]:
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Major:", student["major"])
    print("Address:", student["address"]["street"], student["address"]["city"], student["address"]["zipzode"])
    print("Hobbies:", ", ".join(student["hobbies"]))
    print()





import json
university = {
    "name": "State University",
    "established": 1850,
    "departments": [
        {
            "name": "Computer Science",
            "faculty": 50,
            "courses": [
                {"courseName": "Algorithms", "courseCode": "CS101", "credits": 4},
                {"courseName": "Data Structures", "courseCode": "CS102", "credits": 4}
            ]
        },
        {
            "name": "Mathematics",
            "faculty": 40,
            "courses": [
                {"courseName": "Calculus", "courseCode": "MATH101", "credits": 4},
                {"courseName": "Linear Algebra", "courseCode": "MATH102", "credits": 4}
            ]
        }
    ],
    "library": {
        "name": "Main Library",
        "books": 100000,
        "journals": 5000,
        "digitalResources": {
            "ebooks": 20000,
            "databases": 50
        }
    },
    "sportsFacilities": [
        {"facilityName": "Football Stadium", "capacity": 30000},
        {"facilityName": "Basketball Arena", "capacity": 10000}
    ]
}
university_json = json.dumps(university, indent=4)
print("JSON string:\n", university_json)

parsed_university = json.loads(university_json)
print("\nParsed JSON back to dictionary:\n", parsed_university)
