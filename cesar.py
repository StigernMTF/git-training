# Кодирование с помощью "шифра Цезаря" (на РУССКОМ алфавите).

alph = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя1234567890абвгдеёжзиклмнопрстуфхцчшщъыьэюя1234567890'
# Копирования  алфавита для шифрования последних букв алфавита
vvod = str(input('Какое слово хочешь закодировать?:'))
sdvig = int(input('На сколько идет сдвиг?(1-32):'))
vvod = vvod.lower()
enc = ""
for encrypt in vvod:
    pos = alph.find(encrypt)
    newpos = pos + sdvig
    if encrypt in alph:
        enc = enc + alph[newpos]
    else:
        enc = enc + encrypt
print(f'Твое сообщение:{enc}')
# Для декодирования нужно просто вписать номер сдвига с минусом
