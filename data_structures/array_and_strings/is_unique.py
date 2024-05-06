from implementations.hash_table import HashTable

def solution(string: str) -> bool:
    hash_table = HashTable()
    for char in string:
        if hash_table.search(char):
            return False
        
        hash_table.insert(char)
    return True

if __name__ == '__main__':
    string = input() 
    is_unique = solution(string)
    print(f'String chars are{' not ' if not is_unique else ' '}unique')
