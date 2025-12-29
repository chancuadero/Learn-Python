#Error handling

def clean_text(text):
  # Check the data type
  if type(text) == str:
    return text.replace(" ", "_").lower()
  else:
    # Return a TypeError error if the wrong data type was used
    raise TypeError("The clean_text() function expects a string as an argument, please check the data type provided!")
    
print(clean_text("User Name 187"))


def area(length, width):
  try:
      if length == int and width == int:
        result = length * width
        return result
      else:
        raise ValueError("Invalid Input!")
  except Exception as e:
    print(f"An unexpected error occured: {e}")

print(area(3, "f"))