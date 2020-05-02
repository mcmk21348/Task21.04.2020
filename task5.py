a = input('ведите текст: ')
lower = 0
upper = 0

for i in a:
    if 'a' <= i <= 'z':
        lower +=1
    elif 'A' <= i <= 'Z':
        upper +=1


Zaglav = lower / len(a) * 100
propisnye = upper / len(a) * 100

print('Загланые: ', Zaglav)
print('Прорисные: ', propisnye)

