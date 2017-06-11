from bs4 import BeautifulSoup
import requests
def getrobot(url):
    if (url.endswith('/')):
        path = url
    else:
        path = url+'/'
    r = requests.get("http://" + path + "robots.txt")
    data = r.text
    s = BeautifulSoup(data,"lxml")
    s.decode("utf8")
    return str(s)
