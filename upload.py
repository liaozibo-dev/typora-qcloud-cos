# -*- encoding: utf-8 -*-

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from qcloud_cos.cos_exception import CosServiceError
import requests
from PIL import Image

from io import BytesIO
from hashlib import md5
import sys

import settings



# 根据图片文件对象返回上传文件名
def getUploadName(fp):
    key = md5(fp.read()).hexdigest() + '.' + Image.open(fp).format.lower()
    fp.seek(0)
    return key

# 判断要上传的图片是否已经上传过
def exists(client, key):
    try:
        r =  client.head_object(settings.bucket, key)
        return r.get('ETag') != None
    except CosServiceError as e:
        if e.get_error_code() == 'NoSuchResource':
            return False
        else:
            raise e


def upload(client, path):
    # 上传URL图片
    if path.startswith('http'):
        with requests.get(path) as r:
            with BytesIO(r.content) as fp:
                key = getUploadName(fp)
                if not exists(client, key):
                    response = client.put_object(
                        Bucket=settings.bucket,
                        Body=r.content,
                        Key=key,
                        StorageClass='STANDARD',
                        EnableMD5=False
                    )
                return key
    # 上传本地图片
    with open(path, 'rb') as fp:
        key = getUploadName(fp)
        if not exists(client, key):
            response = client.put_object(
                    Bucket=settings.bucket,
                    Body=fp,
                    Key=key,
                    StorageClass='STANDARD',
                    EnableMD5=False
                )
        return key


def main():
    # 初始化客户端 
    config = CosConfig(Region=settings.region, SecretId=settings.secret_id, SecretKey=settings.secret_key, Token=settings.token)
    client = CosS3Client(config)

    # 上传图片
    urls = list()
    for path in sys.argv[1:]:
        key = upload(client, path)
        urls.append(settings.domain + key)
    # 输出上传后图片的URL
    print("upload success:")
    for url in urls:
        print(url)

if __name__ == "__main__":

    # p1 = 'C:/Users/liaoz/Pictures/mc.jpg'
    # p2 = 'C:/Users/liaoz/Pictures/sunset.jpg'
    # r = upload(p1, p2)
    # print(r)
    main()