apples =2
if apples:
    print("We have apples")

# Operators - a boolean evaluation context
cookie_qty = 0
if cookie_qty == 3:
    print("Cookie is 3")
else:
    print("No value")

#checking the truthiness of a value
my_list = []
print(bool(my_list)) #result in False as the list is empty
my_list.append('cookies')
print(bool(my_list)) #result in True as the list has a value

#Example of set created from a list
cookies_eaten_today = ['chocolate chip', 'peanut butter', 'chocolate chip','oatmeal cream']
types_of_cookies = set(cookies_eaten_today)
print(types_of_cookies)

#updating sets using .update()
cookies_hugo_ate = ['chocolate chip','anzac']
types_of_cookies.update(cookies_hugo_ate)
print(types_of_cookies)
