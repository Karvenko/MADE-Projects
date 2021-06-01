"""TAsk D solution"""

def anagram_count(child_array, gr_array):
    """Anagram counter"""
    counter = 0

    child_counter = [0] * 128
    #counting child's chars
    for ch in child_array:
        child_counter[ord(ch)] += 1

    for i, ch in enumerate(child_counter): #filling with negative
        if ch == 0:
            child_counter[i] = -100

    #Iterating over substrings in gr_array
    i = 0
    j = 0
    while j < len(gr_array):
        if child_counter[ord(gr_array[j])] > 0: #can increase len
            child_counter[ord(gr_array[j])] -= 1
            j += 1
        else:
            counter += j - i
            if child_counter[ord(gr_array[i])] >= 0:
                child_counter[ord(gr_array[i])] += 1
            if i == j:
                j += 1
            i += 1

    #Adding trailing substrings
    tmp_n = j - i
    counter += tmp_n * (tmp_n + 1) // 2

    return counter

if __name__ == '__main__':
    not_used = input() #number of characters - not used in python

    gr_array = input()
    child_array = input()

    ana_count = anagram_count(child_array, gr_array)
    print(ana_count)
