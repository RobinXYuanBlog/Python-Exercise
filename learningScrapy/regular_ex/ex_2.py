# ------------------- Table Ex 2 ------------------- #
#     Symbol     #              Meaning              #
#       .        #     All characters except '\n'    #
#       ^        #    Beginning position of string   #
#       $        #       End position of string      #
#       *        # 0, 1 or more times of before char #
#       ?        #     0 or 1 time of before char    #
#       +        #  1 or more times of before char   #
#      {n}       #       n times of before char      #
#      {n,}      #          at least n times         #
#     {n,m}      #            n to m times           #
#       |        #           Mode selection          #
#       ()       #              Mode unit            #
# -------------------------------------------------- #


import re

string = "abcdfphp345pythony_py"

# ------------------ Ex 2.1 ------------------ #

pattern21 = ".python..."
result21 = re.search(pattern21, string)
print(result21)


# ------------------ Ex 2.2 ------------------ #

pattern221 = "^abc"
pattern222 = "py$"

result221 = re.search(pattern221, string)
result222 = re.search(pattern222, string)

print(result221)
print(result222)


# ------------------ Ex 2.3 ------------------ #

pattern231 = "py.*n"
pattern232 = "cd{2}"
pattern233 = "cd{2,}"

string23 = "abcdddfphp345pythony_py"

result231 = re.search(pattern231, string23)
result232 = re.search(pattern232, string23)
result233 = re.search(pattern233, string23)

print(result231)
print(result232)
print(result233)


# ------------------ Ex 2.4 ------------------ #

pattern24 = "python|php"
result24 = re.search(pattern24, string)
print(result24)


# ------------------ Ex 2.5 ------------------ #

pattern251 = "(cd){1,}"
pattern252 = "cd{1,}"
string25 = "abcdcdcdcdfphp345pythony_py"

result251 = re.search(pattern251, string25)
result252 = re.search(pattern252, string25)

print(result251)
print(result252)