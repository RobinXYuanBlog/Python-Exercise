import re

# net address

pattern_net = "[a-zA-Z]+://[^\s]*[.com|.cn]"
string = "<a href='http://www.google.com'>Google</a>"
result_net = re.search(pattern_net, string)
print(result_net)


# phone number

pattern_phone = "\d{4}-\d{7}|\d{3}-\d{8}"
string_phone = "021-6726346657473545234"
result_phone = re.search(pattern_phone, string_phone)
print(result_phone)


# mail address

pattern_mail = "\w+([.+-]\w+)*@\w+([.-]\w+)*\.\w+([.-]\w+)*"
string_mail = "<a href='http://www.google.com'>Google</a><br>" \
              "<a href='mailto:c-e+o@iqianyue.com.cn'>Mail</a>"
result_mail = re.search(pattern_mail, string_mail)

print(result_mail)