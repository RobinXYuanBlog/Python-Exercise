# 贪婪模式与懒惰模式
# 贪婪模式 - 多匹配
# 懒惰模式 - 少匹配

import re

pattern1 = "p.*y"  # 贪婪模式
pattern2 = "p.*?y" # 懒惰模式

string = "abcdfphp345pythony_py"

result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)

print(result1)
print(result2)

