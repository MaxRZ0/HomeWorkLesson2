coins = int(input("Введите общее коллчество монет: "))
coin_o = 0
coin_r = 0
check = True

for i in range(coins):
    coin = int(input(f"Положите моету {i+1} (0 или 1): "))
    if coin == 0:
        coin_o += 1
    elif coin == 1:
        coin_r += 1
    else:
        print("Неверное значение")
        check = False
        break

if check == True:
    if coin_r > coin_o:
        print(f"Колличество монет, необходимых перевернуть {coin_o}")
    else:
        print(f"Колличество монет, необходимых перевернуть {coin_r}")
