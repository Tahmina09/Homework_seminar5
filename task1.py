# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

string = 'Я люблю Джавуабв абви Питон'
my_list = list(filter(lambda s1: "абв" not in s1, string.split(" ")))
print(*my_list)