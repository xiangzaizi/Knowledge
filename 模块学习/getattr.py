class AA(object):
	n = 10
	def func(self, num):
		print(num)
a = AA()
f = getattr(a, "func")  # 经过getattr后f就是func
print: (100)--->打印出:100
print: getattr(a, "n")---> 10
总结: 方法 or 属性都是AA这个类的.
getattr(a, "字符串or 属性")-->就相当于这个获取到了这个类的方法和属性
