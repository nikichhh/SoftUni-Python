n = int(input())
reservation = set()

for _ in range(n):
    reservation_num = input()
    reservation.add(reservation_num)

while True:
    guest_reservation_num = input()
    if guest_reservation_num == "END":
        break

    reservation.remove(guest_reservation_num)

print(len(reservation))
for num in sorted(reservation):
    print(num)
