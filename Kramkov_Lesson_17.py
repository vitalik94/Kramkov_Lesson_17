# ДЗ на четверг (Ivanov_Lesson_17.py) - на гитхаб
# Описать два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение количества гласных и согласных букв меньше или равно длине слова,
# то выводить все гласные, иначе согласные;
# если передаю число, то вывести произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.
# Итого - один класс, в нем только ДВА МЕТОДА
# Тест:
# object(123) --> 6
# object('abcdef') --> bcdf

class Calculation:

    def product_letter_or_nums(self):
        vowels = 0
        consonants = 0
        listVowels = []
        listConsonants = []
        sumNum = 0

        if isinstance(self, str):

            for i in self:
                if i.isalpha():
                    if i.lower() in 'аоеёюяуиэыaeiouy':
                        vowels += 1
                        listVowels.append(i)
                    else:
                        consonants += 1
                        listConsonants.append(i)

            if vowels * consonants <= Calculation.search_length(self):
                print(f'Все гласные {listVowels}')
            else:
                print(f'Все согласные {listConsonants}')

        elif isinstance(self, int):

            for i in str(self):
                if int(i) % 2 == 0:
                    sumNum += int(i)

            print(f'Произведение суммы чётных цифр на длину числа: {sumNum * Calculation.search_length(self)}')

        else: print('Введены данные другого типа. Введите строку или число')

    def search_length(self):
        count = 0
        if isinstance(self, str):
            for i in self:
                count += 1
        elif isinstance(self, int):
            for i in str(self):
                count += 1

        return count


Calculation.product_letter_or_nums('abcdef')
Calculation.product_letter_or_nums(1234)

