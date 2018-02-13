"""
对象可以分为四种

-Tag
-NavigableString
-BeautifulSoup
-Comment

## Tag

例如<title></title>

抽取title：```print(soup.title)```
抽取a：```print(soup.a)```

Tag中有attributes和name两个重要属性

```
print(soup.name) # [document]
print(soup.title.name)
```

Tag不仅可以获取name，还可以修改name

```
soup.title.name = 'mytitle'
```

soup中的属性

print(soup.p['class'])
print(soup.p.get('class'))

也可以获取全部属性

```
print(soup.p.attrs)
```

属性内容也可以进行修改


## NavigableString

获取Tag的neirong

```
print(soup.p.string)
print(type(soup.p.string))
```

通过unicode()方法可以将NavigableString转换为Unicode字符串

## BeautifulSoup

表示一个文档的全部内容
没有name和attributes属性

print(type(soup.name))
print(soup.name)
print(soup.attrs)

## Comment

获取文档注释内容

print(soup.a.string)
print(type(soup.a.string))

# 遍历文档树

## 子节点

Tag的 .contents属性可以将Tag子节点以列表方式输出。

```
print(soup.head.contents)
print(len(soup.head.contents))
print(soup.head.contents[0].string)
```

.children返回的是生成器，可以对Tag的子节点进行循环

```
for child in soup.head.children:
    print(child)
```

.descendants可以对所有Tag的子孙节点进行循环遍历

```
for child in soup.head.descendants:
    print(child)
```

.strings, .string and stripped_strings

.string

如果一个Tag中不包含任何Tag，返回Tag内容
如果只有唯一Tag，返回最里面内容
其他返回None

.strings主要应用于Tag中包含多个字符串的情况，可以进行循环遍历

```
for string in soup.strings:
    print(string)
```

.stripped_strings可以去掉输出字符串中包含的空格或空行

```
for string in soup.stripped_strings:
    print(repr(string))
```

## 父节点

.parent

获取某个元素的父节点

```
print(soup.title.parent)
```

.parents递归得到元素的所有父辈节点

```
print(soup.a)

for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
```

## 兄弟节点

.next_sibling 下一兄弟节点
.prev_sibling 上一兄弟节点

```
print(soup.p.next_sibling) # 输出空白，空白或者换行也可以被视为一个节点
print(soup.p.prev_sibling)
print(soup.p.next_sibling.next_sibling)
```


"""


html_str = """
<html><head><title> The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie class="sister" id="link1"><!--Elsie--></a>, 
<a href="http://example.com/lacie class="sister" id="link1"><!--Lacie--></a> and 
<a href="http://example.com/tillie class="sister" id="link1">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_str, 'lxml')

# soup = BeautifulSoup(open('index.html'))

# 文档被转换为Unicode，并且HTML实例都被转换为Unicode编码
# print(soup.name)
# print(soup.title.name)
#
# soup.title.name = 'mytitle'
# print(soup.title)
# print(soup.mytitle)
#
# print(soup.p['class'])
# print(soup.p.get('class'))
#
# print(soup.p.string)
# print(type(soup.p.string))
#
# print(soup.a.string)
# print(type(soup.a.string))

# print(soup.head.contents)
# print(len(soup.head.contents))
# print(soup.head.contents[1].string)
#
# for child in soup.head.children:
#     print(child)

# for child in soup.head.descendants:
#     print(child)
#
# print(soup.head.string)
# print(soup.title.string)
# print(soup.html.string)
#
# for string in soup.strings:
#     print(string)
#
#
# for string in soup.stripped_strings:
#     print(repr(string))

# print(soup.a)
#
# for parent in soup.a.parents:
#     if parent is None:
#         print(parent)
#     else:
#         print(parent.name)


print(soup.p.next_sibling)
print(soup.p.prev_sibling)
print(soup.p.next_sibling.next_sibling)
