from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

from typora_cos.factory.ConfigFactory import ConfigFactory

class ClientFactory:
    @staticmethod
    def getClient():
        # 初始化客户端 
        config  = ConfigFactory.getConfig()
        cosConfig = CosConfig(Region=config.region, SecretId=config.secretId, SecretKey=config.secretKey, Token=config.token)
        client = CosS3Client(cosConfig)
        return client


if __name__ == "__main__":
    client = ClientFactory.getClient()
    print(client.list_buckets())