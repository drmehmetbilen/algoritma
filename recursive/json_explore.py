import json

student = {
    "name":"Mehmet",
    "sur_name":"Bilen",
    "number":"1923",
    "lectures":["Algorithm","Maths","Physics"],
    "city":"Isparta"
}
with open("student.json","w") as f:
    json.dump(student,f)