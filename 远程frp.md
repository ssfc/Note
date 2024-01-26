# 远程frp

https://zhuanlan.zhihu.com/p/42071021

1. 从[github](https://link.zhihu.com/?target=https%3A//github.com/fatedier/frp)下载最新的frp二进制文件。其中frps，frps.ini为服务端，供腾讯云使用；frpc，frpc.ini为客户端，供家里的电脑使用。
2. 设置frps.ini，并在腾讯云上运行 `./frps -c frps.ini`，注意frps需要持续运行，可以专门开一个tmux窗口做这个。

```ini
# frps.ini
[common]
bind_port = 7000 #frps服务监听的端口
```

3. 设置frpc.ini，并在工作站上运行，`./frpc -c frpc.ini`，同样，记得后台运行

```ini
# frpc.ini
[common]
server_addr = 1.15.63.146 # 此处为 腾讯云 的公网ip
server_port = 7000 # 服务器上frps服务监听的端口

[ssh]
type = tcp
local_ip = 127.0.0.1 
local_port = 22 # 需要暴露的内网机器的端口
remote_port = 6000 # 暴露的内网机器的端口在vps上的端口
```

4. 在需要登录工作站时，使用`ssh -p 6000 user@vps.ip`，`-p 6000`表示ssh链接vps.ip上的6000端口，对应着frpc.ini中的设定，因此会直接被frps转发到内网工作站的127.0.0.1的22端口，即内网工作站的sshd端口上

## frp怎样在client开机启动和后台运行

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
sudo systemctl start frpc
sudo systemctl enable frpc
查看状态
systemctl status frpc