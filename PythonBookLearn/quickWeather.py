# 检查天气似乎相当简单：打开 Web 浏览器，点击地址栏，输入天气网站的 URL
# （或搜索一个，然后点击链接），等待页面加载，跳过所有的广告等。
# 其实， 如果有一个程序，下载今后几天的天气预报，并以纯文本打印出来，就可
# 以跳过很多无聊的步骤。该程序利用第 11 章介绍的 requests 模块，从网站下载数据。
# 总的来说，该程序将执行以下操作：
# • 从命令行读取请求的位置。
# • 从 OpenWeatherMap.org 下载 JSON 天气数据。
# • 将 JSON 数据字符串转换成 Python 的数据结构。
# • 打印今天和未来两天的天气。
# 因此，代码需要完成以下任务：
# • 连接 sys.argv 中的字符串，得到位置。
# • 调用 requests.get()，下载天气数据。
# • 调用 json.loads()，将 JSON 数据转换为 Python 数据结构。
# • 打印天气预报。
# 针对这个项目，打开一个新的文件编辑器窗口，并保存为 quickWeather.py。

#! python3
# quickWeather.py - Prints the weather for a location from the command line.


import json,requests,sys
# Compute location from command line arguments


if len(sys.argv)<2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])



#TODO: Download the JSON data from OpenWeatherMap.org's API.
url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()



#TODO: Load JSON dat into a Python variable

weatherData = json.load(response.text)
w = weatherData['list']

print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

