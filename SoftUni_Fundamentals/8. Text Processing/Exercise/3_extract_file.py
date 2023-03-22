file_stored = input().split(f"\\")
file = file_stored[-1].split(".")
name = file[0]
extension = file[-1]

print(f"File name: {name}\nFile extension: {extension}")
