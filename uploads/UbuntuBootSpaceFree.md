# [[Ubuntu\] 解决 ubuntu 升级时 /boot 空间不足](https://www.cnblogs.com/rossoneri/p/4017861.html)



经常升级Linux内核，导致更新时警告/boot分区空间不足。这是以为多次升级内核后，导致内核版本太多，清理一下没用的内核文件就行了。

原文地址请保留<http://www.cnblogs.com/rossoneri/p/4017861.html> 

查看安装的内核

```
dpkg --get-selections |grep linux-image
```

也可直接查看/boot下有哪些文件

```
ls /boot
```

查看当前运行内核

```
uname -a
```

将旧的内核删除（尽量保留2-3个以便恢复）

```
sudo apt-get purge linux-image-3.5.0-17-generic
```

清理/usr/src 文件

```
sudo apt-get purge linux-headers-3.13.0-24
```

 

------

 

有人写了一个更直接的命令

```
dpkg -l 'linux-*' | sed '/^ii/!d;/'"$(uname -r | sed "s/\(.*\)-\([^0-9]\+\)/\1/")"'/d;s/^[^ ]* [^ ]* \([^ ]*\).*/\1/;/[0-9]/!d' | xargs sudo apt-get -y purge
```

直接删除除当前运行内核外的所有内核。慎用。

 

参考：

[Ubuntu升级出现/boot空间不足解决](http://blog.csdn.net/zht666/article/details/8776316)

[Ubuntu清理boot分区](http://www.2cto.com/os/201304/206100.html)