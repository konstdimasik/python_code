import datetime as dt

today = dt.datetime.now().date()

print(today)

number1 = 0.12345
number2 = 181
number2 /= 90
print('{:.2f} __ {:.3f}'.format(number1, number2))
print(f'{number1:.2f} __ {number2:.3f}')

can_eat = 45
output_str = (
    'Сегодня можно съесть что-нибудь ещё,'
    f' но с общей калорийностью не более {can_eat} кКал')
print(output_str)

print(1900 % 100)
