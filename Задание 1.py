print(1)
my_name = 'Илья'
my_age = 32
my_profession = 'Тракторист.'
my_hobby = 'Играю на бас-гитраре.'
print('Привет! Я', my_name, '. Мне ', my_age, 'года.', 'Профессия -', my_profession, my_hobby)
programming_language = 'python'
print('Это моё первое знакомство с ', programming_language)

my_gorod = 'Анадырь'  # Мой город
my_years = 17  # Сколько лет Я проживаю в своём городе?
print('Живу в городе', my_gorod, 'уже', my_years, 'лет')
hometown = 'Владивосток'
print('Мой родной город', hometown)

name = input('Ваше имя? ')
city = input('Ваш город проживания? ')
years = input('Сколько лет живёте в Вашем городе? ')

print('Ваше имя', name, 'Ваш город проживания', city, 'Живёте в нём', years, 'лет?')

answer = input('Я Вас правильно понимаю? (да/нет)')
original_answer = 'да'
if answer == original_answer:
    print('Хорошо. Приятного вечера.')

else:
    print('Хорошо. Попробуем снова:')
    name = input('Ваше имя? ')
    city = input('Ваш город проживания? ')
    years = input('Сколько лет живёте в Вашем городе? ')

    print('Ваше имя', name, 'Ваш город проживания', city, 'Живёте в нём', years, 'лет?')

    answer = input('Я Вас правильно понимаю? (да/нет)')
    original_answer = 'да'
    if answer == original_answer:
        print('Хорошо. Приятного вечера.')
