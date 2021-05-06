# Значение выручки
revenue = int(input('Введите значение выручки: '))
# Значение издержек
costs = int(input('Введите значение издержек: '))

if revenue > costs:
    print('Вы получаете прибыль.')
    # Рентабельность
    print('Рентабельность выручки: ', (revenue - costs) / revenue)
else:
    print('Вы не получаете прибыль. Надо что-то менять.')

# Численность сотрудников фирмы
number_of_employees_of_the_company = int(input('Введите число сотрудников фирмы: '))
# Прибыль на одного сотрудника
profit_per_employee = (revenue - costs) / number_of_employees_of_the_company
print('Прибыль на одного сотрудника составляет: ', profit_per_employee)
