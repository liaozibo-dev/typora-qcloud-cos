import xml.etree.ElementTree as ET
import os
import sys
import pathlib
import typora_cos


configPath = os.path.join(*pathlib.Path.home().joinpath('.typora_cos', 'config.xml').parts) 

class Config:
    def __init__(self, secretId, secretKey, region, token, scheme, bucket):
        self.secretId = secretId
        self.secretKey = secretKey
        self.region = region
        self.token = token
        self.scheme = scheme
        self.bucket = bucket

class ConfigFactory:

    @staticmethod
    def getConfig():
        """
            返回 Config 对象
        """
        def camel(text):
            """ 转换成驼峰状 """
            return text[0].lower() + text.title()[1:].replace('_', '')

        config = dict()
        # 读取配置文件
        try:
            tree = ET.parse(configPath)
            xmlConfig = {camel(property.attrib['name']): property.attrib['value'] for property in tree.findall('property')}
            config.update(xmlConfig)
        except FileNotFoundError as err:
            print('请先执行 python -m typora_cos.qcloud --init 生成配置文件，并完成配置')
            sys.exit(1)
        if config.get('token') == 'None': config['token'] = None
        # 读取环境变量
        for name, env in {'secretId': 'QCLOUD_COS_SECRET_ID', 'secretKey': 'QCLOUD_COS_SECRET_KEY'}.items():
            value = os.environ.get(env)
            if value is not None:
                config[name] = value
        return Config(**config)

if __name__ == "__main__":
    print(ConfigFactory.getConfig().bucket)