ticket = int(input('Сколько билетов вы хотите приобрести?'))
age = []
for i in range(1, ticket + 1):
    age.append(int(input(f'Введите возраст {i} посетителя: ')))
def ticket_prise(age):
    if age < 18:
         return 0
    elif 18 <= age <= 25:
        return 990
    elif 25 < age:
        return 1390
total = sum(map(ticket_prise, age))
discounted_prise = int(total * 0.9)
if ticket > 3:
    print('Общая стоимость билетов:', discounted_prise, "руб.")
else:
    print('Общая стоимость билетов:', total, 'руб.')
