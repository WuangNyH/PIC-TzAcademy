# BTTH6: In các hình sau
# Hình a
row, col = 5, 6
print("6a. Hình chữ nhật rỗng")
for i in range(row):
    for j in range(col):
        if i == 0 or i == row - 1 or j == 0 or j == col - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()

# Hình b
height = 5
print("6b. Hình tam giác vuông cân")
for i in range(height):
    for j in range(i + 1):
        print("*", end=" ")
    print()
   