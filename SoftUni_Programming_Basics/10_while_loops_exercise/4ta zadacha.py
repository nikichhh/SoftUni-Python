steps = ""
num_steps = 0
done_steps = 0

while num_steps < 10000:
    steps = input()
    if steps == "Going home":
        done_steps = int(input())
        num_steps += done_steps
        break

    done_steps = int(steps)
    num_steps += done_steps

if num_steps>= 10000:
    print(f"Goal reached! Good job!\n{num_steps-10000} steps over the goal!")
else:
    print(f"{10000-num_steps} more steps to reach goal.")