import re

html = ""

with open("3.html") as f:
    html = f.read()

pattern = re.compile(r'<a href="(.*)?"') # get all links
a = re.finditer(pattern, html)

for i in a:
    print("line with link:", i.group(0))
    print("link:", i.group(1), "\n")