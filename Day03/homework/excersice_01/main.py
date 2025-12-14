from homework.excersice_01.file_utils import read_file_content, count_word_frequency

if __name__ == "__main__":
    filename = input("Nhập tên file cần phân tích: ")

    content = read_file_content(filename)

    if content is not None:
        frequency = count_word_frequency(content)

        print("Tổng số từ: ", sum(frequency.values()))
        print("Top 10 từ phổ biến nhất:")

        top_10_words = sorted(
            frequency.items(), key=lambda item: item[1], reverse=True
        )[:10]

        for word, count in top_10_words:
            print(f"- {word}: {count}")
