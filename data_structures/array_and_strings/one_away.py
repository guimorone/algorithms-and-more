# assuming case sensitive
import string
from typing import Literal


def solution_1(s1: str, s2: str) -> bool:
    # Worst Case -> Time: O(n), Space: O(1)
    if s1 == s2:
        return True

    size_1 = len(s1)
    size_2 = len(s2)

    def check_insert(n: Literal[1, 2]) -> bool:
        s = s1 if n == 1 else s2
        s_to_compare = s2 if n == 1 else s1
        size = size_1 if n == 1 else size_2
        for letter in string.ascii_letters:
            for i in range(size):
                if s[:i] + letter + s[i + 1 :] == s_to_compare:
                    return True

        return False

    def check_remove(n: Literal[1, 2]) -> bool:
        s = s1 if n == 1 else s2
        s_to_compare = s2 if n == 1 else s1
        size = size_1 if n == 1 else size_2
        for i in range(size):
            if s[:i] + s[i + 1 :] == s_to_compare:
                return True

        return False

    def check_replace() -> bool:
        if size_1 != size_2:
            return False

        for letter in string.ascii_letters:
            for i in range(size_1):
                if s1[:i] + letter + s1[i + 1 :] == s2 or s2[:i] + letter + s2[i + 1 :] == s1:
                    return True

        return False

    if abs(size_1 - size_2) > 1:
        return False

    if size_1 > size_2:
        return check_insert(2) or check_remove(1)
    elif size_1 < size_2:
        return check_insert(1) or check_remove(2)

    return check_replace()


def solution_2(s1: str, s2: str) -> bool:
    # With only remove and replace (do not need insert -> same as remove from the other string)
    if s1 == s2:
        return True

    size_1 = len(s1)
    size_2 = len(s2)

    def check_remove(n: Literal[1, 2]) -> bool:
        s = s1 if n == 1 else s2
        s_to_compare = s2 if n == 1 else s1
        size = size_1 if n == 1 else size_2
        for i in range(size):
            if s[:i] + s[i + 1 :] == s_to_compare:
                return True

        return False

    def check_replace() -> bool:
        if size_1 != size_2:
            return False

        for letter in string.ascii_letters:
            for i in range(size_1):
                if s1[:i] + letter + s1[i + 1 :] == s2 or s2[:i] + letter + s2[i + 1 :] == s1:
                    return True

        return False

    if abs(size_1 - size_2) > 1:
        return False

    if size_1 > size_2:
        return check_remove(1)
    elif size_1 < size_2:
        return check_remove(2)

    return check_replace()


if __name__ == '__main__':
    s1, s2 = input().strip(), input().strip()
    print(solution_1(s1, s2))
    print(solution_2(s1, s2))
