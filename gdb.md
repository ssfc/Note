https://www.bilibili.com/video/BV1EK411g7Li/?spm_id_from=333.788.recommend_more_video.0&vd_source=3ef4175721f926fbf390a069da19b0ca

## EP1: What is GDB; 
1. Objective: 程序运行时检查里面发生了什么; 
2. 具体工作: 打断点, 在程序停止时查看参数; 

## EP2: Install GDB; 

## EP3: gdb的quickstart; 
1. 编译并启动gdb: g++ -g learn_gdb.cpp; gdb a.out 
2. 在main函数(函数名)放置断点: b main (函数名)
3. 查看源代码: list
4. 在14行设置断点: b(break) 14
5. 查看所有断点: info b ; 每次启动都得设置一次; 
6. 执行程序, 在断点停止: r(run)
7. 执行下一步程序: n(next)

## EP4: print & step使用
1. 显示变量当前值: p(print) arr[0] (变量名) ; $后的数值每次加一; 
2. 显示变量当前地址: p(print) &arr[0] (&变量名) 
3. 
