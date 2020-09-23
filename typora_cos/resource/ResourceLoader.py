import re

from typora_cos.resource.FileSystemResource import FileSystemResource
from typora_cos.resource.UrlResource import UrlResource

class ResourceLoader:
    """
        职责：从 path 加载字节流
        设计模式：策略模式 + 简单工厂方法
    """
    
    def __init__(self, path):
        if re.match(r'http|ftp', path):
            self.resource = UrlResource(path)
        else:
            self.resource = FileSystemResource(path)

    def getBytes(self):
        return self.resource.getBytes()