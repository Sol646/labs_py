money_capital = 0  # подушка безопасности
salary = 5000  # Зарплата
spend = 8000  # Траты, превышающие доход
increase = 1.03  # Рост цен на 5%
month_number = 10

for i in range(month_number):
    money_capital += salary - spend
    spend *= increase

print("Необходимая подушка безопасности: ", round(abs(money_capital)))
