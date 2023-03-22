sapun = int(input())
chinii = input()

ostanal_sapun = sapun * 750

sudomqlna_cnt = 0
chinii_cnt = 0
tendjeri_cnt = 0

while chinii != "End" and ostanal_sapun >= 0:
    sudomqlna_cnt += 1

    if sudomqlna_cnt % 3 != 0:
        ostanal_sapun -= int(chinii) * 5
        if ostanal_sapun < 0:
            break
        chinii_cnt += int(chinii)

    else:
        ostanal_sapun -= int(chinii) * 15
        if ostanal_sapun < 0:
            break
        tendjeri_cnt += int(chinii)

    chinii = input()

if ostanal_sapun >= 0:
    print(f"Detergent was enough!\n{chinii_cnt} dishes and {tendjeri_cnt} pots were washed.\nLeftover detergent {ostanal_sapun} ml.")

else:
    print(f"Not enough detergent, {abs(ostanal_sapun)} ml. more necessary!")