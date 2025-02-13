arr = []
num_index = 0
for i in range(3):
    arr.append(input())
    if not(arr[i]=="Fizz" or arr[i]=="Buzz" or arr[i]=="FizzBuzz"):
        arr[i] = int(arr[i])
        num_index = i
next_num = arr[num_index] + (3 - num_index)

if next_num % 15 == 0:
    print("FizzBuzz")
elif next_num % 3 == 0:
    print("Fizz")
elif next_num % 5 == 0:
    print("Buzz")
else:
    print(next_num)