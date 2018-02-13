import re

# ------------------ Ex 1.1 ------------------ #

pattern = "yue"
string = "http://yum.iqianyue.com"
result = re.search(pattern=pattern, string=string)
print(result)

# ------------------ Ex 1.2 ------------------ #

pattern_not_print = "\n"
str = '''http://yum.iqianyue.com
http://baidu.com'''
result_not_print = re.search(pattern_not_print, str)
print(result_not_print)

# ------------------ Ex 1.3 ------------------ #

pattern_mix = "\w\dpython\w"
string_mix = "abdsdf54pythonsdfa"
result_mix = re.search(pattern_mix, string_mix)
print(result_mix)

# ------------------ Ex 1.4 ------------------ #

pattern1 = "\w\dpython[xyz]\w"
pattern2 = "\w\dpython[^xyz]\w"
pattern3 = "\w\dpython[xyz]\W"

string_m = "abcdfphp345python_py"

result1 = re.search(pattern1, string_m)
result2 = re.search(pattern2, string_m)
result3 = re.search(pattern3, string_m)

print(result1)
print(result2)
print(result3)