countries = input().split(', ')
capitals = input().split(', ')

country_capitals = {}

for i in range(len(countries)):
    country_capitals[countries[i]] = capitals[i]

for country, capital in country_capitals.items():
    print(f"{country} -> {capital}")