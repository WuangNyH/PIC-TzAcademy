def remove_negatives(numbers: list) -> list:
    return [num for num in numbers if num >= 0]


if __name__ == "__main__":
    nums = [5, -2, 8, -1, 0, 3, -10]

    cleaned_nums = remove_negatives(nums)
    print(f"Original list: {nums}")
    print(f"List after removing negatives: {cleaned_nums}")
