from PIL import Image

from hashlib import md5
from io import BytesIO

class CosFile:
    """
        对要Cos上的文件进行抽象（或者对要上传的文件进行抽象）
    """
    def __init__(self, bytes):
        self.bytes = bytes
        self.md5 = md5(bytes).hexdigest()
        
        with BytesIO(bytes) as fp:
            self.format = Image.open(fp).format.lower()
    
    def getKey(self):
        """
            返回上传图片的文件名
        """
        return self.md5 + '.' + self.format

    def getBytes(self):
        """
            返回上传文件的字节流
        """
        return self.bytes