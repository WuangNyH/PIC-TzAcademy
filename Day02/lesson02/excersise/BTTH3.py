def flatten_list(nested_list: list) -> list:
    flat_list = [y for x in nested_list for y in x]
    return flat_list


if __name__ == "__main__":
    nested_list = [[1, 2, 3], [4, 5], [6]]
    result = flatten_list(nested_list)
    print("Flattened list:", result)
