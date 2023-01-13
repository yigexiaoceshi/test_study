# -*-coding: utf-8 -*-
"""
pip介绍：pip是Python中的标准库管理器，允许安装和管理不属于Python标准库里的其他软件包
www.pypi.com托管了大量非常流行的库
在Python2的2.7.9以及Python3的3.4版本往后，pip被直接包括在Python的安装包里
常用方法：
 * pip help：查看帮助文档
 * pip install 包名：安装包（默认最新版本），如果需要安装指定版本则执行pip install 包名==版本号
 * pip install -U 包名：升级包的版本到最新
 * pip uninstall 包名：卸载
 * pip list：列出所有的包文件
 * pip download 包名：下载安装包
 * pip search 包名：搜索安装包
不少国外的镜像文件下载速度较慢甚至无法连接，这里可以使用国内的镜像源下载安装:
pip3 install 包名 -i 国内镜像源地址 --trusted-host 国内镜像源的host
示例：pip install jupyter -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
国内常用pip镜像源：
阿里云：https://mirrors.aliyun.com/pypi/simple/
清华：https://pypi.tuna.tsinghua.deu.cn/simple
豆瓣：http://pypi.douban.com/simple
"""

"""
虚拟环境管理：
1、命令行操作：
    * 创建一个名称为test_venv的虚拟环境：python -m venv test_venv
    * 当前目录下生成"test_venv"目录，可使用ls查看：ls
    * 进入到test_venv目录：cd test_venv
    * 激活并进入虚拟环境：
        Windows：tutorial-env/Scripts/activate.bat
        Unix或者macOS：source tutorial-env/bin/activate
    * 激活之后会自动进入虚拟环境目录(进入虚拟环境的命令行前面带虚拟环境的名称，本机的系统环境是不带的)，查看虚拟环境下安装的包：pip list
    * 退出虚拟环境：deactivate
    * 删除虚拟环境：rm -rf test_venv
2、pycharm操作：
    * 在pycharm的欢迎界面点击Create New Project，进入虚拟环境创建页面
    * 在Location输入框里输入项目的路径及名称
    * 在New Virtualenv environment里操作虚拟环境的创建及设置
    * New environment using下拉有Virtualenv、Pipenv、Conda三种方式，默认为Virtualenv
    * New environment using下的Location指的是虚拟环境的路径及名称
    * Base interpreter指的是虚拟环境指定的Python解释器（可能会有多个版本，指定哪个版本则虚拟环境会自动创建一套该版本的Python开发环境）
    * Inherit global site-packages意思是继承全局的packages，勾选的话会将系统安装的所有包同步到该虚拟环境下使用，不勾选则是全新的虚拟环境
    * Make available to all projects意思是该虚拟环境对所有项目可用，一般不勾选
    * Existing interpreter勾选该项意思是使用已经存在的环境，点击下拉选择即可
    注1：全新的虚拟环境默认只包含pip(标准库管理工具)、setuptools(设置工具)、urllib3(网络请求库)三个包，其他的需另行安装
    注2：pycharm创建的虚拟环境界面，可以复制虚拟环境的路径，在命令行同样可以进行进入虚拟环境、进入python命令行、退出虚拟环境、包管理等操作
附：pycharm设置页面，Project Interpreter页面的Project Interpreter下拉选择所有的环境，包括所有的虚拟环境和系统环境，可管理所有环境下所有的包
"""