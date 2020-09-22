import requests

class UrlResource:
    def __init__(self, path):
        self.bytes = requests.get(path).content
    
    def getBytes(self):
        return self.bytes