import re

pattern = re.compile(r"(https|http)://([a-zA-Z0-9_\-]+).(com|ru)")

a = re.finditer(pattern, "https://youtube-idk.com")

for i in a:
    print(i.group())