#### 1.The server is not configured as slave; fix in config file or with CHANGE MASTER TO
参考答案：https://blog.csdn.net/l1028386804/article/details/48413681

解决问题中的方法：
查看容器中数据库的日志：
位置：/var/log/mysqld.log
报错内容为：[ERROR] Server id not set, will not start slave

show variables like 'server_id';


查看允许连接mysql的服务器有哪些，在mysql中执行：
user mysql
select * from user\G



### 修改已经运行的容器映射端口
- 方法一：
停止容器
停止容器服务
cd /var/lib/docker/containers/container_id
vi hostconfig.json
如果之前没有端口映射, 应该有这样的一段:
"PortBindings":{}
增加一个映射, 这样写:
"PortBindings":{"3306/tcp":[{"HostIp":"","HostPort":"3307"}]}
前一个数字是容器端口, 后一个是宿主机端口.
而修改现有端口映射更简单, 把端口号改掉就行.

如果config.v2.json里面也记录了端口，也要修改




- 方法二：提交新的镜像，然后添加端口创建新的容器(方法待测)
第一步：提交一个运行中的容器为镜像
docker commit containerid foo/live

第二步：运行镜像并添加端口
docker run -d -p 8000:80  foo/live /bin/bash
