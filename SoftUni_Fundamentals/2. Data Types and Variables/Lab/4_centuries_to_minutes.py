import math

centuries = int(input())
days = math.floor((centuries * 100) * 365.2422)
hours = days * 24
minutes = hours * 60

print(f"{centuries} centuries = {centuries * 100} years = {days:.0f} days = {hours:.0f} hours = {minutes:.0f} minutes")
