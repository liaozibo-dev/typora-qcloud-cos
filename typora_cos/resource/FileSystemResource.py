class FileSystemResource:
    def __init__(self, path):
        with open(path, 'rb') as fp:
            self.bytes = fp.read()
        
    def getBytes(self):
        return self.bytes