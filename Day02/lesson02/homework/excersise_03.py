# a. Tạo một dict user_map từ users, map user_id sang name
def create_user_map(list_users: list[tuple]) -> dict:
    user_map = {}

    for user_id, name in list_users:
        user_map[user_id] = name

    return user_map


# b. Dùng vòng lặp duyệt posts.items() để in ra:
def print_posts(dict_posts: dict, user_map: dict) -> None:
    for post_id, info in dict_posts.items():
        author_name = user_map.get(info.get("author_id"), "Unknown")
        list_tags = sorted(info.get("tags"), reverse=True)
        tags = ", ".join(list_tags)
        print(f"[{post_id}] {info['title']} - {author_name} - Tags: {tags}")


# c. Tạo một set all_tags chứa toàn bộ tag xuất hiện trong mọi bài viết
def get_all_tags(dict_posts: dict) -> set:
    all_tags = set()

    for info in dict_posts.values():
        all_tags.update(info.get("tags"))

    return all_tags


# d. Tạo một dict tag_counter để đếm số bài viết chứa mỗi tag
def count_tags(dict_posts: dict, all_tags: set) -> dict:
    tag_counter = {tag: 0 for tag in all_tags}

    for tag in all_tags:
        for info in dict_posts.values():
            if tag in info.get("tags"):
                tag_counter[tag] += 1

    return tag_counter


if __name__ == "__main__":
    # Danh sách user: list tuple (user_id, name)
    users = [
        ("U01", "Alice"),
        ("U02", "Bob"),
        ("U03", "Charlie"),
    ]

    # Dict bài viết: key là post_id, value là dict thông tin
    posts = {
        "P01": {
            "title": "Hoc Python co ban",
            "author_id": "U01",
            "tags": {"python", "beginner"},
        },
        "P02": {
            "title": "Lam viec voi List va Dict",
            "author_id": "U01",
            "tags": {"python", "data-structure"},
        },
        "P03": {
            "title": "Gioi thieu HTML CSS",
            "author_id": "U02",
            "tags": {"web", "frontend"},
        },
    }

    user_map = create_user_map(users)
    print("User Map:")
    print(user_map)

    print("\nPosts:")
    print_posts(posts, user_map)

    all_tags = get_all_tags(posts)
    print("\nAll Tags:")
    print(all_tags)

    tag_counter = count_tags(posts, all_tags)
    print("\nTag Counter:")
    print(tag_counter)
