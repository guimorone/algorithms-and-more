from implementations.hash_table import HashTable

def solution_1(string: str) -> bool:
    # Worst Case -> Time: O(n), Space: O(n)
    hash_table = HashTable()
    for char in string:
        if hash_table.search(char):
            return False
        
        hash_table.insert(char)

    return True

def solution_2(string: str) -> bool:
    # Worst Case -> Time: O(n²), Space: O(1)
    for i in range(len(string)):
        for j in range(len(string)):
            if i == j:
                continue
            
            if string[i] == string[j]:
                return False

    return True


if __name__ == '__main__':
    string = input() 
    is_unique_1 = solution_1(string)
    print(f'String chars are{' not ' if not is_unique_1 else ' '}unique')
    is_unique_2 = solution_2(string)
    print(f'String chars are{' not ' if not is_unique_2 else ' '}unique')
