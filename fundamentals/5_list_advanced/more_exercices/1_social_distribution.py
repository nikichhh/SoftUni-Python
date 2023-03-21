line = [int(x) for x in input().split(', ')]
minimum_wealth = int(input())

for num in range(len(line) - 1):
    if line[num] < minimum_wealth:
        max_num = max(line)
        needed_money = minimum_wealth - line[num]
        line[line.index(max_num)] -= needed_money
        line[num] += needed_money

if sum(line) >= len(line) * minimum_wealth:
    print(line)
else:
    print("No equal distribution possible")
