# 远程frp

https://zhuanlan.zhihu.com/p/42071021

https://github.com/ssfc/pytorch_tutorial_official/issues/7

1. 从[github](https://link.zhihu.com/?target=https%3A//github.com/fatedier/frp)下载最新的frp二进制文件。其中frps，frps.ini为服务端，供腾讯云使用；frpc，frpc.ini为客户端，供client 4090使用。
2. 由于frps需要持续运行，可以专门开一个tmux窗口做这个`tmux new -s connect_4090`。设置frps.ini，并在server tencent上运行 `./frps -c frps.ini`。

```ini
# frps.ini
[common]
bind_port = 7000 #frps服务监听的端口
```

3. 设置frpc.ini，并在client 4090上运行，`./frpc -c frpc.ini`，同样，记得后台运行

```ini
# frpc.ini
[common]
server_addr = 1.15.63.146 # 此处为 腾讯云 的公网ip
server_port = 7000 # 服务器上frps服务监听的端口

[ssh]
type = tcp
local_ip = 127.0.0.1 
local_port = 22 # 需要暴露的内网机器的端口
remote_port = 4090 # 暴露的内网机器的端口在vps上的端口
```

4. 在需要登录工作站时，使用`ssh -p 4090 user@vps.ip`，`-p 4090`表示ssh链接server.ip上的4090口，对应着frpc.ini中的设定，因此会直接被frps转发到内网工作站的127.0.0.1的22端口，即内网工作站的sshd端口上
5. 对于client 1660s, 我们设置另外一组frps.ini和frpc.ini。需要在server上新开一个`tmux new -s connect_1660`.，然后运行`./frps -c frps.ini`。

```ini
# frps.ini
[common]
bind_port = 7100 #frps服务监听的端口
```

```ini
# frpc.ini
[common]
server_addr = 1.15.63.146 # 此处为 腾讯云 的公网ip
server_port = 7100 # 服务器上frps服务监听的端口

[ssh]
type = tcp
local_ip = 127.0.0.1 
local_port = 22 # 需要暴露的内网机器的端口
remote_port = 6000 # 暴露的内网机器的端口在vps上的端口
```

## 设置frp在client开机启动和后台运行

https://github.com/fatedier/frp/issues/176

在client新建文件frpc.service 

`vim /etc/systemd/system/frpc.service`

fprc.server写法：

```ini
[Unit]
Description=Frp Client Service
After=network.target

[Service]
Type=simple
Restart=on-failure
RestartSec=5s
ExecStart=/home/ssfc/frp/frpc -c /home/ssfc/frp/frpc.ini
ExecReload=/home/ssfc/frp/frpc reload -c /home/ssfc/frp/frpc.ini

[Install]
WantedBy=multi-user.target
```

启用
`sudo systemctl start frpc`
`sudo systemctl enable frpc`
查看状态
`systemctl status frpc`

## 通过内网连接电脑

使用命令`ifconfig`查看内网地址。比如在下一段中，内网ip就是192.168.0.102

```shell
enp3s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.0.102  netmask 255.255.255.0  broadcast 192.168.0.255
        inet6 fe80::5d7c:df6f:fa13:e655  prefixlen 64  scopeid 0x20<link>
        ether 2c:f0:5d:eb:db:0d  txqueuelen 1000  (Ethernet)
        RX packets 289566  bytes 379663920 (379.6 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 145638  bytes 11591608 (11.5 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 18010  bytes 2548450 (2.5 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 18010  bytes 2548450 (2.5 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

```

默认端口是22. 

