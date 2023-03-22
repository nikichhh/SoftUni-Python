mackerel_price = float(input())
sprinkle_price = float(input())
benito = float(input())
safrid = float(input())
mussles = int(input())

benito_bought = mackerel_price * 1.6 * benito
safrid_bought = sprinkle_price * 1.8 * safrid
mussles_bought = mussles * 7.5

print(f"{benito_bought + safrid_bought + mussles_bought:.2f}")