1.command --help  �鿴����İ�����Ϣ
2.man command  ���� command �����ʹ���ֲ�
3.ls --�鿴Ŀ¼   ll  �鿴���е��ļ���������Ŀ¼ or ls �Clah 
- l �б���ʽ��ʾ  -h ��ʾ��С kb  - a ��ʾ�����ļ�
4.clear  ������� or ��ctrl+l��
5.cd  �л�Ŀ¼
6.pwd  ��ǰĿ¼����·��
7.mkdir  �����ļ��� or�ݹ�Ĵ��� ��: mkdir a/b/c/d/ -p  
8.touch  �����ļ�
9. rm  ɾ���ļ� �ļ���ɾ���ǲ��ɻָ���
9.1 rm file.txt    rm �ļ��� -r(ɾ���ļ��Լ�����) /-d ɾ�����ļ�
9.2 -i --�Խ�������ʽִ�л������Ƿ�ɾ��
9.3 -f --ǿ��ɾ��
9.4 -r --ǿ��ɾ���ļ���

10.cp �����ļ�
��ǰĿ¼ֱ�Ӹ��Ƹ�ʽ��cp file.txt ����-file.txt
��Ŀ¼�����ļ���--Ȩ�޲�����ʱ��ʹ�� sudo  cp abcd.txt /opt
cp -r  a.txt  ./b/e  e �ļ��л���f �������-r�����ֱ�ӵݹ鸴��
-r  �ݹ鸴�Ƹ�Ŀ¼�µ�������Ŀ¼���ļ�  ��: cp -r ./A ./B/
	
11.mv �ƶ��ļ�
�ƶ��ļ�: mv file.txt  /�ƶ����ļ�λ��
mv hello a   ֱ���ƶ���hello�ļ��ƶ���a �ļ�����

12.tree ���νṹ�鿴Ŀ¼
13.chmod  �޸�Ȩ��
-------chmod u+r/w/x  test.txt  ��test�ļ���� r/w/x��Ȩ��
+ ����Ȩ��  - ����Ȩ��  = �趨Ȩ��
u �ļ������� 
g ͬ��һ���group���ߣ����û���
o   ��ʾother�����������

a  ��ʾ�������߽���
r ��ȡȨ��  ���ִ���4
w д��Ȩ�� ���ִ���2
x ִ��Ȩ�� ���ִ���1
-�������κ�Ȩ�ޣ����ִ���0
----------��ִ�У�chmod u=rwx,g=rx,o=r filename �͵�ͬ�ڣ�chmod u=7,g=5,o=4 filename
14.find  �����ļ�  
find *.py  ����  .py�ļ�   ��

15.grep �����ļ��е��ı�
grep  "q"    a.txt  ---����a.txt�ļ��е��С�q��������
grep "^q.r"  a.txt  ---����a.txt�ļ�����q��ʼ(.)��r֮����ַ�
grep "r$" a.txt   ---������a.txt����r��β���ַ�
-n  ��ʾ�к�  
-i ���Դ�Сд
grep��һ��ǿ����ļ��������ߣ������ļ�������������ַ���
--��Ҫ:
gedit file.txt  ֱ�Ӵ��ļ����б༭
��������� /opt �л�����Ҫ�򿪵�������ļ����ڣ�Ȼ��./chrome
16.�ض���  > 
1.ls >file.txt   ����ǰ�ն˵��ļ����浽ָ����file�ļ���
����Ӧ��ʾ���ն��ϵ��ļ����浽ָ���ļ���
2.cat��
cat file1.txt file2.txt > file.txt  �� 1 2 ���ݶ���3�ļ���
cat test1.txt > file.txt  ��ʾ����պ����
cat test1.txt >> file.txt  ��ʾֱ�����
17. �����ӡ�Ӳ����  ln
ln -s file.txt file_softlink.txt   ���̿�ݷ�ʽ
ln file.txt file_hardlink.txt  Ӳ���ӣ�ͬһ���ļ��Ĳ�ͬ������
18.�ܵ� |
		�� ls | grep ��.py�� --��ʾ��Ŀ¼����py��β���ļ�
		ls | more      ls | tree
19.������ʾ more
18.ѹ��  tar gzip bzip2 
���ļ���ӵ��ļ�����:
tar -cvf A.tar A    ѹ��  tar -zcvf A.gz A

tar  -xvf  file.tar  ��ѹ  tar -zxvf A.gz
�������ļ�ѹ��tar.gz��ʽ
gzip -r  file.tar  file.tar.gz   ѹ��
gzip -d   file.tar.gz   ��ѹ
�ļ�ֱ�ӽ�����ѹ��
tar -zcvf test.tar.gz *.txt����*����ȫ���ļ���ѹ����orָ��ѹ��Ŀ¼�ļ��е�--.txt
tar -zxvf  test.tar.gz��ѹ
tar -zxvf  test.tar.gz  -C file/ ��ѹ��ָ���ļ���   -C
����:
tar -jcvf test.tar .txt
zip fzip *.zip  ѹ����  
unzip -d b fzip.zip  ��fzip�ļ���ѹ ��bĿ¼��
19��shutdown  �ػ� reboot ���� exit �˳���ǰ�˻�
20.who  �鿴��ǰ�û�    passwd �����û�����
21.sudo Ȩ��  password ֱ���޸ĵ�ǰ�û�����
22.su root ����� #��������Աʱpassword�޸ĵ���unix����
�����������ubuntu �еĹ���Ա������itcast
--�����ݼ�
1.���ն� ctrl+Alt+t 
2.��ֵ�ļ�������:cp ./A/B/C/a.txt ~/Desktop/
3.rm ����ɾ���ļ��к�Ŀ¼(ɾ���ǿձ������-r)
4. mkdir ����Ŀ¼  rmdirɾ��Ŀ¼(ֻ��ɾ�յ�Ŀ¼)
5. tree A   �鿴A�ļ�Ŀ¼�Ľṹ
6.find �Cname ��*.txt ��ָ��Ŀ¼�������ļ���
7.man ps --??
8.ls /usr/local/bin/p*  �鿴��Ŀ¼����p��ͷ���ļ�(�ļ���)
--�ض���͹ܵ�������
�ܵ�:tree --help|grep "p"  ��ȡ help���µ�p���ļ�
�ض���:1.sudo ls /usr/local/bin/p* >  ~/Desktop/C/1.txt or 2.ls > f.txt  ���鿴����Ϣ������ָ���ļ���
3.cat 1.txt 2.txt > result.txt ��1 2�е�����д�뵽3.txt�У�ǰ�����3.
4.grep "m" test3/1.txt > test3/2.txt ��1�к��е�mһ�����ݴ浽2��

1.�ض����ǽ�ǰ����������ļǹ����뵽������ļ�B    ls > a.txt (��ǰĿ¼��Ϣ�洢��a.txt)
2.�ܵ������ǰ�ǰ���������еĽ����Ϊ�������������

��Ҫ����>������һ���ļ���   |������һ������





