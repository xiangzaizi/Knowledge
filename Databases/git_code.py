1. git��ʷ

2. git�����ص㣺
		1. �汾����
		2. �ֲ�ʽ����
	

3. ------------------------------------------git�Ļ���ʹ��
	3.1 ׼��
		sudo apt-get install git ��װ
		
	3.1 �����汾�ֿ�:
		���������ļ���: mkdir git_test
		��ʼ���ֿ��ļ���: git init
	
	3.2 �ļ��汾����
		git add �ļ�/Ŀ¼          ---����ļ����ݴ���
		git commit -m  '�汾��Ϣ'  ---��ӵ��汾��
	
	3.3 �鿴�汾��¼
		git log --pretty=oneline
		
	3.4 �汾����
		git reset --hard HEAD^ 
		---HEADָ��ǰ�汾
		---HEAD^ ��һ�汾
		---HEAD^^ ����һ�汾
		
		git reset --hard HEAD^  ---��������һ���汾
		
		
		
	or  git reset --hard �汾���к�
		git reset --hard 7893w1e
	
	3.5 �鿴������¼(���иĹ��İ汾��)
		git reflog
	
	3.6 ���������ݴ����� �汾��
		1. �༭�ļ������ڹ�����
		2. git add �ǰѹ��������޸ķ����ݴ���
		3. git commit -m �ǰ��ݴ�����޸�һ������һ�ΰ汾��¼
	
	3.7 �����޸�
		git commit -m ֻ����ݴ������޸��ύ�İ汾��¼��
	
	3.8 �����޸�
		1. ���������޸ĵ����ݶ��� 
			git checkout -- names
			
		2. �޸��Ѿ���ӵ��ݴ�������û��commit���ļ�
			git reset HEAD name    ----�˻ع�����
			git checkout -- name   ----�����޸ĵ�����
			----���������������ļ�����ԭ�����ļ���
		
		3. �Ѿ�commit���ļ�
			git reset --hard HEAD^ ---�ɻس���ָ���汾
			
			
	3.9 �Ա��ļ��Ĳ�ͬ
		1. �Աȹ������Ͱ汾��ĳ���ļ�
			git diff HEAD -- �ļ�
		
		2. �Ա������汾�е��ļ�
			git diff HEAD HEAD^ -- �ļ�
	
	3.10 ɾ���ļ�
		1. rm name -r ---����
		
		2. git rm name   ---ɾ���������ļ�?
		   git commit -m 'ɾ���ļ�code.txt'  ---ȷ��ɾ��,���°汾��,�Ӱ汾��ɾ��

		3. git status �鿴��������״̬,���Կ���ɾ�����ļ�
		   ע��: û�� git commit -m 'ɾ���ļ�code.txt'�ļ����� git checkout -- name ---�ָ��ļ� 

		
		
			
		
		
		
	


4. -------------------------------------------------git��֧����:
	4.1 ��֧�����Ļ�������
		�鿴��֧: git branch
		
		������֧:  git branch name
				   git branch dev
				   
		�л���֧: git checkout  name
		
		���� + �л���֧: git checkout -b name 
		
		�ϲ���֧����ǰ��֧: git merge name
			ע��: 1. �ϲ���֮������Ҫ���ύ�汾
			      2. �л���master��ִ�з�֧���ݺϲ�
			      3. ɾ����֧
		
		ɾ����֧: git branch -d name
		
	4.2 ��֧��ͻ
		������֧�������µ��ύ��¼�����޸ĵ���ͬһ���ļ�
		����취: 1. vi code.txt  �򿪺�ɾ����������
			  2. git add code.txt   git commit -m '�°汾code'
			  3. git merge dev ---ִ�кϲ�
			  4. ɾ����֧
				
	
	4.3 ��֧�������
		1. �ϲ���ʱ��, �������,ִ�еĿ��ٺϲ�
		2. ��ֹ���ٺϲ�   --on-off
			1. ��֧: dev  �޸��ύ�ļ�
			2. ��֧: git merge --no-ff -m '���÷�֧ģʽ' dev ---��ֹ���ٺϲ���ʽ 
			3. ɾ����֧
		
	4.3 Bug��֧
		1. git stash  ---���ص�ʱ�����ֳ�
		2. �л���bug���ڷ�֧,���������л���һ����ʱ��֧,�޸�bug
		3. �޸���bug֮��,�л���bug��֧���ϲ���ʱ��֧������,�ϲ�ʹ��on-offģʽ
		4. ɾ����ʱ��֧
		5. �л��ع�����֧
		6. git stash pop
	
		
5. -------------------------------githubʹ��	
	1. �����ֿ�
	2. ���ssh��Կ
		�û�Ŀ¼�£�
			vi .gitconfig   �������+github�û���
			
		����ssh��Կ��ssh-keygen -t rsa -C 'skyxiang.jiang@gmail.com'
		�û�Ŀ¼��ȡ��Կ: 
			cd .ssh��id_rsa  id_rsa.pub  known_hosts
			cat id_rsa.pub  
			
	3. ��Ŀ��¡��
		git clone git@github.com:xiangzaizi/sz07.git
		
		�޸��ļ�Ȩ��: chmod 644 name
					r-4  w-2 x-1   ---- 644  rw   r  r 
					664  --�ļ����޸�   rw  rw r
		
		��¡��Ŀ����:(�ٶ�һ�´���)
					  eval "$(ssh-agent -s)"
					  ssh-add

	4. ���ͷ�֧����:
		git push origin(Զ������)  master(��֧��)/dev(��֧��)
	
	5. ����Զ�̷�֧:
		git branch --set-upstream-to=orgin/dev dev
	
	6. ��ȡԶ�̷�֧����:
		git pull orgin master
	
	�鿴��֧��git branch
	������֧��git branch <name>
	�л���֧��git checkout <name>
	����+�л���֧��git checkout -b <name>
	�ϲ�ĳ��֧����ǰ��֧��git merge <name>
	ɾ����֧��git branch -d <name>

		
		
---------------ʵ�ʲ���:
1. �޸�ubuntu�����or �½� .gitconfig�ļ���
	# �û���������
	 [user]
        email = skyxiang.jiang@hotmail.com
        name = xiangzaizi
2. ������Կ�ļ�:
	ssh-keygen -t rsa -C 'skyxiang.jiang@gmail.com'
	ֱ�ӻس���.ssh���������������ļ�: id_rsa  id_rsa.pub 

3.  vi id_rsa.pub �ļ����Ƹ�����.

4.  ��github ��Persoal settingsλ��-->��SSH and GPG keys

5.  SSH keys  ---> New SSH key
	�����key�����ȥ.

6. ��¡��Ŀ: 
	git clone git@github.com:xiangzaizi/sz07.git
	git clone git https://github.com/xiangzaizi/sz07.git
		
	eval "$(ssh-agent -s)"
	ssh-add
	
	����Ŀ:
	1. ��github�����½�һ����Ŀ�ļ�: dailyfresh
	
	2. ��������:git remote add origin git@github.com:xiangzaizi/dailyfresh.git
	
	3. git pull origin master --->����Ŀ��github����������
		�м�����: git add test01.py
				  git commit -m '����test01�ļ�'
		
	4. git push origin master --->����Ŀ����ȥ
	
	
		sudo redis-server redis_ihome.conf
		redis-cli -h '192.168.177.140' -p '6381' 
		
		

	
	
	
	
	
	
	
	
