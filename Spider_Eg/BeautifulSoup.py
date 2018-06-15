from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

result = soup.find()  # 返回第一个匹配到的结果
result = soup.find_all()  # 返回所有匹配的结果, 返回的是列表
result = soup.select() # 返回所有匹配的结果, 返回时列表, 语法是CSS Selector

result = get_text()  # 取当前节点 的文本内容
result.get("href")  # 取指定属性值
