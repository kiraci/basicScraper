import requests
from bs4 import BeautifulSoup

class News :
    def __init__(self):
        print("")

    def googleNews(self,searchedTerm):
        searched = searchedTerm
        targetUrl = "https://www.google.com/search?source=hp&ei=upvoXtWMDcmGwPAP9YKFsAs&q={}&oq={}&gs_lcp=CgZwc3ktYWIQAzIFCAAQgwEyBQgAEIMBMgUIABCxAzIFCAAQgwEyBQgAELEDMgIIADIFCAAQsQMyAggAMgUIABCDATIFCAAQsQNQvwtYtQ9guBBoAHAAeACAAe8BiAGGBpIBBTAuMi4ymAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab&ved=0ahUKEwjV0diRjYbqAhVJAxAIHXVBAbYQ4dUDCAc&uact=5".format(searched,searched)

        urlHtml = requests.get(targetUrl).content
        urlHtml = BeautifulSoup(urlHtml,"html.parser")

        mydivs = urlHtml.findAll("div", {"class": "BNeawe vvjwJb AP7Wnd"})
        
        print("\n") 
        print(" Related 3 Search Results from Google ".center(60,"*"))

        for i in range(0,3):
            print(mydivs[i].text)
