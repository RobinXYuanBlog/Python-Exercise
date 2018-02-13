html_str = """
<html>
<head>
<title> The Dormouse's story
</title>
</head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie class="sister" id="link1"><!--Elsie--></a>, 
<a href="http://example.com/lacie class="sister" id="link1"><!--Lacie--></a> and 
<a href="http://example.com/tillie class="sister" id="link1">Tillie</a>;
and they lived at the bottom of a well.
</p>
<p class="story">...</p>
</body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_str, 'lxml', from_encoding='utf-8')

# soup = BeautifulSoup(open('index.html'))

# 文档被转换为Unicode，并且HTML实例都被转换为Unicode编码
print(soup.prettify())