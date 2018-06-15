-----------------Redis kev-value 数据库
NoSQL ---一类新出现的数据库
	1. 不支持SQL语法
	2. nosql存储的数据都是KV形式
	3. NoSQL种类: Mongodb, Redis, Hbase hadoop, Cassandra hadoop

NoSQL与SQL比较：
	1. 适用场景不同：sql数据库适合用于关系特别复杂的数据查询场景，nosql反之
	2. “事务”特性的支持：sql对事务的支持非常完善，而nosql基本不支持事务
	
redis应用场景：
		1. 用来做缓存
		2. 替代传统数据库---社交类应用
		3. session共享、购物车
		
1. 安装

2. 核心配置选项
	配置redis.conf
	sudo vi /etc/redis/redis.conf
	redis配置信息参考: http://blog.csdn.net/ljphilp/article/details/52934933
	
	1. 绑定ip： 远程访问: 注释 bind 127.0.0.1
	2. 端口：默认6379
	3. 是否守护进程运行
		daemonize yes
		守护进程,不会在命令端阻塞反之会阻止命令端.
	
	4. 数据文件   dbfiedname dump.rdb 
	5. 数据文件存储路径 dir/ var/lib/redis
	6. 日志文件 logfile /var/log/redis/redis-server.log     ---163
	7. 数据库,默认由16个 database 16  						
	8. 主从复制, 类似于双机备份  slaveof      ----在211行
 	
	
3. 服务端和客户端
	服务器端命令: redis -server
	 启动: sudo service redis start
	 停止: sudo service redis stop 
	 重启: sudo service redis restart
	 
	!!!常用:
		ps aux |grep redis 查看redis服务器进程
		
		停止: sudo kill -9 pid 杀死redis服务器
			  如: sudo kill -9 3782
			  
		启动: sudo redis-server   /etc/redis/redis.conf 指定加载的配置文件
		
	!!!客户端命令:
		1. 连接: redis-cli
			like :redis-cli -h '192.168.177.140' -p '6381'   
			redis-cli --help ---可以看到h 和p是默认的就不用写.
		
		2. 测试命令: ping
		
		3. 切换数据库:select 10  (数据库没有名称,默认16个,通过0-15来标识)
		
		4. redis-li中的16个数据库是？
			1. 相互间数据不受影响
		

4. 数据操作
	1. 数据结构
		1.1 redis是key-value的数据结构,每条数据都是一个键值对
		1.2 键的类型是字符串
		注意:  键不能重复
		
		1.3. 值的类型五种:
			字符串: string
			哈希: hash
			列表：list
			集合：set
			有序集合: zset
	2. 数据操作的行为
		保存
		修改
		获取
		删除
		
	flushdb命令 ----清除数据
	flushall命令 ---会清除这个实例的数据,在执行这个命令前要格外小心.


	
-----------------------------string类型
	1. 接受任何数据格式的数据, 二进制安全
	2. 最大容量为512M
	
	保存：
		# 设置值,value没有时添加,有就修改
		set name itcast
		get name
		
		# 设置值及过期时间, 以秒为单位
		setex name  10 itcast
		
		# 设置多个键值
		mset n1 v1 n2 v2 n3 v3
		
		# 追加值
		append n1 hh
	
	获取:
		# 获取值
		get key
		# 获取多个值
		mget n1 n2 n3
	
	删除:
		del key
	
redis命令参考:百度一下


------------------------------!!!键命令：
		# 查看所有键
		keys *
		
		# 查看名称中包含a的键
		keys a*
		
		# 判断键是否存在, 存在返回1, 不存在返回0
		exists key
		
		# 查看键对应的value的类型
		type key
		
		# 删除键及对应的值
		del key
		del key3 key4
		
		# 设置过期时间, 以秒为单位, 没有指定过期时间,一直存在直到使用del删除
		# 过期时间返回-1  表示永不过期
		expire key seconds
		
		# 查看有效时间
		ttl key
		没有设置时间,一直存在返回-1
		
---------------------------hash类型
	1. hash用于存储对象,对象的结构为属性、值
	2. 值的类型为string
	
	增加:
		# 设置单个属性和值
		hset user name lisi
		# 设置多个属性和值
		hmset u1 name lisi age 18 high 175
	获取:
		# 获取属性
		hkeys key
		
		# 获取属性值  用户  属性
			hget      user  name
			
		# 获取多个属性值
		hmget key name age
		
		# 获取所有属性的值
		hvals key
	
	删除:
		# 整个删除
		del user
		
		# 删除属性, 属性对应的值会被一起删除
		hdel user name age high

------------------------------------list类型
	1. 列表的元素类似为string
	2. 按照插入顺序排序
	
	增加：
		# 从左侧插入数据
		lpush key value1 
		
		lpush k1 a b c  ---从键为k1的列表左侧加入数据a b c 
		rpush k2 d e f  ---从键为k2的列表右侧加入数据d e f 
		
		linsert k1 before/after  现有元素 新元素 ---在指定元素的前或后插入新元素
		linsert k1 before/after a 3  ---在a的前/after插入元素3
		
	获取:
		lrange k1 start stop 
		lrange k1 0 -1 ---获取k1中存储的所有数据, -1--表示最后一个
	
	设置指定索引位置的元素值:
		1. 索引从左侧开始, 第一个元素为0
		2. 索引可以是负数, 表示尾部开始计数, -1--表示最后一个元素
		
		# 修改键
		      键   下标  修改的值
		lset  k1     1       z
		
	删除:
		count>0   --从头往尾移除
		count<0   --从尾往头移除
		count=0   --移除所有
		# 移除元素
		     键   出现次数(1-头到尾 -1 尾到头)   移除的元素
		lrem  k2         1                             a   ---k2 中的a 从头往尾移除,删除1个
		lrem  k2         -2                            b   ----k2中的b 从尾往头,移除2个
	
	
------------------------------------------set类型
1. 无序集合
2. 元素为string类型
3. 元素具有唯一性, 不重复
4. 集合没有修改操作

	增加:
		# 添加元素
		sadd key member1 member2...
		
		# 获取元素
		smembers key
		
	删除:
		# 删除指定元素
		srem key member1 member2
		
---------------------------------------zset类型
1. sorted set, 有序集合
2. 元素为string类型
3. 元素具有唯一性, 不重复
4. 每个元素都会关联一个double类型的score,表示权重,通过权重将元素从小到大排序
5. 没有修改操作

	增加：
		# 添加
		zadd key score1 member1 score2 member2
		# 向k3的集合中添加元素lisi zs ww zliu 权重分别是4, 5, 6, 3
		zadd k3 4 lisi 5 ww 6 zliu  3 zhansan
		
	获取:
	1. 0开始,索引可以为负数, -1 表示最后一个元素
	2. 返回指定范围内的元素
		
		# 获取   键  起始索引  结束索引
		zrange   k3     0         -1 
		
		# 返回score(权重)值在min和max之间的成员
		zrangebyscore key  min max
		zrangebyscore k2 5    6 
		
		# 返回member的score(权重)值
		zscore key zs
		zscore k3  zs
		
	删除:
		# 删除指定元素
		zrem key member1 member2
		zrem k3 zs lisi
		
		# 删除权重在指定范围的元素
		zremrangebyscore key min max 
		zremrangebyscore k3 5 6 
		
5. 与Python交互
	from redis import StrictRedis
	# 创建redis连接对象
	sr = StrictRedis(host='redis服务器主机IP', port='端口号', db=0)
	# 默认
	sr = StrictRedis(host='127.0.0.1', port=6379, db=0)
	
	1. string类型连接是返回值
		[b 'name']  ---b表示以二进制存储
		
		
----------------------------session的redis存储配置
		1. 安装
			pip install django-redis-sessions==0.5.6
			注意：
				1. 直接在项目下面安装
				2. 安装版本0.5.6,其他版本可能出错
				
				
		2. Django项目中setting.py配置
			
			sesson存储服务器设置:
				SESSION_ENGINE = 'redis_sessions.session'
				# 地址设置
				SESSION_REDIS_HOST = 'localhost'
				# 端口设置
				SESSION_REDIS_PORT = 6379
				# 数据库选择
				SESSION_REDIS_DB = 2
				SESSION_REDIS_PASSWORD = ''
				SESSION_REDIS_PREFIX = 'session'
		
		3. 设置完成后,用户提交的session信息回存储到redis数据库中的2号数据库中.
		


6. 搭建主从(master -- slave)
	1. 一个master可以拥有多个slave
	2. master用来写数据,slave用来读数据
	3.通过主从配置实现读写分离(主--写存数据, 从--服务器读数据)
	

-------------------------主从配置
		1. 主服务器配置:
			1. 打开配置文件目录redis
				cd /etc/redis
			
			2. 修改配置文件
				sudo vi redis.conf
				 bind     本机ip     
		   like: bind 192.168.26.128 
		
		2. 从属服务器配置
			1. 复制配置文件
				sudo cp redis.conf ./slave.conf
			2. 修改slave.conf
				bind 192.168.26.128 
				slaveof 192.168.26.128 6379  ---在211行
				port 6380
			3. slave启动服务
				sudo redis-server slave.conf
		
		3. 查看主从关系
			redis-cli -h 192.168.26.128 info Replication
				
		 
		4. 进入主从服务
			主: redis-cli -h 192.168.26.128 -p 6379
			从: redis-cli -h 192.168.26.128 -p 6378
			
-------------------------------------------------------------搭建集群
网络参考:
	redis集群搭建 http://www.cnblogs.com/wuxl360/p/5920330.html
	[Python]搭建redis集群 http://blog.5ibc.net/p/51020.html

	
	1. 集群意思就是在服务器部署的时配置了多个主从服务

	2. redis集群: 一组redis服务共同对外提供服务.
	
	3. 集群
		1. 软件层面 --软件部署多个
		2. 硬件层面 --多台实体电脑
	
	
------------------------------两个不同系统间搭建redis集群
	4. redis集群的搭建
		4.1 搭建两个系统
			系统一: 192.168.177.130
				1. 创建文件夹: redis_test
					Desktop目录下: mkdir redis_test
					
				2. 添加配置文件
					cd redis_test
					vi 7000.conf
					
				3. 添加内容三组conf配置文件:
					 7000.conf 7001.conf 7002.conf
					 区别: port、pidfile、cluster-config-file三项
					 配置文件添加的内容:
							port 7000/7001/7002
							bind 172.16.179.130
							daemonize yes
							pidfile 7000.pid/7001.pid/7002.pid
							cluster-enabled yes
							cluster-config-file 7000_node.conf/7001_node.conf/7002_node.conf
							cluster-node-timeout 15000
							appendonly yes
			
			配置系统二:192.168.177.131
				1. 同系统一配置, 创建文件7003.conf/7004.conf/7005.conf  
		
		4.2 配置将两个系统中的redis全部启动:
			sudo redis-server ./7000.conf
		
	!!!!4.3 创建集群
			1. redis安装包包含了redis-trib.rb, 用于创建集群
				将该命令复制到bin目录下后可以在任何目录中调用此命令
				sudo cp /usr/share/doc/redis-tools/examples/redis-trib.rb /usr/local/bin/    ----使用的Ubuntu系统已经配置OK
			
			2. 安装ruby环境,  redis-trib.rb是用ruby开发的
				1. sudo apt-get install ruby
				2. ruby不是最新版本报错时解决办法:
					-- 先查看自己的gem 源是什么地址
						gem source -l -- 如果是https://rubygems.org/ 就需要更换
					
					-- 更换指令为
						gem sources --add https://gems.ruby-china.org/ --remove https://rubygems.org/
					
					-- 通过 gem 安装 redis 的相关依赖
						sudo gem install redis
					-- 然后重新执行创建集群指令
			
			3. 创建集群
				格式: redis-trib.rb create --replicas 数字 IP+PORT(创建的所有配置文件)
				
				
				redis-trib.rb create --replicas 1 192.168.177.133:7000 192.168.177.133:7001 192.168.177.133:7002 192.168.177.135:7003 192.168.177.135:7004 192.168.177.135:7005
				
				
				node ---节点
				[OK]ALL 16384 slots covered  ----集群搭建成功
			


			
		4.4 数据验证
			1. 根据M标识查看主服务器有:7000 7001 7003    ---主节点
			   根据S标识查看从服务器有:7004 7005 7002   ---从节点
			2. 主从关系一组: replicas 1 
			
			
			
			3. 在192.168.177.131机器上连接7002, -c表示连接到集群
				!!!集群主节点间相互发送信息!!!
				
				# 建立连接
				redis-cli -h 192.168.177.131 -c -p 7002
				
				# 写入数据 ---自动跳到了7003服务器,并写入成功
				set name itcast
				
				# 7003可以获取数据, 写入又重定向到7000(负载均衡)
		

		
		4.5 redis cluster去中心化
			1. 节点中每个节点都是平等的关系,都是对等的
			
			2. 每个节点都保存各自的数据和整个集群的状态
			
			3. redis集群分配数据采用的是--哈希槽(hash slot)的方式来分配
			
			4. redis cluster 默认16384个槽,当我们 set口个key 时，会?CRC16算法来取模得到所属的slot，
			   然后将这个key 分到哈 希槽区间的节点上，具体算法就是：CRC16(key) % 16384。
			   所以我们在测试的 时候看到set 和 get 的时候，直接跳转到了7000端口的节点
			
			5. 当一个master挂掉之后，才会启动一个对应的salve节点，充当master
			
			6. 集群必须要3个或以上的主节点,当存活的主节点数小于总节点数的一半时，整个集群就无法提供服务
			
				
		4.6 与python的交互
			1. 配置包 pip install redis-py-cluster
			
			2. 创建redis_cluster.py文件
				from rediscluster import StrictRedisCluster
				if __name__ == '__main__':
				  try:
					  # 构建所有的节点，Redis会使?CRC16算法，将键和值写到某个节点上
					  startup_nodes = [
						  {'host': '192.168.26.128', 'port': '7000'},
						  {'host': '192.168.26.130', 'port': '7003'},
						  {'host': '192.168.26.128', 'port': '7001'},
					  ]
					  # 构建StrictRedisCluster对象
					  src=StrictRedisCluster(startup_nodes=startup_nodes,decode_responses=True)
					  # 设置键为name、值为itheima的数据
					  result=src.set('name','itheima')
					  print(result)
					  # 获取键为name
					  name = src.get('name')
					  print(name)
				  except Exception as e:
					  print(e)
			
			
			
			
			
			
		
----------------------思考
1. 常见项目会有几种数据库？	
		
server{
	listen  8888;
	server_name localhost;
	location ~ /group[0-9]/{
		ngx_fastdfs_moudle;
	}
	error_page 500 502 503 504 /50x.html;
	location = /50x.html{
		root html;
	}
}	
图书上传fdfs后ID信息:group1/M00/00/01/rBCzg1p32132dsfd.jpg与group的连接.
	