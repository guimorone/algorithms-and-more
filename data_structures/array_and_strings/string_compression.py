def solution_1(string: str) -> str:
    # Worst Case -> Time: O(n + n²) (Due to string concatenation with '+='), Space: O(n)
    # To improve, it is probably better to use an alternative to '+=' concatenation, like ''.join(...)
    compressed_string = ''
    last_char = ''
    count_last = 0
    for c in string:
        print(count_last)
        if c != last_char:
            if last_char and count_last > 0:
                compressed_string += f'{last_char}{count_last}'
            last_char = c
            count_last = 1
        else:
            count_last += 1
    # for the last group
    if last_char and count_last > 0:
        compressed_string += f'{last_char}{count_last}'

    return compressed_string if len(compressed_string) < len(string) else string


def solution_2(string: str) -> str:
    # Worst Case -> Time: O(n + n) (Due to string concatenation with 'join'), Space: O(n)
    compressed_string = ''
    last_char = ''
    count_last = 0
    for c in string:
        if c != last_char:
            if last_char and count_last > 0:
                compressed_string = ''.join([compressed_string, last_char, str(count_last)])
            last_char = c
            count_last = 1
        else:
            count_last += 1
    # for the last group
    if last_char and count_last > 0:
        compressed_string += f'{last_char}{count_last}'

    return compressed_string if len(compressed_string) < len(string) else string


if __name__ == '__main__':
    string = input().strip()
    result_1 = solution_1(string)
    print(result_1)
    result_2 = solution_2(string)
    print(result_2)
