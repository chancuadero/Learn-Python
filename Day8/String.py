#f-string (formatted string literals)
name = "Chan"
work = "Python Developer"
print(f"Hi! I'm {name}.")
print(f"An aspiring {work}.")

#Matching parts of a string - .startswith()
url = "https://python.org"
prefixes = ("https://", "http://", "ftp://")
if url.startswith(prefixes):
    print(f"{url} uses valid URL protocol.")

#Using list comprehension, unpacking the result
girl_names = ["Ana", "Julie", "Alice"]
print(*[name for name in girl_names if name.startswith("J")])