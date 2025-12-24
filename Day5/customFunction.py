#custom functions
def calculate_area(length, width):
    area = length * width
    return area

room_area = calculate_area(4,8)
print(f"The area is: {room_area}")

#Using default value
list_digits = [12.322,4.4,56.2,6.2,65.7]
def average(values, rounded = False):
    if rounded == True:
        average_num = sum(values)/len(values)
        rounded_average = round(average_num, 2)
        return rounded_average
    else:
        average_num = sum(values)/len(values)
        return average_num
    
print(average(list_digits))

#Adding a keyword argument
product = input("Please enter any word:")

def clean_text(text, lower=True):
    clean_text = text.replace(' ','_')
    if lower == False:
        return clean_text
    else:
        return clean_text.lower()
    
print(clean_text(product))