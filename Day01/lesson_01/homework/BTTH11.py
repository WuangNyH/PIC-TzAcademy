# BTTH11: Đếm số lượng nguyên âm trong chuỗi
def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


string = input("Nhập chuỗi: ")
vowel_count = count_vowels(string)
print(f'Số lượng nguyên âm trong chuỗi là: {vowel_count}')
