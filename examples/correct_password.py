import re

pattern = re.compile(r"^[a-zA-Z0-9_!#\$]{8,16}$") # 8 - 16 symbols a-z with caps and without caps or numbers

print(pattern.match("P#$ss_w0rd!")) # true its normal password
print(pattern.match("tyy")) # its pretty small password