def count_characters(s: str) -> dict[str, int]:
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


if __name__ == "__main__":
    input_string = "hello world"
    character_counts = count_characters(input_string)
    print(f"Character counts in '{input_string}': {character_counts}")
