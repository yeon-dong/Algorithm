def solution(numbers, target):
    leaves = [0]
    count = 0
    
    for n in numbers:
        temp = []
        for leaf in leaves:
            temp.append(leaf + n)
            temp.append(leaf - n)
        leaves = temp
    for leaf in leaves : 
        if leaf == target :
            count += 1
    return count