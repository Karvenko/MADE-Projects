roman_dict = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

def roman_to_int(roman):
    """Converts number in roman string to int. No any checks - hope numbers are correct :)"""
    result = 0
    idx = 0
    str_len = len(roman)
    while idx < str_len:
        if idx == str_len-1 or roman_dict[roman[idx]] >= roman_dict[roman[idx+1]]: #handling last char 
            result += roman_dict[roman[idx]]
            idx += 1
        else:
            result += roman_dict[roman[idx+1]] - roman_dict[roman[idx]]
            idx += 2
            
    return result

def king_sort(kings):
    """Takes list of kings and sort it"""
    king_list = []
    for cur in kings:
        king_list.append(cur.split())
        king_list[-1].append(roman_to_int(king_list[-1][1]))
        
    king_list = sorted(king_list, key=lambda x: x[2])#Sort by number
    king_list = sorted(king_list, key=lambda x: x[0])#Sort by name
    
    kings = [king[0]+' '+king[1] for king in king_list]
    return kings

if __name__ == '__main__':
    t = int(input())
    
    kings = []
    for _ in range(t):
        kings.append(input())
        
    kings = king_sort(kings)
    for king in kings:
        print(king)