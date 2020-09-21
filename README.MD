Python 依赖：
```
python3 -m pip install --upgrade pip
python3 -m pip install -U cos-python-sdk-v5
python3 -m pip install --upgrade Pillow
```

typora 设置：
```
d:\Miniconda3\Scripts\conda.exe run -n base python e:/pythonCode/cos_upload/upload.py
 ```

特性：
* 支持本地图片和网络图片上传（复制图片并粘贴到 typora）
* 通过图片字节流识别图片格式
* 通过 md5 避免重复上传图片

已知问题：
* 网络图片的URL不能包含请求参数（不能包含 `&` 字符）