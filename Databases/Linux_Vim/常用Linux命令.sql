1.command --help  查看命令的帮助信息
2.man command  查阅 command 命令的使用手册
3.ls --查看目录   ll  查看所有的文件包括隐藏目录 or ls –lah 
- l 列表形式显示  -h 显示大小 kb  - a 显示隐藏文件
4.clear  清除内容 or “ctrl+l”
5.cd  切换目录
6.pwd  当前目录绝对路径
7.mkdir  创建文件夹 or递归的创建 如: mkdir a/b/c/d/ -p  
8.touch  创建文件
9. rm  删除文件 文件的删除是不可恢复的
9.1 rm file.txt    rm 文件夹 -r(删除文件以及内容) /-d 删除控文件
9.2 -i --以交互的形式执行会提醒是否删除
9.3 -f --强制删除
9.4 -r --强制删除文件夹

10.cp 复制文件
当前目录直接复制格式：cp file.txt 复件-file.txt
跨目录复制文件：--权限不够的时候使用 sudo  cp abcd.txt /opt
cp -r  a.txt  ./b/e  e 文件中还有f 所以添加-r命令会直接递归复制
-r  递归复制该目录下的所有子目录和文件  如: cp -r ./A ./B/
	
11.mv 移动文件
移动文件: mv file.txt  /移动的文件位置
mv hello a   直接移动将hello文件移动到a 文件夹内

12.tree 树形结构查看目录
13.chmod  修改权限
-------chmod u+r/w/x  test.txt  给test文件添加 r/w/x的权限
+ 增加权限  - 撤销权限  = 设定权限
u 文件所有者 
g 同属一组的group组者，即用户组
o   表示other以外的其他人

a  表示以上三者介是
r 读取权限  数字代号4
w 写入权限 数字代号2
x 执行权限 数字代号1
-不具有任何权限，数字代号0
----------如执行：chmod u=rwx,g=rx,o=r filename 就等同于：chmod u=7,g=5,o=4 filename
14.find  查找文件  
find *.py  查找  .py文件   ？

15.grep 查找文件中的文本
grep  "q"    a.txt  ---查找a.txt文件中的有“q”的内容
grep "^q.r"  a.txt  ---查找a.txt文件中以q开始(.)到r之间的字符
grep "r$" a.txt   ---查找以a.txt中以r结尾的字符
-n  显示行号  
-i 忽略大小写
grep是一种强大的文件搜索工具，查找文件里符合条件的字符串
--重要:
gedit file.txt  直接打开文件进行编辑
打开浏览器： /opt 切换到需要打开的软件的文件夹内，然后./chrome
16.重定向  > 
1.ls >file.txt   将当前终端的文件保存到指定的file文件中
将本应显示在终端上的文件保存到指定文件内
2.cat中
cat file1.txt file2.txt > file.txt  将 1 2 内容定向到3文件内
cat test1.txt > file.txt  表示先清空后添加
cat test1.txt >> file.txt  表示直接添加
17. 软连接、硬链接  ln
ln -s file.txt file_softlink.txt   立刻快捷方式
ln file.txt file_hardlink.txt  硬链接，同一个文件的不同引用名
18.管道 |
		如 ls | grep “.py” --显示该目录下以py结尾的文件
		ls | more      ls | tree
19.分屏显示 more
18.压缩  tar gzip bzip2 
将文件添加到文件包中:
tar -cvf A.tar A    压缩  tar -zcvf A.gz A

tar  -xvf  file.tar  解压  tar -zxvf A.gz
将包中文件压缩tar.gz格式
gzip -r  file.tar  file.tar.gz   压缩
gzip -d   file.tar.gz   解压
文件直接进包—压缩
tar -zcvf test.tar.gz *.txt单独*就是全部文件都压缩，or指定压缩目录文件中的--.txt
tar -zxvf  test.tar.gz解压
tar -zxvf  test.tar.gz  -C file/ 解压到指定文件夹   -C
其他:
tar -jcvf test.tar .txt
zip fzip *.zip  压缩包  
unzip -d b fzip.zip  将fzip文件解压 到b目录下
19．shutdown  关机 reboot 重启 exit 退出当前账户
20.who  查看当前用户    passwd 设置用户密码
21.sudo 权限  password 直接修改当前用户密码
22.su root 进入后 #超级管理员时password修改的是unix密码
现在虚拟机中ubuntu 中的管理员密码是itcast
--补充快捷键
1.打开终端 ctrl+Alt+t 
2.赋值文件到桌面:cp ./A/B/C/a.txt ~/Desktop/
3.rm 可以删除文件夹和目录(删除非空必须加上-r)
4. mkdir 创建目录  rmdir删除目录(只能删空的目录)
5. tree A   查看A文件目录的结构
6.find –name “*.txt 在指定目录中搜索文件”
7.man ps --??
8.ls /usr/local/bin/p*  查看该目录下以p开头的文件(文件夹)
--重定向和管道的区别
管道:tree --help|grep "p"  读取 help树下的p的文件
重定向:1.sudo ls /usr/local/bin/p* >  ~/Desktop/C/1.txt or 2.ls > f.txt  将查看的信息保存在指定文件内
3.cat 1.txt 2.txt > result.txt 将1 2中的内容写入到3.txt中，前提存在3.
4.grep "m" test3/1.txt > test3/2.txt 将1中含有的m一行数据存到2中

1.重定向是将前面运行命令的记过输入到后面的文件B    ls > a.txt (当前目录信息存储到a.txt)
2.管道功能是把前面命令运行的结果作为后面命令的输入

主要区别：>后面是一个文件名   |后面是一个命令





