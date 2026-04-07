#9.1
import json
from fileinput import filename

text = '''
{
    "products": [
        {"name": "Шоколад", "price": 50, "available": true, "weight": 100},
        {"name": "Кофе", "price": 100, "available": false, "weight": 250},
        {"name": "Чай", "price": 70, "available": true, "weight": 50}
    ]
}
'''
data = json.loads(text)
for product in data['products']:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
if product['available']:
    print("В наличии")
else:
    print("Нет в наличии!")
print()

#9.2
import json
text = '''
{
    "products": [
        {"name": "Шоколад", "price": 50, "available": true, "weight": 100},
        {"name": "Кофе", "price": 100, "available": false, "weight": 250},
        {"name": "Чай", "price": 70, "available": true, "weight": 50}
    ]
}
'''
data = json.loads(text)
count = int(input("Сколько продуктов хотите добавить"))
for i in range(count):
    print(f"\nПродукт {i + 1}:")
    name = input("Введите название продукта: ")
    price = int(input("Введите цену: "))
    weight = int(input("Введите вес: "))
    available = input("Есть в наличии? (да/нет): ").lower() == "да"

    new_product = {
        "name": name,
        "price": price,
        "available": available,
        "weight": weight
    }

    data['products'].append(new_product)

    # Вывод всех продуктов
    for product in data['products']:
        print(f"Название: {product['name']}")
        print(f"Цена: {product['price']}")
        print(f"Вес: {product['weight']}")
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()

#9.3
import os

#исходный словарь (русский → английский)
ru_en = {
    "кошка": "cat",
    "собака": "dog",
    "домашняя папка": "home",
    "дом": "home",
    "мышь": "mouse",
    "манипулятор мышь": "mouse",
    "делать": "to do",
    "изготавливать": "to do, to make"
}
en_ru = {}

for ru, eng in ru_en.items():
#разделяем английские слова по запятой
    eng_words = eng.split(", ")

    for eng_word in eng_words:
        if eng_word not in en_ru:
            en_ru[eng_word] = []
        if ru not in en_ru[eng_word]:
            en_ru[eng_word].append(ru)

#записываем в файл
try:
    with open("ru-en.txt", "w", encoding="utf-8") as f:
        for eng in sorted(en_ru.keys()):
            ru_words = ", ".join(sorted(en_ru[eng]))
            f.write(f"{eng} – {ru_words}\n")

#проверяем, создался ли файл
    if os.path.exists("ru-en.txt"):
        print("Файл ru-en.txt успешно создан!")
        print("\nСодержимое файла:")
        with open("ru-en.txt", "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("Файл не создался")

except Exception as e:
    print(f"Ошибка: {e}")


