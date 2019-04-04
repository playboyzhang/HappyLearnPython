# 每次我在 Google 上搜索一个主题时，都不会一次只看一个搜索结果。通过鼠
# 标中键点击搜索结果链接，或在点击时按住 CTRL 键，我会在一些新的选项卡中打
# 开前几个链接，稍后再来查看。我经常搜索 Google，所以这个工作流程（开浏览器，
# 查找一个主题，依次用中键点击几个链接）变得很乏味。如果我只要在命令行中输
# 入查找主题，就能让计算机自动打开浏览器，并在新的选项卡中显示前面几项查询
# 结果，那就太好了。让我们写一个脚本来完成这件事。
# 下面是程序要做的事：
# • 从命令行参数中获取查询关键字。
# • 取得查询结果页面。
# • 为每个结果打开一个浏览器选项卡。
# 这意味着代码需要完成以下工作：
# • 从 sys.argv 中读取命令行参数。
# • 用 requests 模块取得查询结果页面。
# • 找到每个查询结果的链接。
# • 调用 webbrowser.open()函数打开 Web 浏览器。
#! python3
# lucky.py - Opens several Google search results.


import requests,sys,webbrowser,bs4

print('Googling.......')     #display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()

#TODO: Retrieve top search result links.

#TODO: Open a browser tab for each result.



#Retrieve top search result links.

soup = bs4.BeautifulSoup(res.text)

#Open a browser tab for each result.

linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))