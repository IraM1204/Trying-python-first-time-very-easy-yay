# List in Dictionary practise
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

city = travel_log["France"][2]
print(city)

#List in List practise
Nested_list = ['A', 'B', ['C', 'D']]
print(Nested_list[2][0])

#Dictionary in Dictionary practise
Im_confused = {
    "Arithmetic" : "Studied in 4th and 5th. Barely remember anything.",
    "Geometry" : "Surprisingly easy",
    "Algebra" : "THE best Maths",
}

Im_confused_again = {
    "Biology" : "Kingdom Animalia",
    "Physics" : "Hydrostatics",
    "Chemistry" : "Atomic Structure",
}

Subjects_fav_part = {
    "History" : "Independence of India",
    "Maths" : Im_confused,
    "Science" : Im_confused_again,
}

print(Subjects_fav_part["Science"]["Physics"])
print(Subjects_fav_part["Maths"]["Algebra"])
