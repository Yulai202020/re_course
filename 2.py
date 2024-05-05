import re

string = "12.2 jihugy 12"
pattern = re.compile(r"(\+\-)?\d+(\.|,)?\d*") # find all decimal number or whole like 12.3 or 1. or 123

a = [x.group() for x in re.finditer(pattern, string)]

print(a) # idk why i cant do pattern.findall
print(pattern.findall(string)) # ITS NOT SAME!!!??? BRUH