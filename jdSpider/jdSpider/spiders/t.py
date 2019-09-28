import re

a = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv1826&productId=100004049987&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"

data = re.findall(r"page=(.*?)&", a)
# data = re.search(r"(?<=\().*(?=\);)", a).group()
print("="*60)
print(data)


