# x = (5)  # KHÔNG phải tuple, chỉ là số 5
# x_tuple = (5,)  # Đây mới là tuple 1 phần tử
#
# print(type(x))  # <class 'int'>
# print(type(x_tuple))  # <class 'tuple'>

# nums = (1, 2, 3)
# nums[1] = 100

students = {}

key1 = ("Nguyen", "An")
key2 = ("Tran", "Binh")

students[key1] = 8.5
students[key2] = 9.0

print(students[("Nguyen", "An")])
