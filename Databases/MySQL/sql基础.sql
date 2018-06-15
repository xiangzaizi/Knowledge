-- mysql 数据库的操作

    -- 链接数据库
	mysql -uroot -pmysql

	
    
	-- 不显示密码
	mysql -uroot -p
	

    -- 退出数据库
	quit/exit/ctrl+d
    
    

    -- sql语句最后需要有分号;结尾
    -- 显示数据库版本 version
	select version();
    

    -- 显示时间
	select now();
	
    
    -- 查看当前使用的数据库
	select database();
    

    -- 查看所有数据库
	show databases;
	

    -- 创建数据库
    -- create database 数据库名 charset=utf8;
	create database student charset=utf8;
	

    -- 查看创建数据库的信息的语句
	show create database student;
     

    -- 使用数据库
    use student
 
    -- 删除数据库
	drop database student;

-- 数据表的操作

    -- 查看当前数据库中所有表
   show tables;
  
    

    -- 创建表
	-- int unsigned 无符号整型
    -- auto_increment 表示自动增长
    -- not null 表示不能为空
    -- primary key 表示主键
    -- default 默认值
    --unique  唯一的 此字段的值不允许重复
    ---decimal 小数位
    --bit  0和1 (like删除 or 不删)
    -- create table 数据表名字 (字段 类型 约束[, 字段 类型 约束]);
creat table students(id int primary key unsigned auto_increment not null);

    -- 查看表结构 字段
	desc studnets;
	
    -- 查看表的创建信息的语句
	show creat table students;
 
    -- 修改表-添加字段 mascot (吉祥物)
	alter table students add mascot varchar(20) not null;
   

    -- 修改表-修改字段：不重命名版  修改约束
	修改约束 默认值
      alter table students modify age int unsigned not null;

    -- 修改表-修改字段：重命名版
      alter table students change age data int unsigned not null;

    -- 修改表-删除字段
	alter table students drop data;

    -- 删除表
    -- drop table 表名;
    -- drop database 数据库;
    
-- 增删改查(curd)
    -- 增加

        -- 全列插入
        -- insert [into] 表名 values(...)
        -- 主键字段 可以用 0  null   default 来占位
       -- 向students表插入 一个学生信息  -- 多行插入
	insert into students values(0,"xiaohong",160.00,"女",18),(0,"jack",170.00,"男",19),
(0,"jack", 180.00,"男",17);

        -- 部分插入
        -- insert into 表名(列1,...) values(值1,...)
    	insert into students(name) values("tom");
        
	


    -- 修改
    -- update 表名 set 列1=值1,列2=值2... where 条件;
        -- 全部修改
		
		-- 按条件修改
	update students set name="laowang" where id=1;
		-- 按条件修改多个值
   update students set name="laowang",gender="女",age=18 where name="barry";
--insert 使用insert插入数据时数据不能空



    
    -- 查询基本使用
        -- 查询所有列
        -- select * from 表名;
      
        ---定条件查询
	select * from students where gender="男";
        


        -- 查询指定列
        -- select 列1,列2,... from 表名;
	select name,gender from students;
        


        -- 可以使用as为列或表指定别名
        -- select 字段[as 别名] , 字段[as 别名] from 数据表 where ....;
	select name as "姓名", gender as "性别" from students;
	        

        -- 字段的顺序
	select gerder,name from students;
        
    

    -- 删除
        -- 物理删除
        -- delete from 表名 where 条件
	delete from students where gender="女";
        
        -- 逻辑删除
        -- 用一个字段来表示 这条信息是否已经不能再使用了
        -- 给students表添加一个 is_delete 字段 bit 类型
	alter table students add is_delete bit default 0;
	update students set is_delete where id=4;
		
	
	-- 数据库备份与恢复	
		-- mysqldump –uroot –p 数据库名 > python.sql;
		-- mysql -uroot –p 新数据库名 < python.sql;

