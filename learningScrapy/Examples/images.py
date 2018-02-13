import re
from urllib.request import urlopen, urlretrieve
from urllib.error import URLError

# url = "https://coll.jd.com/list.html?sub=23289&page=1&JL=6_0_0"

def craw(url, page):
    html1 = urlopen(url).read()
    html1 = str(html1)
    pat1 = '<div id="plist".+?<div class="page clearfix">'
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0]
    pat2 = '<img class="err-product" data-img="1" data-img="1" src="//(.+?\.jpg)".+?>'
    imagelist = re.compile(pat2).findall(result1)

    x = 1

    for imageurl in imagelist:
        imagename = "/Users/robinxyuan/Documents/jd_images/" + str(page) + str(x) + ".jpg"
        imageurl = "http://" + imageurl
        try:
            urlretrieve(imageurl, filename=imagename)
        except URLError as e:
            if hasattr(e, "code"):
                x += 1
            if hasattr(e, "reason"):
                x += 1
        x += 1

for page in range(1, 79):
    url = "https://coll.jd.com/list.html?sub=23289&page=" + str(page) +"&JL=6_0_0"
    craw(url, page)


# print(imagelist)
#
# print(result1)

