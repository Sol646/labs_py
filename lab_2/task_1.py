money_capital = 10000  # подушка безопасности
salary = 5000  # Зарплата
spend = 8000  # Траты, превышающие доход
increase = 1.05  # Рост цен на 5%
month_cnt = 0

while money_capital + salary >= spend:
    money_capital += salary - spend
    spend *= increase
    month_cnt += 1

print("Сколько месяцев можно протянуть без долгов: ", month_cnt)
