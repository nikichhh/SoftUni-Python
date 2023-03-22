a = int(input())
b = int(input())

minutes1 = b+15
minutes = minutes1%60

hours = a+minutes1//60

print(f"{hours}:{minutes:02d}")
# if hours==24:
#     if minutes<10:
#         print(f"0:0{minutes}")
#     else:
#         print(f"0:{minutes}")
# else:
#     if minutes<10:
#         print(f"{hours}:0{minutes}")
#     else:
#         print(f"{hours}:{minutes}")