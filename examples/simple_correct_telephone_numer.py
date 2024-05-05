import re

pattern = re.compile(r"^(\+7|8)\s?\(?([0-9]{3})\)?\s?([0-9]{2})\-?\s?([0-9]{2})\-?\s?([0-9]{2})$")

print(pattern.match("8 (917) 23-23-23")) # true
print(pattern.match("+7 (917) 36 39 27")) # true
print(pattern.match("+7 (917) 363927")) # true
print(pattern.match("+7 971 323 23 23")) # false
print(pattern.match("+7 9713 23 23 23")) # false
print(pattern.match("6 821 13 13 12")) # false