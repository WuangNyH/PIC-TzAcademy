# with open("data/data.txt", "r", encoding="utf-8") as f:
#     content = f.read()
# print(content)

# with open("data/data.txt", "r", encoding="utf-8") as f:
#     line1 = f.readline()
#     line2 = f.readline()
#     line3 = f.readline().strip()
#     line4 = f.readline().strip()
#
# print(line1)
# print(line2)
# print(line3)
# print(line4)

# with open("data/data.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#
# for line in lines:
#     print(line.strip())

# with open("output.txt", "w", encoding="utf-8") as f:
#     f.write("Xin chào Python!\n")
#     f.write("Dòng thứ hai\n")

# with open("output.txt", "a", encoding="utf-8") as f:
#     f.write("Dòng mới được thêm vào\n")

# lines = ["Hello", "Python", "File I/O"]
# with open("list.txt", "w", encoding="utf-8") as f:
#     for line in lines:
#         f.write(line + "\n")

# with open("list.txt", "w", encoding="utf-8") as f:
#     lines = ["Xin chào Python!\n", "Dòng thứ hai\n"]
#     f.writelines(lines)

try:
    with open("abc.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("Không tìm thấy file!")
