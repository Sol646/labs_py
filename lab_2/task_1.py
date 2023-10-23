money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month_cnt = 0

while money_capital + salary >= spend:
    money_capital += salary - spend
    spend += spend * increase
    month_cnt += 1

print("Количество месяцев, которое можно протянуть без долгов:", month_cnt)
