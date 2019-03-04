# Django站点框架文件介绍

## 建立项目后的根目录

``` cmd 
django-admin startproject <站点名称>
```

该命令在当前目录建立一个子目录/<站点名称>，以及一些默认文件，树状结构如下：

​	<站点名称>/ #我们称这个目录为项目的**根目录**，root
>		​	manage.py
>​	<站点名称>/ 
>​		\__init__.py
>​		settings.py
>​		urls.py
>​		wsgi.py

* **manage.py**:  Django用于管理本项目的命令行工具，站点运行、数据库生成、静态文件手机等需要该文件
* **内层<站点名称>/目录**： 包含了本项目的实际文件（包含了\__init__.py,说明它是一个python包）
* **settings.py**:  Django项目配置文件。默认本项目引用的组件、项目名等。开发过程中需要配置数据库参数、导入其他Python包
* **urls.py**:  维护项目的URL路由映射，即定义客户端访问的URL由哪一个Python模块解释并提供反馈。默认情况下，其中只定义了“/admin”即管理员站点的解释器
* **wsgi.py**:  定义WSGI的接口信息，用于与其他Web服务器集成，一般本文件生成后无需改动。

## 建立应用

``` powershell
PS python manage.py startapp <应用名称>
```

命令完成后会在项目**根目录**下建立如下目录及文件结构

>		​	manage.py
>​		​	<站点名称>/ 
>​		​		\__init__.py
>​		​		settings.py
>​		​		urls.py
>​		​		wsgi.py
>​		​	<应用名称>/
>​		​		\__init__.py
>​		​		admin.py
>​		​		apps.py		
>​		​		migrations/
>​		​			\__init\__.py
>​		​		models.py
>​		​		tests.py
>​		​		views.py

* **\__init__.py**: 该文件存在使得app成为一个Python包
* **admin.py**: 管理站点模型的生命文件，默认为空
* **apps.py**:  应用信息定义文件。在其中生成了类AppConfig, 该类用于定义应用名等Meta数据
* **migrations**包：  用于在之后定义应用迁移功能。
* **models.py**:  添加模型层数据类文件
* **test.py**:  测试代码文件
* **views.py**:  定义URL响应函数

