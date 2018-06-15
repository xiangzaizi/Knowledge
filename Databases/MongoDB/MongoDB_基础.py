

启用服务端：sudo redis-server
启用客户端：redis-cli
端口：6379

启用服务端：sudo mysql start
启用客户端：mysql -uroot -pxx
端口：3306

启用服务端：sudo mongod
启用客户端：mongo
端口：27017




一、MongoDB 注意点：

1. 首次使用，需要在根目录下创建 /data/db 目录，用来做为MongoDB默认的数据存储目录，并指定全部权限。
    $ sudo mkdir -p /data/db
    $ sudo chmod 777 /data/db

2. 之后在终端执行 sudo mongod，开启MongoDB服务；在终端执行 mongo，开启MongoDB shell客户端操作接口。

3. 关闭MongoDB服务的三种方式：
    -1 在MongoDB服务 终端界面 ctrl + c 关闭（推荐）；
    -2 在MongoDB shell 客户端内执行：
        > use admin
        > db.shutdownServer()
    -3 ps -aux | grep mongod 查询进程pid号，再通过 sudo kill -9 pid号 结束进程（不推荐）

4. 关闭MongoDB shell 客户端：
    -1 在MongoDB shell 客户端 终端界面 ctrl + c 关闭；
    -2 在MongoDB shell 客户端内执行：
        > exit


5. MongoDB 内可以有多个 数据库(db)；每个数据库可以有多个 集合(collections)，每个集合内可以有多个 文档(document)，每个文档 是由多个键值对 组成的 字典形式(dict)。


6. MongoDB数据库内提供的方法功能：如果是单个单词组成，则默认全部小写字母；如果是多个单词组成；则第一个单词的首字母小写，后面所有单词首字母大写（小驼峰），如 db.shutdownServer()

7. MongoDB的 数据库(db) 不需要单独创建，通过 use 切换即可使用，如 use admin。如果该 数据库(db) 内没有数据，数据库其实并没有创建；当数据库中存有数据时，才会真正创建该 数据库(db)。



二、MongoDB 基本操作命令：

查看当前所在的数据库
> db

查看MongoDB服务器中所有的数据库
> show dbs

切换到指定的数据库
> use XXX

查看当前数据库中所有的集合
> show collections

在当前数据库下 创建存储不设上限的集合 xxx
> db.createCollection("xxx")

在当前数据库下 创建存储上限为 1024 字节的集合 xxx （了解）
> db.createCollecion("xxx", {capped : true, size : 1024})

查看当前数据库 指定集合的 所有文档数据
> db.xxx.find()

删除当前数据库 指定集合 及其所有文档数据
> db.xxx.drop()

删除当前数据库 及其所有集合和文档数据
> db.dropDatabase()




三、MongoDB文档数据的插入 (insert)

1. 直接插入文档
> db.stu.insert({_id : 1, name : "关羽", age : 36})

2. 先构建空文档，再填充数据，最后插入

> data = {}
> data._id = 2
> data.name = "张飞"
> data.age = 34
> data
{ "_id" : 2, "name" : "张飞", "age" : 34 }

>
> db.stu.insert(data)

注意：新增的文档数据的_id必须是唯一的，如果没有_id，MongoDb默认会添加一个 objectId()类型的数据



四、文档数据的删除 (remove)

1. 默认删除所有符合匹配的文档
> db.stu.remove({"name" : "张飞"})

2. 添加可选参数 {justOne : true} 表示只删除第一个符合匹配的文档
> db.stu.remove({"name" :"张飞"}, {justOne : true})

3. 一般采用根据_id 删除文档
> db.stu.remove({_id : 4})

4. 当匹配条件为空时，默认全部删除
db.stu.remove({})


五、文档数据的修改 (update)

1. update必须有两个参数，第一个参数表示匹配条件，第二个参数表示替换后的全部文档数据（除_id 之外）
> db.stu.update({"name" : "关羽"}, {"age" : 38})
> db.stu.update({"age" : 38}, {"name" : "诸葛亮", "age" : 40})

2. 添加 $set 修饰符，只替换指定字段数据，其他字段不变
> db.stu.update({"name" : "张飞"}, {$set : {"age" : 38}})
> db.stu.update({"name" : "张飞"}, {$set : {"age" : 38, "name" : "喳喳"}})

3. 默认下只修改第一个符合匹配的结果，添加第三个可选参数 {multi : true} 表示全部修改。
> db.stu.update({"name" :"张飞"}, {$set : {"age" : 50}}, {multi : true})

4. 如果字段存在，则修改字段值；如果字段不存在，则添加该字段。
> db.stu.update({"name" :"张飞"}, {$set : {"hometown" : "蜀"}}, {multi : true})


六：save ： insert + update
db.stu.save() 语法等同于 insert()

1. 如果查找的对象 _id 不存在，则相当于insert新增该对象；
> db.stu.save({"_id": : 5, "name" : "诸葛亮", "age" : 40})
> db.stu.save({"_id": : 6, "name" : "司马懿", "age" : 40})

2. 如果查找的对象 _id 存在，则相当于 update 就更新该对象
> db.stu.save({"_id": : 5, "name" : "陆逊"})
> db.stu.save({"_id": : 6, "name" : "鲁肃", "age" : 40})





六：文档数据的查询 find()
1. 基本查询方法:
> db.stu.find() 默认查找所有的文档

> db.stu.find({"age" : 18}) 查找所有age为18的文档

> db.stu.findOne({"age" : 18}) 查找第一个age为18的文档数据

> db.stu.find().pretty() 将所有结果按json风格格式化显示


2. 比较运算符，用来处理数字的值
等于 ： 默认是等于
大于 ： $gt
大于等于 : $gte
小于 : $lt
小于等于 : $lte
不等于 : $ne

> db.stu.find({"age" : {$gt : 18}})
> db.stu.find({"age" : {$gte : 18}})
> db.stu.find({"age" : {$lt : 18}})
> db.stu.find({"age" : {$lte : 18}})
> db.stu.find({"age" : {$ne : 18}})

也可以和其他条件组合查找：
> db.stu.find({"age" : {$gt : 18}, "hometown" : "桃花岛"})


3. 逻辑运算符 $and $or

默认多个条件关系是 $and { : , :, : } 表示多个条件是与
> db.stu.find({"name" : "xxx", "age" : 18, "hometown" : "xxx"})

可以通过 $or : [{}, {}, {}] 来修饰多个条件是关系是 或
> db.stu.find({$or : [{"name" : "xxx"}, {"age" : 18}, {"hometown" : "xxx"}]})


表示查找年龄大于等于18岁，或性别为男性
> db.stu.find( {$or : [{"age" : {$gte : 18}}, {"gender" : true}] }  )

表示查找年龄大于等于18岁，或性别为男性， 并且籍贯为蒙古
> db.stu.find( {$or : [{"age" : {$gte : 18}}, {"gender" : true}], "hometown" : "蒙古" }  )


4、范围运算符 $in $nin

查找年龄在 [18, 20, 22] 范围中的文档数据
> db.stu.find({"age" : {$in : [18, 20, 22]}})

查找年龄不在 [18, 20, 22] 范围中的文档数据
> db.stu.find({"age" : {$nin : [18, 20, 22]}})


查询所有 蒙古或大理的 男性的 文档数据
> db.stu.find({"hometown": {$in : ["蒙古", "大理"]}, "gender" : true})

查询所有 蒙古或大理的， 或男性的 文档数据
> db.stu.find( {$or : [{"hometown": {$in : ["蒙古", "大理"]}}, {"gender" : true}]})



5. 正则表达式修饰符 $regex ，用来匹配字符串文本

> db.stu.find({"name" : /^段/})
{ "_id" : 5, "name" : "段誉", "hometown" : "大理", "age" : 16, "gender" : true }
{ "_id" : 6, "name" : "段王爷", "hometown" : "大理", "age" : 45, "gender" : true }

> db.stu.find({"name" : {$regex : "^段"}})
{ "_id" : 5, "name" : "段誉", "hometown" : "大理", "age" : 16, "gender" : true }
{ "_id" : 6, "name" : "段王爷", "hometown" : "大理", "age" : 45, "gender" : true }


查找所有name以 b 开始的 文档数据
> db.stu.find({"name" : {$regex : "^b"}})
{ "_id" : 8, "name" : "bigcat", "age" : 18, "hometown" : "中国", "gender" : true }
>
$options 表示启用正则的修饰符，"$i" 表示忽略大小写，查找所有name以 b或B 开始的 文档数据
> db.stu.find({"name" : {$regex : "^b", $options : "$i"}})


6. 自定义函数语句（类似于JavaScript函数语句）查询
查询所有年龄大于等于20的文档
> db.stu.find({$where : function() {return this.age >= 20}})

查询所有籍贯不是大理的文档
> db.stu.find({$where : function() {return this.hometown != "大理"}})






七、find() 查询后的结果处理

1. limit() 和 skip()
limit() 从头部开始显示指定4个文档
db.stu.find().limit(4)

skip() 从头部跳过指定4个文档再开始显示
db.stu.find().skip(4)

如果组合使用，先skip() 再 limit()
db.stu.find().limit(4).skip(2)




2. 投影（在 find() 的第二个参数指定显示需要的字段）

find() 第二个参数可以指定显示的字段值，1 和 true表示显示；0 和 false表示不显示
> db.stu.find({}, {"name" : 1, "age" : true})

默认字段是不显示的，除非指定为1或true；_id 字段默认是显示的，除非指定为 0或false
> db.stu.find({}, {"name" : 1, "age" : true, "_id" : 0})



3. sort() 排序：
先对性别进行降序排序；如果有相同的性别，再对相同性别的文档的age进行升序排序，
db.stu.find().sort({"gender" : -1, "age" : 1, })

1 表示升序
-1 表示降序


4. count() 统计个数

> db.stu.find().count()
> db.stu.count()


> db.stu.find({"age" : 18}).count()
> db.stu.count({"age" : 18})

count() 也可以直接写查询条件，但是返回值是文档的个数

5. distinct() 输出查询结果的指定字段，并去重，返回数组形式
显示 所有age大于等于18 的籍贯，并去重显示输出数组。
> db.stu.distinct("hometown", {"age" : {$gte : 18}})
[ "蒙古", "桃花岛", "大理", "中国" ]
