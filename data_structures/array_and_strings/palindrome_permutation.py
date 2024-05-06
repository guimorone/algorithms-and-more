import string as s_lib
from typing import List


def is_palindrome(string: str) -> bool:
    return string == string[::-1]


def generate_perms(string: str) -> List[str]:
    if len(string) == 1:
        return [string]

    perms = [char + p for i, char in enumerate(string) for p in generate_perms(string[:i] + string[i + 1 :])]

    return perms


def solution_1(string: str) -> bool:
    # Worst Case -> Time: O(n * n!), Space: O(n!)
    perms = generate_perms(string)
    for p in perms:
        if is_palindrome(p):
            return True

    return False


def solution_2(string: str) -> bool:
    # Worst Case -> Time: O(n), Space: O(1)
    odd_found = False
    for letter in s_lib.ascii_lowercase:
        if string.count(letter) % 2 == 1:
            if odd_found:
                return False

            odd_found = True

    return True


if __name__ == '__main__':
    string = input().strip().lower().replace(' ', '')
    response_1 = solution_1(string)
    print(response_1)
    response_2 = solution_2(string)
    print(response_2)
