import re

text = ""

with open("test.txt") as f:
    text = f.read()

# find all time codes with titles

pattern = re.compile(r".*(\b\d{2}:\d{2}:\d{2}\b).*")
a = re.finditer(pattern, text)

for i in a:
    print("line with link:", i.group(0))