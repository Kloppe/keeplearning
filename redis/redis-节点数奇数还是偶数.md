看业务需求：
特点：master数量必须必salve或者等于，否则数据会丢失一部分

3节点环境：1个master、2个slave

        存储空间：最大等于1个节点的容量。（如果是2个master的话，那么数据会丢失一部分）

        冗余性：允许1个节点故障。



    4节点环境：2个master、2个slave

        存储空间：2个节点的容量。

        冗余性：允许1个节点故障。（集群中，半数以上节点认为故障，才会选举。）



    5节点环境：2个master、3个slave

        存储空间：2个节点的容量。

        冗余性：允许2个节点故障。



    6节点环境：3个master、3个slave

        存储空间：3个节点的容量。

        冗余性：允许2个节点故障。
