print(
    "\u4f60\u63d0\u4ea4\u8fc7\u6765\u7684\u77ed\u4fe1\u5185\u5bb9\u5fc5\u987b\u4e0e\u62a5\u5907\u8fc7\u7684\u6a21\u677f\u683c\u5f0f\u76f8\u5339\u914d")
print('\u63d0\u4ea4\u6210\u529f')
from hashlib import md5

md = md5()
md.update("123".encode('utf-8'))
sign = md.hexdigest()
print(sign)
