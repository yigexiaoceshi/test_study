# -*-coding: utf-8 -*-
"""
pytest
requests
"""
import requests

# 向http://www.baidu.com发起get氢气
r = requests.get("http://www.baidu.com")
# 获取响应体的文本，显示有乱码
print(r.text)
# 获取响应体的编码格式
print(r.encoding)
# 修改响应体的编码格式为utf-8
r.encoding = "utf-8"
# 查看响应体的编码格式
print(r.encoding)
# 再次获取响应体的文本，此时乱码消失
print(r.text)
# 获取请求状态码
print(r.status_code)
# 获取响应头信息
print(r.headers)
# 向http://httpbin.org/post发起post请求，传入参数{"key":"value"}
rr = requests.post("http://httpbin.org/post", data={"key": "value"})
# 获取响应体的文本
print(rr.text)
# 获取JSON格式的响应体
print(rr.json())
# 获取响应头信息
print(rr.headers)
# 获取响应的编码格式
print(rr.encoding)
# 获取相应状态码
print(rr.status_code)
# 获取二进制格式的响应体内容
print(rr.content)
import pytest

print(pytest)
