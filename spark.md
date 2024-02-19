# 分布式系统

## 安装spark

https://www.bandwagonhost.net/12504.html

## 运行spark

启动ubuntu spark master?  在master电脑上运行， `start-master.sh`  (2024年2月1日)

启动spark worker? 在worker命令行运行， `start-worker.sh spark://主机IP:7077` (2024年2月19日)

网页端查看sparks状态?  主机IP:8080.  如4090机器上就是http://192.168.0.103:8080/

8080端口用于Spark的Web UI，用于监视和管理集群的状态，而7077端口则用于Spark Master节点与Worker节点之间的通信，用于资源分配和作业调度。

