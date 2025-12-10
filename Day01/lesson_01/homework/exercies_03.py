def normalize_sentence(s: str) -> str:
    s = s.strip()

    while s.endswith('.'):
        s = s[:-1]
    s = s.strip()

    s = s.lower()

    words = s.split()
    s = " ".join(words)

    if len(s) > 0:
        s = s[0].upper() + s[1:]

    s = s + "."

    return s


inp = "Hello worlD, this Is python.. "
print(normalize_sentence(inp))
