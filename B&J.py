
karty = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4

import random
random.shuffle(karty)

print('Поиграем?')
count = 0

while True:
    choice = input('Будете брать карту? y/n\n')
    if choice == 'y':
        current = karty.pop()
        print('Вам выпала карта достоинством %d' %current)
        count += current
        if count > 21:
            print('Извините, но вы проиграли. У вас %d очков' %count)
            break
        elif count == 21:
            print('Поздравляем! Вы набрали 21.')
            break
        else:
            print('У вас %d очков.' %count)
    elif choice == 'n':
        print('У вас %d очков и вы завершили игру.' %count)
        break
print('До новых встреч!')