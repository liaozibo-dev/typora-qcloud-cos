# -*- coding: utf-8 -*-

import pathlib
import os
import sys
import shutil
import typora_cos

from typora_cos.service.CosClient import CosClient
from typora_cos.resource.ResourceLoader import ResourceLoader
from typora_cos.service.CosFile import CosFile

"""
    程序主入口：提供生成配置文件和上传文件功能
"""


def initConfig():
    """
        生成配置文件
    """
    configDirPath = os.path.join(*pathlib.Path.home().joinpath(".typora_cos").parts)
    configTemplatePath = os.path.join(os.path.dirname(os.path.abspath(typora_cos.__file__)), 'config.xml')
    configFilePath = os.path.join(configDirPath, 'config.xml')
    if not os.path.exists(configFilePath):
        os.makedirs(configDirPath, exist_ok=True)
        shutil.copy(configTemplatePath, configFilePath)
        print('已生成配置文件，请继续完成配置：', configFilePath)
        print('从 https://console.cloud.tencent.com/cam/capi 获取 SecretId 和 SecretKey')
        print('从 https://console.cloud.tencent.com/cos5/bucket 创建存储桶并得到存储桶名称 bucket 和 所属区域 scheme')
    else:
        print("配置文件已存在，请先删除：", configFilePath)

def upload():
    """
        从命令行读取一个或多个路径并将其文件上传到腾讯云对象存储
    """
    paths = sys.argv[1:]
    client = CosClient()
    urls = list()
    for path in paths:
        resourceLoader = ResourceLoader(path)
        cosFile = CosFile(resourceLoader.getBytes())
        url = client.upload(cosFile)
        urls.append(url)

    print("已成功上传：")
    for url in urls: print(url)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--init':
        initConfig()
    else:
        upload()