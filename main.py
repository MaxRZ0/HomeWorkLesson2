import math

summ = int(input("Введите сумму чисел х и у: "))
comp = int(input("Введите произведение чисел х и у: "))
discr_0 = True

discr = (summ**2) - ((4 * -1) * -comp)

if discr < 0:
    discr_0 = False

if discr_0:
    x = (-summ + math.sqrt(discr)) / 2 * -1
    y = (-summ - math.sqrt(discr)) / 2 * -1
    print(f"x={int(x)}, a y={int(y)}")
else:
    print("Невозможно вычислить х и у")
