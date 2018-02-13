import re

# re.match(pattern, string, flag)

string = "apythonhellomypythonhispythonourpythonend"
pattern = ".python."

result = re.match(pattern, string)
result2 = re.match(pattern, string).span()

print(result)
print(result2)


# re.search()
string2 = "hellomypythonhispythonourpythonend"

result3 = re.search(pattern, string2)
result4 = re.match(pattern, string2)

print(result3)
print(result4)


# 全局匹配函数

pattern2 = re.compile(".python.") # 预编译
result5 = pattern2.findall(string)

print(result5)


# re.sub(pattern, rep, string, max)

pattern3 = "python."
result6 = re.sub(pattern3, "php", string)  # 全部替换
result7 = re.sub(pattern3, "php", string, 2)  # 最多替换两次

print(result6)
print(result7)

