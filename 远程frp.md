# 远程frp

https://zhuanlan.zhihu.com/p/42071021

https://github.com/ssfc/pytorch_tutorial_official/issues/7

github网址: https://github.com/fatedier/frp

Doc: https://gofrp.org/zh-cn/docs/setup/systemd/

1. 从[github](https://link.zhihu.com/?target=https%3A//github.com/fatedier/frp)下载最新的frp二进制文件。其中frps，frps.ini为服务端，供腾讯云使用；frpc，frpc.ini为客户端，供client 4090使用。
2. 由于frps需要持续运行，可以专门开一个tmux窗口做这个`tmux new -s connect_4090`。设置frps.ini，并在server tencent上运行 `./frps -c frps.toml`。

```toml
# frps.toml
bindPort = 7000 #frps服务监听的端口
vhostHTTPPort = 8080
```

3. 设置frpc.ini，并在client 4090上运行，`./frpc -c frpc.toml`，同样，记得后台运行

```ini
# frpc.toml
[common]
server_addr = 1.15.63.146 # 此处为 腾讯云 的公网ip
server_port = 7000 # 服务器上frps服务监听的端口

[[proxies]]
name = "test-tcp"
type = "tcp"
localIP = "127.0.0.1"
localPort = 22  # 需要暴露的内网机器的端口
remotePort = 4090 # 暴露的内网机器的端口在vps上的端口

[[proxies]]
name = "web"
type = "http"
localPort = 8080
customDomains = ["4090spark.com"]
```

4. 在需要登录工作站时，使用`ssh -p 4090 user@vps.ip`，`-p 4090`表示ssh链接server.ip上的4090口，对应着frpc.ini中的设定，因此会直接被frps转发到内网工作站的127.0.0.1的22端口，即内网工作站的sshd端口上
5. 对于client 1660s, 我们设置另外一组frps.ini和frpc.ini。需要在server上新开一个`tmux new -s connect_1660`.，然后运行`./frps -c frps.toml`。

```ini
# frps.toml
[common]
bind_port = 7100 #frps服务监听的端口
```

```ini
# frpc.toml
serverAddr = "1.15.63.146"
serverPort = 7100

[[proxies]]
name = "test-tcp"
type = "tcp"
localIP = "127.0.0.1"
localPort = 22
remotePort = 6000

[[proxies]]
name = "web"
type = "http"
localPort = 8080
customDomains = ["www.4090spark.com"]
```

## 设置frp在client开机启动和后台运行

https://github.com/fatedier/frp/issues/176

在client新建文件frpc.service 

`sudo vim /etc/systemd/system/frpc.service`

fprc.service写法：

```ini
[Unit]
Description=Frp Client Service
After=network.target

[Service]
Type=simple
Restart=on-failure
RestartSec=5s
ExecStart=/home/ssfc/frp_0.54.0_linux_amd64/frpc -c /home/ssfc/frp_0.54.0_linux_amd64/frpc.toml
ExecReload=/home/ssfc/frp_0.54.0_linux_amd64/frpc reload -c /home/ssfc/frp_0.54.0_linux_amd64/frpc.toml

[Install]
WantedBy=multi-user.target
```

启用
`sudo systemctl start frpc`

重启

`sudo systemctl restart frpc`

查看状态

`systemctl status frpc`

开机自启动

`sudo systemctl enable frpc`

Comment: 注意官网写的是frps.service, 吾人改成frpc.service了。道理大同小异。(2024年2月1日)

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

Comment:  frp仅仅用在公网连接电脑上，内网不需要，直接连就好了。因此调试frp的时候可以通过内网连接。(2024年2月1日)

# Xshell

### Q: 我通过xshell连接远程服务器，需要用户密钥和密码。怎样把用户密钥和密码保存在xshell中，让我不用每次都输入一遍？

右键会话 - 属性 - 连接 - 用户身份验证 - 去掉password中的对勾 - 再次登录时选择记住密码。(2024年2月1日)



