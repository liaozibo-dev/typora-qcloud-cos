secret_id = 'xxx'      # 建议使用环境变量 QCLOUD_COS_SECRET_ID 代替； 替换为用户的 secretId
secret_key = 'xxx'      # 建议使用环境变量 QCLOUD_COS_SECRET_KEY 代替；替换为用户的 secretKey
region = 'ap-nanjing'     # 替换为用户的 Region
token = None                # 使用临时密钥需要传入 Token，默认为空，可不填
scheme = 'https'            # 指定使用 http/https 协议来访问 COS，默认为 https，可不填
bucket='markdown-images-1253318070' # 'test-1253318070'
domain=f'https://{bucket}.cos.{region}.myqcloud.com/'