def solution(s):
    if len(s) != 6 and len(s) != 4:
        return False
    for i in s:
        if i not in ["0","1","2","3","4","5","6","7","8","9"]:
            return False
    return True