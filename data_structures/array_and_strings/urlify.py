def solution(string: str, true_length: int) -> str:
    string = string[:true_length] + '\0'
    return string.replace(' ', '%20')


if __name__ == '__main__':
    string, true_length = input(), int(input())
    url = solution(string, true_length)
    print(url)
