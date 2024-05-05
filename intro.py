import re

pattern = re.compile(r"[0-9]")

print(pattern.match("127564689")) # find first match (it is 1)
print(pattern.search("127564689")) # its same with pattern.match
print(pattern.findall("127564689")) # find all matches ["1", "2", "7", "5", "6", "4", "6", "8", "9"]
