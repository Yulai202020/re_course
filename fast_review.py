import re

pattern = re.compile(r"([0-9]{1})\1")

# ^ - начало строки
# $ - конец строки
# \b - начало или конец слова
# | - или одно или другое
# [.?,!] - есть ли эти сиволы в строке
# ^[./]HI - строка начанается с . или / а потом идёт HI
# \b[^ABC] - слово НЕ начанается с A,B,C

# \d = [0-9]
# \D = [^0-9]
# \w = [a-zA-Z0-9_]
# \s = [ ]
# \S = [^ ]
# . = any

# [0-9]{3} - 3 цифры подряд
# [0-9]{3,5} - от 3 до 5 цифр подряд

# [0-9]+ = [0-9]{1,} - колво цифр от 1 до бесконечности
# [0-9]* = [0-9]{0,} - колво цифр от 0 до бесконечности
# [0-9]? = [0-9]{0,1} - колво цифр от 0 до 1

# () - групировка
# \n $n - copy nth group

# X(?=Y) - 
# X(?|Y) - 
# (?<=Y)X - 
# (?<!Y)X - 

print(pattern.search("11"))