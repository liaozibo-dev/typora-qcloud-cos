import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="typora_cos",
    version="2.0.1",
    author="liaozibo",
    author_email="liaozibo@qq.com",
    description="tool for uploading typora images to qcloud cos",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/liaozb1996/typroa_qcloud_cos.git",
    packages=setuptools.find_packages(),
    package_data={
        'typora_cos': ['config.xml'],
    },
    install_requires=[
        'cos-python-sdk-v5',
        'requests',
        'Pillow',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)