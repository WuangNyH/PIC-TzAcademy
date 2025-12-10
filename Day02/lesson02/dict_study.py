# student = {
#     "name": "Nguyen Van A",
#     "age": 20,
#     "city": "Danang",
# }
#
# for key in student:
#     print(key, "=>", student[key])
#
# # Lấy danh sách key
# print(student.keys())  # dict_keys(['name', 'age', 'city'])
#
# # Lấy danh sách value
# print(student.values())  # dict_values(['Nguyen Van A', 20, 'Danang'])
#
# # Lấy cặp (key, value)
# print(student.items())
# # dict_items([('name', 'Nguyen Van A'), ('age', 20), ('city', 'Danang')])
#
# # Duyệt với `items()`
# for key, value in student.items():
#     print(key, ":", value)
#
# student = {"name": "An", "age": 20}
# extra = {"age": 21, "city": "Danang"}
#
# student.update(extra)
# student.update(hobby="football")
# student.update(city="ThanhHoa")
# print(student)

students = {
    "SV01": {
        "name": "Nguyen Van A",
        "age": 20,
        "scores": [8.0, 7.5, 9.0],
    },
    "SV02": {
        "name": "Tran Thi B",
        "age": 21,
        "scores": [7.0, 8.5, 8.0],
    },
}

print(students.get("SV01").get("name"))  # Nguyen Van A
print(students.get("SV02").get("scores")[1])  # 8.5
