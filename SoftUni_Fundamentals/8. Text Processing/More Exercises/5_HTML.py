counter = 0

while True:
    line = input()
    if line == "end of comments":
        break

    if counter == 0:
        print(f"<h1>\n    {line}\n</h1>")
    elif counter == 1:
        print(f"<article>\n    {line}\n</article>")
    else:
        print(f"<div>\n    {line}\n</div>")

    counter += 1
