import re


def extract_words(text: str) -> list[str]:
    lower_text = text.lower()
    punctuation_removed = re.sub(r"[.,;:?!()\[\]]", "", lower_text).strip()
    words = punctuation_removed.split()
    return words


def count_word_frequency(text: str) -> dict[str, int]:
    words = extract_words(text)
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


def read_file_content(filename: str) -> str | None:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{filename}'.")
    except Exception:
        print(f"Lỗi: Có lỗi xảy ra khi đọc file '{filename}'.")
