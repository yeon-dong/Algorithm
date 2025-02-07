def solution(bridge_length, weight, truck_weights):
    bridge_car = [0] * bridge_length
    bridge_sum = 0
    time = 0
    while len(truck_weights) != 0 or len(bridge_car) != 0:
        time += 1
        bridge_sum -= bridge_car.pop(0) #왼쪽거 하나 빼기
        if len(truck_weights) == 0:
            continue
        elif bridge_sum == 0:
            bridge_sum += truck_weights[0]
            bridge_car.append(truck_weights.pop(0))
        elif bridge_sum + truck_weights[0] <= weight:
            bridge_sum += truck_weights[0]
            bridge_car.append(truck_weights.pop(0))
        else:
            bridge_car.append(0)
    return time