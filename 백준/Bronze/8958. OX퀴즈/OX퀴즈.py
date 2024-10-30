n = int(input())
for _ in range(n):
    quiz = input()
    total = 0
    prev = 0
    for i in range(len(quiz)):
        if quiz[i] == 'O':
            prev += 1
            total += prev
        else:
            prev = 0
    print(total)