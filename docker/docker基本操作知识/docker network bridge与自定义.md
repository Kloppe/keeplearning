相关文章地址：
https://blog.csdn.net/dhaiuda/article/details/82820318#bridge%E7%BD%91%E7%BB%9C


自定义bridge网络与默认bridge网络对比：

默认桥接网络中的容器只能通过IP地址访问其他容器（除非使用遗留的-link指令连接两个容器），而自定义桥接网络提供DNS解析，可以通过容器的名字或是别名访问其他容器
容器可以自由的进入或是退出自定义桥接网络，如果想要退出默认桥接网络，需要先停止容器的运行，然后重新创建该容器，并指定需要连接的其他网络

如果更改了默认桥接网络的网络配置，需要重新启动docker，并且由于默认桥接网络只有一个，因此所有容器的网络配置都是一样的，而用户自定义网络可以在创建时指定网络配置（例如默认网关、MTU等），不需要重启docker，灵活性更高

在默认桥接网络中，可以通过--link参数连接两个容器来共享环境变量，用户自定义网络中无法使用这种方式，但是docker提供了更好的方式：                 
1、多个容器可以使用docker volume（这是docker存储数据的一种方式，以后会介绍）挂载到同一个文件，在文件中指明环境变量，从而实现所容器的环境变量共享                                                                                                                             
2、多个容器可以使用同一个docker-compose（与docker service有关）文件启动 ，可以在该文件中定义共享环境变量                               
3、可以使用swarm services，并且通过  secrets 和 configs  （这两个还没看）实现环境变量共享
