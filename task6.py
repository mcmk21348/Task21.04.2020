weigth = int(input('Введите вес в кг: '))
in_moon = weigth * 0.165
if_15let = 1 * 15 * 0.165
in_moon_after15let = in_moon +  if_15let
za15let = in_moon_after15let - in_moon
print('Ваш вес через 15 лет на луне: ', in_moon_after15let)
print('Вы добавите: ', za15let)

#2Способ с циклом 

for i in range(15):
    weigth += 1
    in_moon = weigth * 0.165
    print(in_moon)

