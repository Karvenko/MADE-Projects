"""Task C solution"""

NUM_COUNTERS = 128 #number of counters to use for sorting

def digi_sort(strings, number):
    """counter sorting strings by position number"""
    char_counter = [0] * NUM_COUNTERS
    pointers = [0] * NUM_COUNTERS
    output_array = [0] * len(strings)

    num_round = len(strings[0]) - number - 1

    for string in strings:
        char_counter[ord(string[num_round])] += 1

    for i in range(1, NUM_COUNTERS - 1):
        pointers[i + 1] = pointers[i] + char_counter[i]

    for string in strings:
        idx = ord(string[num_round])
        output_array[pointers[idx]] = string
        pointers[idx] += 1

    return output_array

def batch_digi_sort(strings, number):
    """Making several digi_sort"""
    for i in range(number):
        strings = digi_sort(strings, i)

    return strings

if __name__ == '__main__':
    strings = []
    string_number, _, round_count = map(int, input().split())

    for _ in range(string_number):
        strings.append(input())

    strings = batch_digi_sort(strings, round_count)
    for string in strings:
        print(string)
