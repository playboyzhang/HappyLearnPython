# 博客和其他经常更新的网站通常有一个首页，其中有最新的帖子，以及一个“前
# 一篇”按钮，将你带到以前的帖子。然后那个帖子也有一个“前一篇”按钮，以此
# 类推。这创建了一条线索，从最近的页面，直到该网站的第一个帖子。如果你希望
# 拷贝该网站的内容，在离线的时候阅读，可以手工导航至每个页面并保存。但这是
# 很无聊的工作，所以让我们写一个程序来做这件事。
# XKCD 是一个流行的极客漫画网站，它符合这个结构（参见图 11-6）。首页
# http://xkcd.com/有一个“Prev”按钮，让用户导航到前面的漫画。手工下载每张漫
# 画要花较长的时间，但你可以写一个脚本，在几分钟内完成这件事。
# 下面是程序要做的事：
# • 加载主页；
# • 保存该页的漫画图片；
# • 转入前一张漫画的链接；
# • 重复直到第一张漫画。
# 这意味着代码需要做下列事情：
# • 利用 requests 模块下载页面。
# • 利用 Beautiful Soup 找到页面中漫画图像的 URL。
# • 利用 iter_content()下载漫画图像，并保存到硬盘。
# • 找到前一张漫画的链接 URL，然后重复。
#!python3
#DownloadXkcd.py - Downloads every single XKCD comic.

import requests,os,bs4

url ='http://xkcd.com'    #starting url
os.makedirs('xkcd',exist_ok=True)   #store comics in ./xkcd
while not url.endswith('#'):
    # Todo: Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    # Todo: Find the URL of the comic image.

    comicElem = soup.select('#comic img')
    if comicElem ==[]:
        print('Could not find comic image.')
    else:
        for comic in comicElem:
            comicUrl = 'http:'+ comic.get('src')
            if 'comics' in comicUrl:
                # Todo: Download the image.
                print('Downloading image %s...' %(comicUrl))
                res = requests.get(comicUrl)
                res.raise_for_status()



                # Todo: Save the image to ./xkcd.
                imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()


    # Todo: Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
print('Done...')



