# Runtime dependes on "isSubstring" function


def solution_1(s1: str, s2: str) -> bool:
    # If s2 is a rotation of s1
    # Worst Case -> Time: O(n + n²) (In case of substring function "s2 in s1". Actually n * m, but n == m), Space: O(1)
    size_s1 = len(s1)
    size_s2 = len(s2)
    if size_s1 != size_s2:
        return False

    total, count, index = 0, 0, 0
    while index < size_s2:
        if s2[total : index + 1] in s1:
            count += 1
            index += 1
        else:
            if count > 0:
                total += count
            count = 0
    total += count

    return total == size_s1


def solution_2(s1: str, s2: str) -> bool:
    # If s2 is a rotation of s1
    # Worst Case -> Time: O(n²) (In case of substring function "s2 in s1". Actually n * m, but n == m), Space: O(1)
    size_s1 = len(s1)
    size_s2 = len(s2)
    if size_s1 != size_s2:
        return False

    return s1 in s2 * 2


if __name__ == '__main__':
    s1, s2 = input().strip(), input().strip()
    print(solution_1(s1, s2))
    print(solution_2(s1, s2))
