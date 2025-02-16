import sys

n = int(sys.stdin.readline())
words = []

for i in range(n):
    words.append(sys.stdin.readline().strip())
set_words = set(words)
words = list(set_words)
words.sort()
words.sort(key = len)

for i in words:
    print(i)