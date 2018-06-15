# -*- coding:utf-8 -*-
import itertools

"""itertools中的函数大多是返回各种迭代器对象"""
# 1. 连接多个列表或者迭代器     chain
# a = itertools.chain(range(3), range(4), [3,2,1])
# print(list(a))

# 2.求列表或生成器中指定数目的元素不重复的所有组合***     combinations
# x = itertools.combinations(range(4), 2)
# print(list(x))

# 3. 允许重复元素的组合       combinations_with_replacement
# x = itertools.combinations_with_replacement('ABC', 2)
# print(list(x))

# 3.3 按照真值表筛选元素    compress
x = itertools.compress(range(5), (True, False, True, True, False))
print(list(x))


# 4. 一个计数器, 可以指定起始位置和步长  count
# x = itertools.count(start=20, step=1)  # step 表示 +1/2... or -1
# print(list(itertools.islice(x, 0, 10, 1)))


# 5. 循环指定的列表和迭代器  cycle
# x = itertools.cycle('ABC')
# print(list(itertools.islice(x, 0, 12, 2)))

# 6.按照真值函数丢弃掉列表和迭代器前面的元素  dropwhile
# x = itertools.dropwhile(lambda e: e < 5, range(10))
# print(list(x))

# 7. 保留对应真值为False的元素   ifilterfalse
# x = itertools.ifilterfalse(lambda e:e<5, (1, 5, 3, 6, 9, 4))
# print(list(x))

# 8. 按照分组函数的值对元素进行分组   groupby
# x = itertools.groupby(range(10), lambda x:x<5 or x>8)
# for condition, numbers in x:
#     print(condition, list(numbers))

# 9. 上文使用过得函数, 对迭代器进行切片   islice
# x = itertools.islice(range(10), 0, 9, 2)
# print(list(x))

# 10. 产生指定数目的元素的所有排列(顺序有关)   permutations
# x = itertools.permutations(range(4), 3)
# print(list(x))

# 11. 产生多个列表和迭代器的(积)     product
# x = itertools.product('ABC', range(3))
# print(list(x))

# 12. 生成一个拥有指定数目元素的迭代器 repeat
# x = itertools.repeat(3, 5)
# print(list(x))

# 13. 类似map  starmap
# x = itertools.starmap(str.islower, 'aBCDefGhI')
# print(list(x))

# 14. 与dropwhile相反, 保留元素直至真值函数值为假  takewhile
# x = itertools.takewhile(lambda e:e<5, range(10))
# print(list(x))

# 15. 类似生成指定数目的迭代器  tee
# x = itertools.tee(range(10), 2)
# for let in x:
#     print(list(let))

# 16. 类似zip, 不过已较长的列表和迭代器长度为准  izip_longest
# x = itertools.izip_longest(range(3), range(5))
# y = zip(range(3), range(5))
# print(list(x))
# print(list(y))
