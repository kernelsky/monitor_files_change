使用方法：
1．提前配置客户信息表和文件版本表  
客户表：org.txt  
客户代码 客户名称 客户邮箱 客户账号 客户密码  
A testa xxx@qq.com testa testapassword  
B testb xxx@qq.com testb testpassword  
文件版本表：version.txt  
文件名称 大版本 小版本 md5  
有度测试20200514.docx 2020 0515 aabbcc  
2．修改邮件服务器地址：Sendmail.py  
fromaddr = 'xxx@qq.com'  
password = 'password'  
3．安装python3,依赖包：watchdog  
4．启动监控 python monitor_file.py  
