from collections import deque

green_light_duration = int(input())
free_window = int(input())

cars = deque()

timer = 0
counter = 0
while True:
    car_light = input()
    if car_light == "END":
        break

    if car_light == 'green':
        if cars:
            current_car = cars.popleft()
            seconds_left = green_light_duration - len(current_car)

            while seconds_left > 0:
                counter += 1

                if cars:
                    current_car = cars.popleft()
                    seconds_left -= len(current_car)
                else:
                    break

            if seconds_left == 0:
                counter += 1

            if free_window >= abs(seconds_left):
                if seconds_left < 0:
                    counter += 1
            else:
                idx = free_window + seconds_left
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[idx]}.")
                quit()
    else:
        cars.append(car_light)

print("Everyone is safe.")
print(f"{counter} total cars passed the crossroads.")
