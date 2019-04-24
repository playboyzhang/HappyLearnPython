from urllib.request import urlopen
from io import StringIO
import csv
data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii','ignore')
dataFile = StringIO(data)
csvReader = csv.reader(dataFile)



for row in csvReader:
    print (row)


# textPage = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
# print(textPage.read(),'utf-8')