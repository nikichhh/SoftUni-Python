n = input()

n2 = list(set(n.split()))

team_a = 11
team_b = 11
is_terminated = False

for i in range(len(n2)):
    if "A" in n2[i]:
        team_a -= 1
    else:
        team_b -= 1

    if team_a < 7 or team_b < 7:
        is_terminated = True
        break

print(f"Team A - {team_a}; Team B - {team_b}")
if is_terminated:
    print(f"Game was terminated")