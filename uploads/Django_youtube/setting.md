## Python 生成requirement以及使用requirements.txt安装类库

### 操作

在A电脑的环境中：

```
快速生成requirement.txt的安装文件


(CenterDesigner) xinghe@xinghe:~/PycharmProjects/CenterDesigner$ pip freeze > requirements.txt
```
目标环境下：

```
安装所需要的文件

pip install -r requirement.txt
```



### 具体的原理

> 我理解的是，虚拟环境把本机的python，库，全都考了一份到evn里，那么我另一个电脑拿来这个env，就用这个env里的python版本，库接着进行 。
>
> 是的。<br>你甚可以把另一台电脑里的env目录中的虚拟环境目录复制到本机相应位置,一样可以用
>
> 你最多只需要生成requments.txt。<br>放到你的项目根目录下<br>上传git<br>换电脑<br>建立新虚拟环境<br>拉出git上的项目<br>pip install requments.txt<br>就自动安装相关包了<br>可以跑你的项目的虚拟环境就建成了



列出需要安装的包：

> pip freeze

生成requirements.txt文件，执行如下命令：

> pip freeze > requirements.txt

在env1生成安装要求，在env2安装，可以执行如下命令：

> $ env1/bin/pip freeze > requirements.txt
>
> $ env2/bin/pip install -r requirements.txt

作者：土豆特别想爬山

链接：https://www.jianshu.com/p/2be90ca7bdb3

來源：简书