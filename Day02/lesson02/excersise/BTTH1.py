scores = [7.5, 8.0, 6.5, 9.0, 8.5]


def self_loop(sc: list[float]) -> tuple[float, float, float]:
    total = 0
    minimum = sc[0]
    maximum = sc[0]
    for i in sc:
        total += i

        if i < minimum:
            minimum = i

        if i > maximum:
            maximum = i

    average = total / len(sc)

    return average, minimum, maximum


def use_built_in(sc: list[float]) -> tuple[float, float, float]:
    average = sum(sc) / len(sc)
    minimum = min(sc)
    maximum = max(sc)
    return average, minimum, maximum


if __name__ == "__main__":
    avg1, min1, max1 = self_loop(scores)
    print(f"Self Loop -> Average: {avg1:.1f}, Min: {min1:.1f}, Max: {max1:.1f}")

    avg2, min2, max2 = use_built_in(scores)
    print(f"Built-in -> Average: {avg2:.1f}, Min: {min2:.1f}, Max: {max2:.1f}")
