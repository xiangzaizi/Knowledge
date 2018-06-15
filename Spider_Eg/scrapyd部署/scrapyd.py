Scrapyd 远程部署和监控:

1. pip install scrapyd  # 服务端
   pip install scrapyd-client  # 客户端
   
2. 在服务器端启动scrapyd服务
   相当于一个本地的web服务器, port=6800
3. scrapyd # 启动访问: 127.0.0.1:6800
 
4. 部署项目:
	1) 修改scrapy.cfg配置文件
		# 1. 添加scrapyd配置名
		[deploy:scrapyd_Douyu]  # 配置名称
		# 2. 服务在那个IP地址启动就是这个IP
		url = http://localhost:6800/  
	2)部署:
	scrapyd-deloy scrapyd_Douyu -p Douyu
	
	3)项目启动:
	curl http://localhost:6800/schedule.json -d project=Douyu -d spider=douyu
	注意: 记住jobid
	
	停止爬虫:curl http://localhost:6800/cancel.json -d project=Douyu -d job=366781fa6d4d11e8b9be000c29219f36
	删除爬虫:curl http://localhost:6800/delproject.json-d project=Douyu
	
5. 新版本scrapyd配置文件, 第五版本的scrapyd
	查看源码site-packages-->scrapyd文件
	vi default_scrapyd.conf 文件可查看配置信息
	****使用时一定要将bind_address改成:bind_address = 0.0.0.0
	
6. 用scrapyd服务器管理爬虫，至少有以下几个优势：
	1.可以避免爬虫源码被看到
	2.有版本控制
	3.可以远程启动、停止、删除，正是因为这一点，所以scrapyd也是分布式爬虫的解决方案之一

7. 多服务器部署:
	1)配置
	[deploy:scrapyd_1]  
	url = http://127.0.0.1:6800/ 
	project = Renren
	
	[deploy:scrapyd_2]  
	url = http://127.0.0.2:6800/
	project = Renren
	
	[deploy:scrapyd_3]
	url = http://127.0.0.3:6800/
	project = Renren
	
	2)部署:
	scrapyd-deloy scrapyd_1 -p Renren
	3)执行：
	curl http://127.0.0.1:6800/schdeule.json -d project=Renren -d spider=renren
	
