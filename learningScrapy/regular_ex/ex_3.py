import re

pattern1 = "python"
pattern2 = "python"

string = "abcdfphp345Pythony_py"

result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string, re.I) # 忽略大小写

print(result1)
print(result2)
