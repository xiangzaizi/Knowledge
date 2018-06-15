-----------SQL语句
库之间操作 select
表之间的操作  alter

修改表
alter table studennts add name varchar(20) not null 

往表中添加字符---1.数据类型(int bit(0,1) decimal(5,2) varchar, enum())
							 gender enum('男','女','人妖','保密')
2. not null 3.default 4. primary key auto_increment 
-------------------------------------------------------------------------
-----------SQL查询：
1.给表/字段起别名
	关键词  as distinct(去重)
	给表起名
	select s.* from students as s;
	给字段起名
	select name as "姓名"， age as "年龄" from students;
	去重复数据
	select distinct gender from students;
	--查询指定行数据 limit(num-1, num-1)  like 显示2-4行信息
	select * from student limit 1,3;
	--SQL中查询当前年份
	select date_format(now(),'%Y')---显示目前年份
	--查询年龄22~26岁的学生信息 但表中没有age这一栏 **重点
	select id,(select date_format(now(),'%Y'))-birth as age
	,adderss from student
	where 2017-birth>=22 and 2017-birth<=26;
	


2.条件查询  where + 条件
	比较运算符: <, >, >=, <=, !=
	select * from students where age>=18;

	逻辑运算符: and, or, not 
	select * from students where age>=18 and gender=1;

	模糊查询： like, %--替换任意个 , _----替换一个
	"a%"---以a开始的数据
	"%a%"--含有a字符的数据
	"__" 查询有2个字的数据
	"__%" 查询至少有2个字的数据
	select * from students where name like "a%";  --以a开始的

	范围查询: in, not in, between， is null or is not null,
	where 主 in 子 查询
	--找出班级表中对应的名字
	select * from classes where id in (select cls_id from students);


	select * from students where age between 18 and 24;

	排序: order by 字段, asc 升序，desc 降序
	select * from students where (age between 18 and 24) and gender=1 order by age asc;
	
3.聚合函数	(分组数据可搭配使用)
	关键词: count(*), sum, min, max, avg, round(avg(age), 2)--保留小数位两位 
	select count(*) from students where gender=1;
	select min(age) from students;

4.分组
	关键词 group by 分组， group_concat(...) 对应...的数据， having 
	select * from students group by id; ----"only for id"
	select gender from students group by gender; ---按性别分组
	select count(*),age from students group by age;---按年龄分组并计算数量
	select group_concat(age), gender from students group by gender;--性别分组中显示对应年龄数据
	分组仅分组数据，在显示其他信息
	---按性别分组后，组中人数大于2的人的姓名
	select group_concat(name)from students group by gender having count(*)>2;
	-----按性别分组后，组中人数大于2的人的姓名 ---显示性别
	select group_concat(name),gender from students group by gender having count(*)>2;

	----总结: ???
	
5.分页
	关键词: limit--限制查询的数据 
	limit(页数, count)----某页---显示数据个数
	limit((页数-1)*2, 每页数据个数)
	
	select * from students limit 8, 3;
6.连接查询 

	关键词: --inner join ....on,--内链接查询--左连接查询--右连接查询
	select * from studnets inner join classes;
	--按要求显示姓名,班级
	select s.name, c.name from students as s inner join classes as c on s.cls_id=c.id;
select s.*, c.name from students as s inner join classes as c on s.cls_id=c.id;
select s.*, c.name from students as s inner join classes as c on s.cls_id=c.id order by c.name;	
	--left join
	---查询每位学生对应的班级信息
	select * from students left join classes on students.cls_id=classes.id;
	select * from students left join classes on students.cls_id=classes.id 
having classes.id is null;---等于右连接查询的数据
	1.排序 asc desc 
	2.order by
	3.having classes.id is null;
	4.-- select ... from xxx as s left join xxx as c on..... where .....
	-- select ... from xxx as s left join xxx as c on..... having .....
	
7.子查询
	select * from students where age=(select max(age) from students where gender=2);








--------------------------------------8.补充  重点
1.group.concat(name) ,分组后该项目中的人数
2.任何字段都可以分组
3.什么时候需要多个表？
	----当同一个数据表中的数据需要使用多次的时候就inner join多个表(不要怕慢慢拼)



--今日作业中题目查询参加计算机和英语考试的信息
select stu.* from student as stu 
inner join score as s1 inner join score as s2 on s1.stu_id = s2.stu_id
and stu.id = s1.stu_id and stu.id = s2.stu_id and s1.c_name = '计算机' and s2.c_name = '英语';

--查询姓名like 王 or 张中， on(like where) + 条件 最后在and 拼接数据

select * from student as s inner join score as c --on-- (name like"张%" or name like "王%") and c.stu_id=s.id;


--SQL中查询当前年份  ---给数据起名字
	select date_format(now(),'%Y')---显示目前年份
	--查询年龄22~26岁的学生信息 但表中没有age这一栏 **重点
	select id,(select date_format(now(),'%Y'))-birth as age
	,adderss from student
	where 2017-birth>=22 and 2017-birth<=26;


ambiguous 不明确的 模棱两可的

-------------------------------------------------------------------------------------------
SQL----day03
1.种类中价格最高的数据
select cate_name, max(price) from goods group by cate_name;

最高价格:
select * from goods 
inner join 
(select cate_name, max(price) as max_price from goods group by cate_name) as max_price_good on 
goods.cate_name=max_price_good.cate_name and goods.price=max_price_good.price.max_price;

分表
1.创建表 --cate_name=cate_id
create table if not exists goods_cates(
    id int unsigned primary key auto_increment,
    name varchar(40) not null);

create table if not exists goods_cates(
    id int unsigned primary key auto_increment,
    name varchar(40) not null);
2.将原表中种类提取出来
select cate_name from goods group by cate_name;
3.将查询的表放入goods_cates表中合成一张表  !!!
insert into goods_cates(name) (select cate_name from goods group by cate_name); 
4.连接两张表
select * from goods inner join goods_cates on goods.cate_name=goods_cates.name;
5.更新取出最后的表格--最后修改字段
update (goods inner join goods_cates on goods.cate_name=goods_cates.name) set goods.cate_name=goods_cates.id;

2.1
create table if not exists goods_brands(
    id int unsigned primary key auto_increment,
    brands varchar(40) not null);
select brand_name from goods group by brand_name;

insert into goods_brands(brands) (select brand_name from goods group by brand_name);

select * from goods inner join goods_brands on goods.brand_name=goods_brands.brands;
update (goods inner join goods_brands on goods.brand_name=goods_brands.brands) set goods.brand_name=goods_brands.id;



----------视图 事物  索引-------------
1.创建视图
create view v_students as
	select s.id,s.name,s.age, c.name as cs_name from students as s 
	inner join students as c on s.id=c.id;
删除视图表  drop view v_xxx
2.事物

针对突然中断的交易，不允许两步骤间数据传输的一致性，


-- 索引最主要解决的问题
	-- 当数据非常庞大时,并且这些数据不需要经常修改,为了加快查询速度,我们会使用索引
1.查看索引  show index from 表名
2.创建索引 create index 索引名称 on 表名(字段(长度))
	create index title_index on title_test(title(10));
3.删除索引 drop index xxx

set profiling=1;----开启运行时间监测
show profiles;-----查看执行的时间

----------------test
create table student1(
    id int unsigned unique primary key auto_increment not null,
    name varchar(40), 
    age int,
    high decimal(5,2),
    gender enum("男","女","中性"),
    is_show bit default 1);





反扒验证码
