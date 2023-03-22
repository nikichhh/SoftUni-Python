fat_perc = int(input())
prot_perc = int(input())
hlqb_perc = int(input())
calories = int(input())
water = int(input())

fat = (calories * (fat_perc / 100.0)) / 9
prot = (calories * (prot_perc / 100.0)) / 4
hlqb = (calories * (hlqb_perc / 100.0)) / 4
food = fat + prot + hlqb

calories_per_gram = calories / food
calories_per_gram -= (calories_per_gram * (water / 100.0))

print(f"{calories_per_gram:.4f}")