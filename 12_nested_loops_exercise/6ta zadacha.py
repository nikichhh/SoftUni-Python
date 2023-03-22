movie = input()

student = 0
standard = 0
kid = 0
tickets = 0

while movie != "Finish":
    movie_name = movie
    places = int(input())
    mid = 0
    movie = input()

    while mid < places and movie != "Finish" and movie != "End":
        mid += 1
        if movie == "student":
            student += 1
        elif movie == "standard":
            standard += 1
        elif movie == "kid":
            kid += 1

        movie = input()

    if movie == "End":
        movie = input()

    print(f"{movie_name} - {float(mid) / places * 100:.2f}% full.")
    tickets += mid

print(f"Total tickets: {tickets}")
print(f"{float(student) / tickets * 100:.2f}% student tickets.")
print(f"{float(standard) / tickets * 100:.2f}% standard tickets.")
print(f"{float(kid) / tickets * 100:.2f}% kids tickets.")