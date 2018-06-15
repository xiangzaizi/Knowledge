

------ MongoDB 高级： 聚合应用 aggregate


一、$group



1. {$group : {_id : "$字段"}} 按指定字段进行分组（_id 是特殊的字段，用来表示分组依据）

对集合所有文档，按 "gender" 字段进行分组，产生两组数据 （仅仅分组，没有应用聚合方法）
> db.stu.aggregate([ {$group : {_id : "$gender"}}])
{ "_id" : false }
{ "_id" : true }


2. {$sum : 1}   统计个数

- 对集合所有文档，按"gender" 字段进行分组，并分别统计两组文档数据的个数（用count字段表示）
> db.stu.aggregate([ {$group : {_id : "$gender", count : {$sum : 1} }}])
{ "_id" : false, "count" : 2 }
{ "_id" : true, "count" : 6 }


3. {$sum : "$字段"}  计算指定字段值的总和

- 对集合所有文档，按"gender"字段进行分组，并分别统计两组文档数据"age"的总和（用sum_age字段表示）
> db.stu.aggregate([ {$group : {_id : "$gender", sum_age : {$sum : "$age"} }}])
{ "_id" : false, "sum_age" : 36 }
{ "_id" : true, "sum_age" : 157 }


4. {$avg : "$字段"}   计算指定字段值的平均数

- 对集合所有文档，按"gender"字段进行分组，并分别统计两组文档数据"age"的平均值（用avg_age字段表示）
> db.stu.aggregate([ {$group : {_id : "$gender", avg_age : {$avg : "$age"} }}])
{ "_id" : false, "avg_age" : 18 }
{ "_id" : true, "avg_age" : 26.166666666666668 }

- 对集合所有文档，按"hometown"字段进行分组，并分别统计两组文档数据"age"的平均值（用avg_age字段表示）
> db.stu.aggregate([ {$group : {_id : "$hometown", avg_age : {$avg : "$age"} }}])
{ "_id" : "中国", "avg_age" : 18 }
{ "_id" : "大理", "avg_age" : 30.5 }
{ "_id" : "桃花岛", "avg_age" : 29 }
{ "_id" : "蒙古", "avg_age" : 19 }


5. {$max : "$字段"}   计算指定字段值的最大数

- 对集合所有文档，按"hometown"字段进行分组，并分别统计两组文档数据"age"的最大值（用max_age字段表示）
> db.stu.aggregate([ {$group : {_id : "$hometown", max_age : {$max : "$age"} }}])
{ "_id" : "中国", "max_age" : 18 }
{ "_id" : "大理", "max_age" : 45 }
{ "_id" : "桃花岛", "max_age" : 40 }
{ "_id" : "蒙古", "max_age" : 20 }


6. {$min : "$字段"}   计算指定字段值的最小数

- 对集合所有文档，按"hometown"字段进行分组，并分别统计两组文档数据"age"的最小值（用min_age字段表示）
> db.stu.aggregate([ {$group : {_id : "$hometown", min_age : {$min : "$age"} }}])
{ "_id" : "中国", "min_age" : 18 }
{ "_id" : "大理", "min_age" : 16 }
{ "_id" : "桃花岛", "min_age" : 18 }
{ "_id" : "蒙古", "min_age" : 18 }
>

7. {$push : "$字段"}   计算指定字段所有的值，并存入数组中
- 对集合所有文档，按"hometown"字段进行分组，并分别统计两组文档数据中所有的"age"值（用all_age字段表示）
> db.stu.aggregate([ {$group : {_id : "$hometown", all_age : {$push : "$age"} }}])
{ "_id" : "中国", "all_age" : [ 18, 18 ] }
{ "_id" : "大理", "all_age" : [ 16, 45 ] }
{ "_id" : "桃花岛", "all_age" : [ 18, 40 ] }
{ "_id" : "蒙古", "all_age" : [ 20, 18 ] }

- 对集合所有文档，按"hometown"字段进行分组，并分别统计两组文档数据中所有的"name"值（用all_name字段表示）
> db.stu.aggregate([ {$group : {_id : "$hometown", last_name : {$last : "$name"} }}])
{ "_id" : "中国", "last_name" : "bigcat" }
{ "_id" : "大理", "last_name" : "段王爷" }
{ "_id" : "桃花岛", "last_name" : "黄药师" }
{ "_id" : "蒙古", "last_name" : "华筝" }


8. {$first : "$age"}    计算指定字段的第一个值

- 对集合所有文档，按"hometown"字段进行分组，并分别统计两组文档数据"age"的第一个值（用first_age字段表示）
> db.stu.aggregate([ {$group : {_id : "$hometown", first_age : {$first : "$age"} }}])
{ "_id" : "中国", "first_age" : 18 }
{ "_id" : "大理", "first_age" : 16 }
{ "_id" : "桃花岛", "first_age" : 18 }
{ "_id" : "蒙古", "first_age" : 20 }


9. {$last : "$age"}    计算指定字段的最后一个值

- 对集合所有文档，按"hometown"字段进行分组，并分别统计两组文档数据"name"的最后一个值（用last_name字段表示
> db.stu.aggregate([ {$group : {_id : "$hometown", first_name : {$first : "$name"} }}])
{ "_id" : "中国", "first_name" : "BigCat" }
{ "_id" : "大理", "first_name" : "段誉" }
{ "_id" : "桃花岛", "first_name" : "黄蓉" }
{ "_id" : "蒙古", "first_name" : "郭靖" }


用来分别输出分组后每组文档的所有数据信息
 db.stu.aggregate([{$group : {_id : "$gender", all_info : {$push : "$$ROOT"}}}])


二. $match 对文档进行条件过滤，语法等同于 find()条件查询，过滤结果可用于 group 分组处理

只对年龄大于等于18岁的文档 进行分组，再按籍贯分组，分别统计每组的姓名。
db.stu.aggregate([{$match : {age : {$gte : 18}}}, {$group : {_id : "$hometown", all_name : {$push : "$name"}}}])


只对 籍贯为 桃花岛和大理的 文档数据 按性别分组，同统计每组文档数据的姓名。
db.stu.aggregate([
    {$match : {hometown : {$in : ["桃花岛", "大理"]}}},
    {$group : {_id : "$gender", all_name : {$push : "$name"}}}
])



三. $project ；相当于 find() 的投影处理，只输出指定的字段

只对籍贯为蒙古和中国的文档数据 按性别分组，并统计平均年龄和所有人的姓名，最后投影只显示平均年龄
db.stu.aggregate([
    {$match : {hometown : {$in : ["蒙古", "中国"]}}},
    {$group : {_id : "$gender", avg_age : {$avg : "$age"}, all_name : {$push : "$name"}}},
    {$project : {_id : 0, avg_age : 1}}
])
_id 默认显示，必须手动指定为 0/false 表示不显示


四、 $sort : 对指定字段的值进行排序处理

$match ； 查找所有age小于45的文档数据
$group : 按hometown进行分组，并统计每组文档数据的 平均年龄和文档个数
$sort ；对文档数据按 avg_age 升序排序
$project : 最后投影显示 _id 和 avg_age 字段数据

db.stu.aggregate([
    {$match : {age : {$lt : 45}}},
    {$group : {_id : "$hometown", avg_age : {$avg : "$age"}, count : {$sum : 1}}},
    {$sort : {avg_age : 1}},
    {$project : {_id : 1, avg_age : 1}}
])

{ "_id" : "大理", "avg_age" : 16 }
{ "_id" : "中国", "avg_age" : 18 }
{ "_id" : "蒙古", "avg_age" : 19 }
{ "_id" : "桃花岛", "avg_age" : 29 }



五、 $skip 和 $limit : 分别表示 跳过前N个文档开始显示 和 显示前N个文档
db.stu.aggregate([
    {$match : {age : {$lt : 45}}},
    {$group : {_id : "$hometown", avg_age : {$avg : "$age"}, count : {$sum : 1}}},
    {$sort : {avg_age : 1}},
    {$project : {_id : 1, avg_age : 1}},
    {$skip : 1},
    {$limit : 2}
])



六、 $unwind : 对文档指定字段的值（如果是Arrays） 进行拆分，并返回拆分后的多个文档。

db.test.insert([
{ "_id" : 1, "item" : "a", "size": [ "S", "M", "L"] },
{ "_id" : 2, "item" : "b", "size" : [ ] },
{ "_id" : 3, "item" : "c", "size": "M" },
{ "_id" : 4, "item" : "d" },
{ "_id" : 5, "item" : "e", "size" : null }
])


对集合里所有文档的 size 字段进行拆分，
如果size的值是数组，则拆分为多个文档；
如果size的值是字符串，保持不变；
如果size的值是null、[] 或没有size字段，则默认忽略该文档。
> db.test.aggregate([{$unwind : "$size"}])

- 添加preserveNullAndEmptyArrays : true 保留 size的值是null、[] 或没有size字段 的文档（即结果保持不变）
> db.test.aggregate([{$unwind : {path : "$size", preserveNullAndEmptyArrays:true}}])


> db.stu.aggregate([{$group : {_id : "$gender", all_name : {$push : "$name"}}}])
{ "_id" : false, "all_name" : [ "黄蓉", "华筝" ] }
{ "_id" : true, "all_name" : [ "郭靖", "黄药师", "段誉", "段王爷", "BigCat", "bigcat" ] }
>
> db.stu.aggregate([{$group : {_id : "$gender", all_name : {$push : "$name"}}}, {$unwind : "$all_name"}])
{ "_id" : false, "all_name" : "黄蓉" }
{ "_id" : false, "all_name" : "华筝" }
{ "_id" : true, "all_name" : "郭靖" }
{ "_id" : true, "all_name" : "黄药师" }
{ "_id" : true, "all_name" : "段誉" }
{ "_id" : true, "all_name" : "段王爷" }
{ "_id" : true, "all_name" : "BigCat" }
{ "_id" : true, "all_name" : "bigcat" }



-- MongoDB 的索引

查看当前集合下所有的索引，注意每个所有都有一个name字段，表示索引名
db.num.getIndexes()

使用指定的字段做为索引
db.num.ensureIndex({name : 1})

删除指定的索引，注意参数是索引的name字段
db.num.dropIndex("name_1")

查看查询语句的执行状态
db.sum.find({name : "user12123"}).explain("executionStats")




-- MongoDb 数据备份和恢复（必须实现开启mongod服务）

将-h指定的MongoDB服务器的 test 数据库数据 备份到 -o 指定的目录下（默认会按数据库名新建下一级目录 test）
mongodump -h 127.0.0.1 -d test -o /data/db/

将--dir 指定目录下的数据库 恢复到 -h 指定的MongoDB服务器的 test 数据库下
mongorestore -h 127.0.0.1 -d test --dir /data/db/test







