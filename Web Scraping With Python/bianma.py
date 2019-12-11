# from urllib.request import urlopen
# from io import StringIO
# import csv
# data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii','ignore')
# dataFile = StringIO(data)
# csvReader = csv.reader(dataFile)
#
#
#
# for row in csvReader:
#     print (row)


# textPage = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
# print(textPage.read(),'utf-8')



# import requests
#
# session = requests.Session()
#
# params = {'usrname':'username','password':'password'}
#
# s = session.post("http://pythonscraping.com/pages/cookies/welcome.php",params)
#
# print("Cookie is set to:")
# print(s.cookies.get_dict())
# print("---------------")
# print("Going to profile page...")
# s = session.get("http://pythonscraping.com/pages/cookies/profile.php")
# print(s.text)

# import requests
# from requests.auth import AuthBase
# from requests.auth import HTTPBasicAuth
#
# auth = HTTPBasicAuth('ryan','password')
#
# r = requests.post("http://pythonscraping.com/pages/auth/login.php",auth=auth)
#
# print(r.text)



from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.ID,"loadedButton")))
finally:
    print(driver.find_element_by_id("content").text)
    driver.close()



