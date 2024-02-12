def solution(my_string, is_suffix):
    a = []
    for i in range(len(my_string)):
        a.append(my_string[i:])
    return 1 if is_suffix in a else 0