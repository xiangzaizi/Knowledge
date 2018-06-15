1. git历史

2. git两大特点：
		1. 版本控制
		2. 分布式管理
	

3. ------------------------------------------git的基本使用
	3.1 准备
		sudo apt-get install git 安装
		
	3.1 创建版本仓库:
		创建代码文件夹: mkdir git_test
		初始化仓库文件夹: git init
	
	3.2 文件版本创建
		git add 文件/目录          ---添加文件到暂存区
		git commit -m  '版本信息'  ---添加到版本库
	
	3.3 查看版本记录
		git log --pretty=oneline
		
	3.4 版本回退
		git reset --hard HEAD^ 
		---HEAD指向当前版本
		---HEAD^ 上一版本
		---HEAD^^ 上上一版本
		
		git reset --hard HEAD^  ---撤销到上一个版本
		
		
		
	or  git reset --hard 版本序列号
		git reset --hard 7893w1e
	
	3.5 查看操作记录(所有改过的版本号)
		git reflog
	
	3.6 工作区、暂存区、 版本库
		1. 编辑文件都是在工作区
		2. git add 是把工作区的修改放入暂存区
		3. git commit -m 是把暂存的区修改一次性做一次版本记录
	
	3.7 管理修改
		git commit -m 只会把暂存区的修改提交的版本记录中
	
	3.8 撤销修改
		1. 工作区中修改的内容丢弃 
			git checkout -- names
			
		2. 修改已经添加到暂存区，但没有commit的文件
			git reset HEAD name    ----退回工作区
			git checkout -- name   ----丢弃修改的内容
			----操作以上两步后文件就是原来的文件了
		
		3. 已经commit的文件
			git reset --hard HEAD^ ---可回撤到指定版本
			
			
	3.9 对比文件的不同
		1. 对比工作区和版本库某个文件
			git diff HEAD -- 文件
		
		2. 对比两个版本中的文件
			git diff HEAD HEAD^ -- 文件
	
	3.10 删除文件
		1. rm name -r ---慎用
		
		2. git rm name   ---删除工作区文件?
		   git commit -m '删除文件code.txt'  ---确认删除,更新版本库,从版本库删除

		3. git status 查看工作树的状态,可以看到删除的文件
		   注意: 没有 git commit -m '删除文件code.txt'文件可以 git checkout -- name ---恢复文件 

		
		
			
		
		
		
	


4. -------------------------------------------------git分支管理:
	4.1 分支操作的基本命令
		查看分支: git branch
		
		创建分支:  git branch name
				   git branch dev
				   
		切换分支: git checkout  name
		
		创建 + 切换分支: git checkout -b name 
		
		合并分支到当前分支: git merge name
			注意: 1. 合并分之内容需要先提交版本
			      2. 切换到master后执行分支内容合并
			      3. 删除分支
		
		删除分支: git branch -d name
		
	4.2 分支冲突
		两个分支都有了新的提交记录并且修改的是同一个文件
		解决办法: 1. vi code.txt  打开后删除多余内容
			  2. git add code.txt   git commit -m '新版本code'
			  3. git merge dev ---执行合并
			  4. 删除分支
				
	
	4.3 分支管理策略
		1. 合并的时候, 如果可以,执行的快速合并
		2. 禁止快速合并   --on-off
			1. 分支: dev  修改提交文件
			2. 主支: git merge --no-ff -m '禁用分支模式' dev ---禁止快速合并格式 
			3. 删除分支
		
	4.3 Bug分支
		1. git stash  ---隐藏当时工作现场
		2. 切换到bug所在分支,并创建并切换到一个临时分支,修复bug
		3. 修复完bug之后,切换回bug分支并合并临时分支的内容,合并使用on-off模式
		4. 删除临时分支
		5. 切换回工作分支
		6. git stash pop
	
		
5. -------------------------------github使用	
	1. 创建仓库
	2. 添加ssh公钥
		用户目录下：
			vi .gitconfig   添加邮箱+github用户名
			
		生成ssh密钥：ssh-keygen -t rsa -C 'skyxiang.jiang@gmail.com'
		用户目录下取密钥: 
			cd .ssh：id_rsa  id_rsa.pub  known_hosts
			cat id_rsa.pub  
			
	3. 项目克隆：
		git clone git@github.com:xiangzaizi/sz07.git
		
		修改文件权限: chmod 644 name
					r-4  w-2 x-1   ---- 644  rw   r  r 
					664  --文件可修改   rw  rw r
		
		克隆项目出错:(百度一下错误)
					  eval "$(ssh-agent -s)"
					  ssh-add

	4. 推送分支代码:
		git push origin(远程主机)  master(分支名)/dev(分支名)
	
	5. 跟踪远程分支:
		git branch --set-upstream-to=orgin/dev dev
	
	6. 拉取远程分支代码:
		git pull orgin master
	
	查看分支：git branch
	创建分支：git branch <name>
	切换分支：git checkout <name>
	创建+切换分支：git checkout -b <name>
	合并某分支到当前分支：git merge <name>
	删除分支：git branch -d <name>

		
		
---------------实际步骤:
1. 修改ubuntu下面的or 新建 .gitconfig文件：
	# 用户名和密码
	 [user]
        email = skyxiang.jiang@hotmail.com
        name = xiangzaizi
2. 生成密钥文件:
	ssh-keygen -t rsa -C 'skyxiang.jiang@gmail.com'
	直接回车在.ssh下面生成了两个文件: id_rsa  id_rsa.pub 

3.  vi id_rsa.pub 文件复制该内容.

4.  上github 在Persoal settings位置-->打开SSH and GPG keys

5.  SSH keys  ---> New SSH key
	将这个key添加上去.

6. 克隆项目: 
	git clone git@github.com:xiangzaizi/sz07.git
	git clone git https://github.com/xiangzaizi/sz07.git
		
	eval "$(ssh-agent -s)"
	ssh-add
	
	新项目:
	1. 在github上面新建一个项目文件: dailyfresh
	
	2. 本地连接:git remote add origin git@github.com:xiangzaizi/dailyfresh.git
	
	3. git pull origin master --->把项目从github上面拉下来
		中间内容: git add test01.py
				  git commit -m '增加test01文件'
		
	4. git push origin master --->将项目推上去
	
	
		sudo redis-server redis_ihome.conf
		redis-cli -h '192.168.177.140' -p '6381' 
		
		

	
	
	
	
	
	
	
	
