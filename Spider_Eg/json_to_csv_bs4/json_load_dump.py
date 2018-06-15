# -*- coding:utf-8 -*-
# 1. json.dumps是将一个Python数据类型列表进行json格式的编码解析
# 测试:
import json
a  =  ['iplaypython',[1,2,3], {'name':'xiaoming'}]
encode_json = json.dumps(a)  # 将列表进行了json格式的编码

# 2. 解码python json格式, json.loads()
decode_json = json.loads(encode_json)  # 解码Python数据风格


# 3. json.dump主要用来json文件读写, 和json.load函数配合使用


# data = [{"a":"aaa","b":"bbb","c":[1,2,3,(4,5,6)]},33,'tantengvip',True]
# data2 = json.dumps(data)
# print(data2)

# json.dump(data2, open('./tt.txt','a'))
# 这样就生成了一个tt.txt文件，保存了json格式的数据。dumps还提供pritty print，格式化的输出。

# json.load加载json格式文件   下面是从txt文件中读取了json数据。
# f = open('./tt.txt','r')
# hehe = json.load(f)
# print(hehe)
