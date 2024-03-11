def solution(n_str):
    for i,j in enumerate(n_str):
        if j == '0' and n_str[i+1] != '0':
            a = i
            break
    return n_str[a+1:] if n_str[0] == '0' else n_str