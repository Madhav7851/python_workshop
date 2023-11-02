student={
    "name":"madhav",
    "age":18,
    "grade":"A"
}

name=student["name"]
age=student["age"]
student["age"]=19
student["city"]="kanpur"
print(student)

for key,value in student.items():
    print(f"{key}:{value}")
if "age" in student:
    print("Age exist in the dictionary")

student["favorite food"]="garlic bread"
print(student)



dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)
