your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}
your_expenses_total = sum(your_expenses.values())
partner_expenses_total = sum(partner_expenses.values())

print("Your total expenses:",your_expenses_total)
print("Partner's total expenses:",partner_expenses_total)

if your_expenses_total > partner_expenses_total:
    print("you spent more money")
elif your_expenses_total < partner_expenses_total:
    print("your partner spent more money")
else:
    print("Both spent same money")

max_difference = 0
category_name = ""
for category in your_expenses:
    difference = abs(your_expenses[category]-partner_expenses[category])
    
    if difference > max_difference:
        max_difference = difference
        category_name = category
print("Category with the maximum difference is:",category_name)
print("Difference:",max_difference)