import re

pattern = re.compile(r"[0-9]{3}") # get all 3 nums a row

print(pattern.findall("hi 13b 145 192")) # ["145", "192"]