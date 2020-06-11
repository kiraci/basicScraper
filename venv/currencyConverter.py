import urllib.request as request
import json

class Currency :
    def __init__(self):
        with request.urlopen('https://finans.truncgil.com/today.json') as response:
            source = response.read()
            data = json.loads(source)
            self.data = data



    def printValue(self, option):
        if option == '1':
            return self.data['ABD DOLARI']['Satış']
        elif option == '2':
            return self.data['EURO']['Satış']
        elif option == '3':
            return self.data['İNGİLİZ STERLİNİ']['Satış']
        elif option == '4':
            return self.data['Gram Altın']['Satış']
        elif option == '5':
            return self.data['Yarım Altın']['Satış']
        elif option == '6':
            return self.data['KANADA DOLARI']['Satış']
