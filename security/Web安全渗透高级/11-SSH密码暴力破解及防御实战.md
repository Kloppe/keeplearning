-  什么是SSH暴力破解攻击？
SSH暴力破解是指攻击者通过密码字典或随机组合密码的方式尝试登陆服务器（针对的是全网机器），这种攻击行为一般不会有明确攻击目标，多数是通过扫描软件直接扫描整个广播域或网段

- 怎样检测暴力破解攻击？
1、查看近期登陆日志：cat /var/log/secure
2、计算近期失败的登陆次数：cat /var/log/secure|grep 'Failed password for root'|wc -l
宝塔面板上面的风险安全提醒是根据您的服务器日志统计出来的。

- 怎样防御暴力破解攻击？
一：系统及网络安全
1、定期检查并修复系统漏洞
2、定期修改SSH密码，或配置证书登陆
3、修改SSH端口
4、禁Ping
5、若你长期不需要登陆SSH，请在面板中将SSH服务关闭
6、安装悬镜、云锁、安全狗等安全软件(只安装一个)
二：购买企业运维版，开启安全隔离服务
1、宝塔企业运维版的安全隔离功能是专为拦截暴力破解而开发的功能
2、安全隔离服务好比在您的服务器外面建立一道围场，只允许授权IP进来。







##### 参考文章


- [Linux SSH密码暴力破解技术及攻防实战](https://www.freebuf.com/sectool/159488.html)

- [SSH暴力破解的解读与防御](https://blog.csdn.net/chenlongjs/article/details/80682467)
