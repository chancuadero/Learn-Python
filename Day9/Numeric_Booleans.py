#Examples of numeric data type
x = 100
y = 42.1
print(x)
print(y)
print(type(x))
print(type(y))

stock_name = "TechCore Inc."
shares_owned = 157
purchase_price = 142.50
current_price = 158.73
cash_balance = 500.00

total_cost = shares_owned * purchase_price
current_value = shares_owned * current_price
profit_loss = current_value - total_cost

print(f"The total cost is {total_cost}")
print(f"The current value is {current_value}")
print(f"The profit_loss is {profit_loss}")

#Booleans
is_logged_in = True
has_premium_subscription = False
is_admin = True

can_access_content = is_logged_in and (has_premium_subscription or is_admin)

if can_access_content:
    print("Access Granted!")
else:
    print("Access Denied")