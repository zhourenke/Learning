

import random

players_guess = input("请出拳（石头/剪刀/布）：")
ais_list = ("石头", "剪刀", "布")
ais_guess = random.choice(ais_list)
print(f"*AI出的是{ais_guess}")
if (players_guess == "石头" and ais_guess == "剪刀") or \
        (players_guess == "剪刀" and ais_guess == "布") or \
        (players_guess == "布" and ais_guess == "石头"):
    print("你赢了")
elif players_guess == ais_guess:
    print("平局")
else:
    print("你输了")
