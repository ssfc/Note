# 远程frp

https://zhuanlan.zhihu.com/p/42071021

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