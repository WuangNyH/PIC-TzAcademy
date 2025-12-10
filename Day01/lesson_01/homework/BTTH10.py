# BTTH10: Kiểm tra chuỗi đối xứng
def is_palindrome(s: str) -> bool:
    return s == s[::-1]


string = input("Nhập chuỗi: ")
if is_palindrome(string):
    print(f'"{string}" là chuỗi đối xứng.')
else:
    print(f'"{string}" không phải là chuỗi đối xứng.')
