from qcloud_cos.cos_exception import CosServiceError

from io import BytesIO

from typora_cos.factory.ClientFactory import ClientFactory
from typora_cos.factory.ConfigFactory import ConfigFactory


class CosClient:
    """
        职责：封装腾讯云SDK客户端，上传 CosFile 表示的文件到腾讯云对象存储
        设计模式：外观模式
    """
    def __init__(self):
        self.config = ConfigFactory.getConfig()
        self.client = ClientFactory.getClient()

    def upload(self, CosFile):
        url = 'https://{bucket}.cos.{region}.myqcloud.com/{key}'.format(bucket=self.config.bucket, region=self.config.region, key=CosFile.getKey())
        try:
            # 判断文件是否已经上传过
            self.client.head_object(self.config.bucket, CosFile.getKey())
            # 没有报错表示文件已经存在
            return url
        except CosServiceError as err:
            if err.get_error_code() == 'NoSuchResource':
                # 上传图片
                with BytesIO(CosFile.getBytes()) as fp:
                    self.client.put_object(
                        Bucket=self.config.bucket,
                        Body=fp,
                        Key=CosFile.getKey(),
                        StorageClass='STANDARD',
                        EnableMD5=False
                    )
                return url
            else:
                raise err

if __name__ == "__main__":
    from typora_cos.resource.ResourceLoader import ResourceLoader
    from typora_cos.service.CosFile import CosFile

    path = 'C:/Users/liaoz/Pictures/mc.jpg'
    resourceLoader = ResourceLoader(path)
    CosFile = CosFile(resourceLoader.getBytes())
    client = CosClient()
    url = client.upload(CosFile)
    print(url)