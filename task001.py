# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.lower().split()))
    return " ".join(my_text)

my_text = 'абвгдеж рабав копыто фабв Абкн абрыволк аБволк'
my_text = del_some_words(my_text)
print(my_text)
