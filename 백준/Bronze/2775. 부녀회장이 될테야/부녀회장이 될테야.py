import sys

t = int(input())

for _ in range(t):
    floor = int(input())
    room = int(input())
    people_list = [ i for i in range(1,room+1)]
    for i in range(floor):
        this_floor_people = []
        people = 0
        for j in range(room):
            people += people_list[j]
            this_floor_people.append(people)
        people_list = this_floor_people
    print(people_list[-1])