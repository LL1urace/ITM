# Практика
# Часть 5. Словари
#
# 1. Создайте словарь содержащий данные о человеке.
# В качестве строковых ключей используйте его имя, возраст, пол, рост, вес, размер ноги.
person = dict(
              age="22",
              sex="Мужской",
              height="200 см",
              weight="110 кг",
              foot_size="50")

# 2. Выведите на экран все данные о человеке по ключам.
print(person["name"])
print(person["age"])
print(person["sex"])
print(person["height"])
print(person["weight"])
print(person["foot_size"])

# 3. Добавьте в словарь ключ и значение размера ноги
person["foot_size2"] = "20"
print(person)

# 4. Удалите из словаря возраст.
person.pop("age", None) # С None удаление безопасное (нет ошибки если отсутствует ключ)
print(person)