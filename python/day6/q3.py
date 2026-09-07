#Q3 — Dictionary
#Create a student dictionary containing: name,age,course,city
#Then:Print the name. Update the age. Add a phone number. Remove the city.Print the final dictionary.

student={"name":"Priya",
         "age":22,
         "course":"MCA",
         "city":"Trichy"}
print("Name:",student["name"])
print("Age:",student["age"])
student["age"]=25
print("Updated Age:",student["age"])
student["number"]=9080706050
print("Number:",student["number"])
student.pop("city")
print(student)