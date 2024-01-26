# 远程frp

https://zhuanlan.zhihu.com/p/42071021

./frps -c frps.ini

./frpc -c frpc.ini



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