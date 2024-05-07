import re

pattern = re.compile(r"[0-9]{2}") # get all 3 nums a row

print(pattern.findall("hi13b145192")) # ["145", "192"]