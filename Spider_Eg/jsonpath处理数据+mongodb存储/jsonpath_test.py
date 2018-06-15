import jsonpath
# jsonpath测试
dict_obj = [{"name":"xiaoming", "age":20}, {"name":"xiaoli", "age":"21"}]

result_list = jsonpath.jsonpath(dict_obj, "$..name")  # $表示根目录, ..表示任意节点, name表示去需要的字段

print result_list # --->['xiaoming', 'xiaoli']

# jsonpath返回的是列表
# var js数据(result)也是列表所以这里的获取职位信息
result_list = jsonpath.jsonpath(dict_obj, "$..result")[0]
