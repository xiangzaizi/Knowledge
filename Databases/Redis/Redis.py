-----------------Redis kev-value ���ݿ�
NoSQL ---һ���³��ֵ����ݿ�
	1. ��֧��SQL�﷨
	2. nosql�洢�����ݶ���KV��ʽ
	3. NoSQL����: Mongodb, Redis, Hbase hadoop, Cassandra hadoop

NoSQL��SQL�Ƚϣ�
	1. ���ó�����ͬ��sql���ݿ��ʺ����ڹ�ϵ�ر��ӵ����ݲ�ѯ������nosql��֮
	2. ���������Ե�֧�֣�sql�������֧�ַǳ����ƣ���nosql������֧������
	
redisӦ�ó�����
		1. ����������
		2. �����ͳ���ݿ�---�罻��Ӧ��
		3. session�������ﳵ
		
1. ��װ

2. ��������ѡ��
	����redis.conf
	sudo vi /etc/redis/redis.conf
	redis������Ϣ�ο�: http://blog.csdn.net/ljphilp/article/details/52934933
	
	1. ��ip�� Զ�̷���: ע�� bind 127.0.0.1
	2. �˿ڣ�Ĭ��6379
	3. �Ƿ��ػ���������
		daemonize yes
		�ػ�����,�����������������֮����ֹ�����.
	
	4. �����ļ�   dbfiedname dump.rdb 
	5. �����ļ��洢·�� dir/ var/lib/redis
	6. ��־�ļ� logfile /var/log/redis/redis-server.log     ---163
	7. ���ݿ�,Ĭ����16�� database 16  						
	8. ���Ӹ���, ������˫������  slaveof      ----��211��
 	
	
3. ����˺Ϳͻ���
	������������: redis -server
	 ����: sudo service redis start
	 ֹͣ: sudo service redis stop 
	 ����: sudo service redis restart
	 
	!!!����:
		ps aux |grep redis �鿴redis����������
		
		ֹͣ: sudo kill -9 pid ɱ��redis������
			  ��: sudo kill -9 3782
			  
		����: sudo redis-server   /etc/redis/redis.conf ָ�����ص������ļ�
		
	!!!�ͻ�������:
		1. ����: redis-cli
			like :redis-cli -h '192.168.177.140' -p '6381'   
			redis-cli --help ---���Կ���h ��p��Ĭ�ϵľͲ���д.
		
		2. ��������: ping
		
		3. �л����ݿ�:select 10  (���ݿ�û������,Ĭ��16��,ͨ��0-15����ʶ)
		
		4. redis-li�е�16�����ݿ��ǣ�
			1. �໥�����ݲ���Ӱ��
		

4. ���ݲ���
	1. ���ݽṹ
		1.1 redis��key-value�����ݽṹ,ÿ�����ݶ���һ����ֵ��
		1.2 �����������ַ���
		ע��:  �������ظ�
		
		1.3. ֵ����������:
			�ַ���: string
			��ϣ: hash
			�б�list
			���ϣ�set
			���򼯺�: zset
	2. ���ݲ�������Ϊ
		����
		�޸�
		��ȡ
		ɾ��
		
	flushdb���� ----�������
	flushall���� ---��������ʵ��������,��ִ���������ǰҪ����С��.


	
-----------------------------string����
	1. �����κ����ݸ�ʽ������, �����ư�ȫ
	2. �������Ϊ512M
	
	���棺
		# ����ֵ,valueû��ʱ���,�о��޸�
		set name itcast
		get name
		
		# ����ֵ������ʱ��, ����Ϊ��λ
		setex name  10 itcast
		
		# ���ö����ֵ
		mset n1 v1 n2 v2 n3 v3
		
		# ׷��ֵ
		append n1 hh
	
	��ȡ:
		# ��ȡֵ
		get key
		# ��ȡ���ֵ
		mget n1 n2 n3
	
	ɾ��:
		del key
	
redis����ο�:�ٶ�һ��


------------------------------!!!�����
		# �鿴���м�
		keys *
		
		# �鿴�����а���a�ļ�
		keys a*
		
		# �жϼ��Ƿ����, ���ڷ���1, �����ڷ���0
		exists key
		
		# �鿴����Ӧ��value������
		type key
		
		# ɾ��������Ӧ��ֵ
		del key
		del key3 key4
		
		# ���ù���ʱ��, ����Ϊ��λ, û��ָ������ʱ��,һֱ����ֱ��ʹ��delɾ��
		# ����ʱ�䷵��-1  ��ʾ��������
		expire key seconds
		
		# �鿴��Чʱ��
		ttl key
		û������ʱ��,һֱ���ڷ���-1
		
---------------------------hash����
	1. hash���ڴ洢����,����ĽṹΪ���ԡ�ֵ
	2. ֵ������Ϊstring
	
	����:
		# ���õ������Ժ�ֵ
		hset user name lisi
		# ���ö�����Ժ�ֵ
		hmset u1 name lisi age 18 high 175
	��ȡ:
		# ��ȡ����
		hkeys key
		
		# ��ȡ����ֵ  �û�  ����
			hget      user  name
			
		# ��ȡ�������ֵ
		hmget key name age
		
		# ��ȡ�������Ե�ֵ
		hvals key
	
	ɾ��:
		# ����ɾ��
		del user
		
		# ɾ������, ���Զ�Ӧ��ֵ�ᱻһ��ɾ��
		hdel user name age high

------------------------------------list����
	1. �б��Ԫ������Ϊstring
	2. ���ղ���˳������
	
	���ӣ�
		# ������������
		lpush key value1 
		
		lpush k1 a b c  ---�Ӽ�Ϊk1���б�����������a b c 
		rpush k2 d e f  ---�Ӽ�Ϊk2���б��Ҳ��������d e f 
		
		linsert k1 before/after  ����Ԫ�� ��Ԫ�� ---��ָ��Ԫ�ص�ǰ��������Ԫ��
		linsert k1 before/after a 3  ---��a��ǰ/after����Ԫ��3
		
	��ȡ:
		lrange k1 start stop 
		lrange k1 0 -1 ---��ȡk1�д洢����������, -1--��ʾ���һ��
	
	����ָ������λ�õ�Ԫ��ֵ:
		1. ��������࿪ʼ, ��һ��Ԫ��Ϊ0
		2. ���������Ǹ���, ��ʾβ����ʼ����, -1--��ʾ���һ��Ԫ��
		
		# �޸ļ�
		      ��   �±�  �޸ĵ�ֵ
		lset  k1     1       z
		
	ɾ��:
		count>0   --��ͷ��β�Ƴ�
		count<0   --��β��ͷ�Ƴ�
		count=0   --�Ƴ�����
		# �Ƴ�Ԫ��
		     ��   ���ִ���(1-ͷ��β -1 β��ͷ)   �Ƴ���Ԫ��
		lrem  k2         1                             a   ---k2 �е�a ��ͷ��β�Ƴ�,ɾ��1��
		lrem  k2         -2                            b   ----k2�е�b ��β��ͷ,�Ƴ�2��
	
	
------------------------------------------set����
1. ���򼯺�
2. Ԫ��Ϊstring����
3. Ԫ�ؾ���Ψһ��, ���ظ�
4. ����û���޸Ĳ���

	����:
		# ���Ԫ��
		sadd key member1 member2...
		
		# ��ȡԪ��
		smembers key
		
	ɾ��:
		# ɾ��ָ��Ԫ��
		srem key member1 member2
		
---------------------------------------zset����
1. sorted set, ���򼯺�
2. Ԫ��Ϊstring����
3. Ԫ�ؾ���Ψһ��, ���ظ�
4. ÿ��Ԫ�ض������һ��double���͵�score,��ʾȨ��,ͨ��Ȩ�ؽ�Ԫ�ش�С��������
5. û���޸Ĳ���

	���ӣ�
		# ���
		zadd key score1 member1 score2 member2
		# ��k3�ļ��������Ԫ��lisi zs ww zliu Ȩ�طֱ���4, 5, 6, 3
		zadd k3 4 lisi 5 ww 6 zliu  3 zhansan
		
	��ȡ:
	1. 0��ʼ,��������Ϊ����, -1 ��ʾ���һ��Ԫ��
	2. ����ָ����Χ�ڵ�Ԫ��
		
		# ��ȡ   ��  ��ʼ����  ��������
		zrange   k3     0         -1 
		
		# ����score(Ȩ��)ֵ��min��max֮��ĳ�Ա
		zrangebyscore key  min max
		zrangebyscore k2 5    6 
		
		# ����member��score(Ȩ��)ֵ
		zscore key zs
		zscore k3  zs
		
	ɾ��:
		# ɾ��ָ��Ԫ��
		zrem key member1 member2
		zrem k3 zs lisi
		
		# ɾ��Ȩ����ָ����Χ��Ԫ��
		zremrangebyscore key min max 
		zremrangebyscore k3 5 6 
		
5. ��Python����
	from redis import StrictRedis
	# ����redis���Ӷ���
	sr = StrictRedis(host='redis����������IP', port='�˿ں�', db=0)
	# Ĭ��
	sr = StrictRedis(host='127.0.0.1', port=6379, db=0)
	
	1. string���������Ƿ���ֵ
		[b 'name']  ---b��ʾ�Զ����ƴ洢
		
		
----------------------------session��redis�洢����
		1. ��װ
			pip install django-redis-sessions==0.5.6
			ע�⣺
				1. ֱ������Ŀ���氲װ
				2. ��װ�汾0.5.6,�����汾���ܳ���
				
				
		2. Django��Ŀ��setting.py����
			
			sesson�洢����������:
				SESSION_ENGINE = 'redis_sessions.session'
				# ��ַ����
				SESSION_REDIS_HOST = 'localhost'
				# �˿�����
				SESSION_REDIS_PORT = 6379
				# ���ݿ�ѡ��
				SESSION_REDIS_DB = 2
				SESSION_REDIS_PASSWORD = ''
				SESSION_REDIS_PREFIX = 'session'
		
		3. ������ɺ�,�û��ύ��session��Ϣ�ش洢��redis���ݿ��е�2�����ݿ���.
		


6. �����(master -- slave)
	1. һ��master����ӵ�ж��slave
	2. master����д����,slave����������
	3.ͨ����������ʵ�ֶ�д����(��--д������, ��--������������)
	

-------------------------��������
		1. ������������:
			1. �������ļ�Ŀ¼redis
				cd /etc/redis
			
			2. �޸������ļ�
				sudo vi redis.conf
				 bind     ����ip     
		   like: bind 192.168.26.128 
		
		2. ��������������
			1. ���������ļ�
				sudo cp redis.conf ./slave.conf
			2. �޸�slave.conf
				bind 192.168.26.128 
				slaveof 192.168.26.128 6379  ---��211��
				port 6380
			3. slave��������
				sudo redis-server slave.conf
		
		3. �鿴���ӹ�ϵ
			redis-cli -h 192.168.26.128 info Replication
				
		 
		4. �������ӷ���
			��: redis-cli -h 192.168.26.128 -p 6379
			��: redis-cli -h 192.168.26.128 -p 6378
			
-------------------------------------------------------------���Ⱥ
����ο�:
	redis��Ⱥ� http://www.cnblogs.com/wuxl360/p/5920330.html
	[Python]�redis��Ⱥ http://blog.5ibc.net/p/51020.html

	
	1. ��Ⱥ��˼�����ڷ����������ʱ�����˶�����ӷ���

	2. redis��Ⱥ: һ��redis����ͬ�����ṩ����.
	
	3. ��Ⱥ
		1. ������� --���������
		2. Ӳ������ --��̨ʵ�����
	
	
------------------------------������ͬϵͳ��redis��Ⱥ
	4. redis��Ⱥ�Ĵ
		4.1 �����ϵͳ
			ϵͳһ: 192.168.177.130
				1. �����ļ���: redis_test
					DesktopĿ¼��: mkdir redis_test
					
				2. ��������ļ�
					cd redis_test
					vi 7000.conf
					
				3. �����������conf�����ļ�:
					 7000.conf 7001.conf 7002.conf
					 ����: port��pidfile��cluster-config-file����
					 �����ļ���ӵ�����:
							port 7000/7001/7002
							bind 172.16.179.130
							daemonize yes
							pidfile 7000.pid/7001.pid/7002.pid
							cluster-enabled yes
							cluster-config-file 7000_node.conf/7001_node.conf/7002_node.conf
							cluster-node-timeout 15000
							appendonly yes
			
			����ϵͳ��:192.168.177.131
				1. ͬϵͳһ����, �����ļ�7003.conf/7004.conf/7005.conf  
		
		4.2 ���ý�����ϵͳ�е�redisȫ������:
			sudo redis-server ./7000.conf
		
	!!!!4.3 ������Ⱥ
			1. redis��װ��������redis-trib.rb, ���ڴ�����Ⱥ
				��������Ƶ�binĿ¼�º�������κ�Ŀ¼�е��ô�����
				sudo cp /usr/share/doc/redis-tools/examples/redis-trib.rb /usr/local/bin/    ----ʹ�õ�Ubuntuϵͳ�Ѿ�����OK
			
			2. ��װruby����,  redis-trib.rb����ruby������
				1. sudo apt-get install ruby
				2. ruby�������°汾����ʱ����취:
					-- �Ȳ鿴�Լ���gem Դ��ʲô��ַ
						gem source -l -- �����https://rubygems.org/ ����Ҫ����
					
					-- ����ָ��Ϊ
						gem sources --add https://gems.ruby-china.org/ --remove https://rubygems.org/
					
					-- ͨ�� gem ��װ redis ���������
						sudo gem install redis
					-- Ȼ������ִ�д�����Ⱥָ��
			
			3. ������Ⱥ
				��ʽ: redis-trib.rb create --replicas ���� IP+PORT(���������������ļ�)
				
				
				redis-trib.rb create --replicas 1 192.168.177.133:7000 192.168.177.133:7001 192.168.177.133:7002 192.168.177.135:7003 192.168.177.135:7004 192.168.177.135:7005
				
				
				node ---�ڵ�
				[OK]ALL 16384 slots covered  ----��Ⱥ��ɹ�
			


			
		4.4 ������֤
			1. ����M��ʶ�鿴����������:7000 7001 7003    ---���ڵ�
			   ����S��ʶ�鿴�ӷ�������:7004 7005 7002   ---�ӽڵ�
			2. ���ӹ�ϵһ��: replicas 1 
			
			
			
			3. ��192.168.177.131����������7002, -c��ʾ���ӵ���Ⱥ
				!!!��Ⱥ���ڵ���໥������Ϣ!!!
				
				# ��������
				redis-cli -h 192.168.177.131 -c -p 7002
				
				# д������ ---�Զ�������7003������,��д��ɹ�
				set name itcast
				
				# 7003���Ի�ȡ����, д�����ض���7000(���ؾ���)
		

		
		4.5 redis clusterȥ���Ļ�
			1. �ڵ���ÿ���ڵ㶼��ƽ�ȵĹ�ϵ,���ǶԵȵ�
			
			2. ÿ���ڵ㶼������Ե����ݺ�������Ⱥ��״̬
			
			3. redis��Ⱥ�������ݲ��õ���--��ϣ��(hash slot)�ķ�ʽ������
			
			4. redis cluster Ĭ��16384����,������ set�ڸ�key ʱ����?CRC16�㷨��ȡģ�õ�������slot��
			   Ȼ�����key �ֵ��� ϣ������Ľڵ��ϣ������㷨���ǣ�CRC16(key) % 16384��
			   ���������ڲ��Ե� ʱ�򿴵�set �� get ��ʱ��ֱ����ת����7000�˿ڵĽڵ�
			
			5. ��һ��master�ҵ�֮�󣬲Ż�����һ����Ӧ��salve�ڵ㣬�䵱master
			
			6. ��Ⱥ����Ҫ3�������ϵ����ڵ�,���������ڵ���С���ܽڵ�����һ��ʱ��������Ⱥ���޷��ṩ����
			
				
		4.6 ��python�Ľ���
			1. ���ð� pip install redis-py-cluster
			
			2. ����redis_cluster.py�ļ�
				from rediscluster import StrictRedisCluster
				if __name__ == '__main__':
				  try:
					  # �������еĽڵ㣬Redis��ʹ?CRC16�㷨��������ֵд��ĳ���ڵ���
					  startup_nodes = [
						  {'host': '192.168.26.128', 'port': '7000'},
						  {'host': '192.168.26.130', 'port': '7003'},
						  {'host': '192.168.26.128', 'port': '7001'},
					  ]
					  # ����StrictRedisCluster����
					  src=StrictRedisCluster(startup_nodes=startup_nodes,decode_responses=True)
					  # ���ü�Ϊname��ֵΪitheima������
					  result=src.set('name','itheima')
					  print(result)
					  # ��ȡ��Ϊname
					  name = src.get('name')
					  print(name)
				  except Exception as e:
					  print(e)
			
			
			
			
			
			
		
----------------------˼��
1. ������Ŀ���м������ݿ⣿	
		
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
ͼ���ϴ�fdfs��ID��Ϣ:group1/M00/00/01/rBCzg1p32132dsfd.jpg��group������.
	