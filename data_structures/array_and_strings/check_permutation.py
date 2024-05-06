from implementations.hash_table import HashTable

def solution_1(string_1: str, string_2: str) -> bool:
    # Worst Case -> Time: O(n), Space: O(n)
    hash_table_1 = HashTable()
    hash_table_2 = HashTable()
    for c1 in string_1:
        hash_table_1.insert(c1)
    for c2 in string_2:
        hash_table_2.insert(c2)
        
    for c1 in string_1:
        if hash_table_1.count(c1) != hash_table_2.count(c1):
            return False
            
    return True

def solution_2(string_1: str, string_2: str) -> bool:
    # Worst Case -> Time: O(n * log(n)), Space: O(n) | Based on mergesort
    # Worst Case -> Time: O(n²), Space: O(log(n)) | Based on quicksort
    string_1 = sorted(string_1)
    string_2 = sorted(string_2)
            
    return string_1 == string_2
    


if __name__ == '__main__':
    string_1, string_2 = input().strip().lower(), input().strip().lower()
    check_permutation_1 = solution_1(string_1, string_2)
    print(f'The string are{' NOT ' if not check_permutation_1 else ' '}a permutation of each other')
    check_permutation_2 = solution_2(string_1, string_2)
    print(f'The string are{' NOT ' if not check_permutation_2 else ' '}a permutation of each other')
