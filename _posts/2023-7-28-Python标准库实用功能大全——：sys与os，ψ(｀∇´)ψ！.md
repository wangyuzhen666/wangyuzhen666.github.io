---
layout: post
title: Python标准库实用功能大全——第一篇：sys与os，ψ(｀∇´)ψ！
categories: Python
description: Python标准库实用功能大全——第一篇：sys与os，ψ(｀∇´)ψ！
keywords: Python,python
---

Python标准库实用功能大全——第一篇：sys与os，ψ(｀∇´)ψ！
====================================

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

置顶 [WANGYUZHEN王玉镇](https://blog.csdn.net/wyz831201 "WANGYUZHEN王玉镇") 

分类专栏： [python](https://blog.csdn.net/wyz831201/category_11098727.html) 文章标签： [python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=) [Python标准库](https://so.csdn.net/so/search/s.do?q=Python%E6%A0%87%E5%87%86%E5%BA%93&t=all&o=vip&s=&l=&f=&viparticle=) [wyz831201](https://so.csdn.net/so/search/s.do?q=wyz831201&t=all&o=vip&s=&l=&f=&viparticle=)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：[https://blog.csdn.net/wyz831201/article/details/119454266](https://blog.csdn.net/wyz831201/article/details/119454266)
 版权

 [![](https://img-blog.csdnimg.cn/20201014180756930.png?x-oss-process=image/resize,m_fixed,h_64,w_64) python 专栏收录该内容](https://blog.csdn.net/wyz831201/category_11098727.html "python")
 

Python官方提供的不少包和模块，我们称之为标准库，python标准库会随着python解释器一直安装到你的电脑中。本文章将会介绍一些作者搜集整理的常用的标准库中的模块。

NO.1：sys

sys模块的功能很多，这里我们介绍一些比较实用的功能模块.sys提供了许多变量来处理python运行时环境的不同部分。

1.识别操作系统。

    import sys print(sys.platform)

如果是是windows平台，应该输出的是win32。其他系统请参考下表。

系统及相应执行结果。

系统

执行结果

Linux

linux

Windows

win32

Windows/Cygwin

cygwin

Mac OS X

darwin

2.处理命令行参数。

sys.argv变量可以获取命令行的参数。argv是一个list类型的变量，它会返回在命令行中用户输入的参数，例如:

    import sys print(sys.argv)

我们可以在命令行终端中使用_**python 9.4.2.py arg1 arg2**_运行代码。

结果是：

    ['9.4.2.py','arg1','arg2']

从结果可以看到，sys.argv返回了一个列表。题目列表的第一个元素是这个文件名，第二个元素是我们运行时输入的参数的内容。

3.搜索模块的路径。

sys.path存储了python结束其需要搜索的所有路径。我们可以通过修改该变量，修改搜索模块的路径。

    import sys for path in sys.path:    print(path)

结果如下：

    C:\Users\dell\Documents\mindplus-py\environment\Python3.6.5-64\python36.zipC:\Users\dell\Documents\mindplus-py\environment\Python3.6.5-64\DLLsC:\Users\dell\Documents\mindplus-py\environment\Python3.6.5-64\libC:\Users\dell\Documents\mindplus-py\environment\Python3.6.5-64C:\Users\dell\Documents\mindplus-py\environment\Python3.6.5-64\lib\site-packagesC:\Users\dell\Documents\mindplus-py\environment\Python3.6.5-64\lib\site-packages\win32    C:\Users\dell\Documents\mindplus-py\environment\Python3.6.5-64\lib\site-packages\win32\libC:\Users\dell\Documents\mindplus-py\environment\Python3.6.5-64\lib\site-packages\Pythonwin

在不同的环境下执行的结果可能会不一样。

4.退出程序

想要退出程序的话，可以调用sys.exit函数。（0：正常退出；其他为异常）

sys模块的exit函数，通过抛出一个SystemExit异常来尝试结束程序，Python代码可以捕获这个异常来进行一些程序退出前的清理工作，也可以不退出程序。sys.exit函数同样可以带一个参数来作为程序的退出码，默认是0。

5.查找已导入的模块。

sys.modules是一个全局字典，该字典在python启动后就加载到内存中。每当程序员导入新的模块时。sys.modules就会自动记录。当二次导入该模块时，python会直接到字典中查找。从而加快了程序运行的速度。例如：

    ​import sys print(sys.modules.keys())print(sys.modules.values())print(sys.modules ["os"]) ​

执行结果如下：

    dict_keys(['builtins', 'sys', '_frozen_importlib', '_imp', '_warnings', '_thread', '_weakref', '_frozen_importlib_external', '_io', 'marshal', 'nt', 'winreg', 'zipimport', 'encodings', 'codecs', '_codecs', 'encodings.aliases', 'encodings.utf_8', '_signal', '__main__', 'encodings.latin_1', 'io', 'abc', '_weakrefset', 'site', 'os', 'errno', 'stat', '_stat', 'ntpath', 'genericpath', 'os.path', '_collections_abc', '_sitebuiltins', 'sysconfig', '_bootlocale', '_locale', 'encodings.gbk', '_codecs_cn', '_multibytecodec', 'pywin32_bootstrap', 'pywin32_system32'])dict_values([<module 'builtins' (built-in)>, <module 'sys' (built-in)>, <module '_frozen_importlib' (frozen)>, <module '_imp' (built-in)>, <module '_warnings' (built-in)>, <module '_thread' (built-in)>, <module '_weakref' (built-in)>, <module '_frozen_importlib_external' (frozen)>, <module 'io' (built-in)>, <module 'marshal' (built-in)>, <module 'nt' (built-in)>, <module 'winreg' (built-in)>, <module 'zipimport' (built-in)>, <module 'encodings' from 'C:\\Users\\dell\\Documents\\mindplus-py\\environment\\Python3.6.5-64\\lib\\encodings\\__init__.py'>, <module 'codecs' from 'C:\\Users\\dell\\Documents\\mindplus-py\\environment\\Python3.6.5-64\\lib\\codecs.py'>, <module '_codecs' (built-in)>, <module 'encodings.aliases' from 'C:\\Users\\dell\\Documents\\mindplus-py\\environment\\Python3.6.5-64\\lib\\encodings\\aliases.py'>, <module 'encodings.utf_8' from 'C:\\Users\\dell\\Documents\\mindplus-py\\environment\\Python3.6.5-64\\lib\\encodings\\utf_8.py'>, <module '_signal' (built-in)>, <module '__main__' from 'C:\\Users\\dell\\Documents\\mindplus-py\\user\\2021-08-06-14-41-30\\Python标准库.py'>, <module 'encodings.latin_1' from 'C:\\Users\\dell\\Documents\\mindplus-py\\environment\\Python3.6.5-64\\lib\\encodings\\latin_1.py'>, <module 'io' from 'C:\\Users\\dell\\Documents\\mindplus-py\\environment\\Python3.6.5-64\\lib\\io.py'>, <module 'abc' from 'C:\\Users\\dell\\Documents\\mindplus-py\\environment\\Python3.6.5-64\\lib\\abc.py'>, <module '_weakrefset' from 'C:\\Users\\dell\\Documents\\mindplus-py\\environment\\Python3.6.5-64\\lib\\_weakrefset.py'>, <module 'site' from 'C:\\Users\\dell\\Documents\\mindplus-py\\environment\\Python3.6.5-64\\lib\\site.py'>, <module 'os' from 'C:\\Users\\dell\\Documents\\mindplus-py\\environment\\Python3.6.5-64\\lib\\os.py'>, <module 'errno' (built-in)>, <module 'stat' from 'C:\\Users\\dell\\Documents\\mindplus-py\\environment\\Python3.6.5-64\\lib\\stat.py'>, <module '_stat' (built-in)>, <module 'ntpath' from 'C:\\Users\\dell\\Documents\\mindplus-py\\environment\\Python3.6.5-64\\lib\\ntpath.py'>, <module 'genericpath' from 'C:\\Users\\dell\\Documents\\mindplus-py\\environment\\Python3.6.5-64\\lib\\genericpath.py'>, <module 'ntpath' from 'C:\\Users\\dell\\Documents\\mindplus-py\\environment\\Python3.6.5-64\\lib\\ntpath.py'>, <module '_collections_abc' from 'C:\\Users\\dell\\Documents\\mindplus-py\\environment\\Python3.6.5-64\\lib\\_collections_abc.py'>, <module '_sitebuiltins' from 'C:\\Users\\dell\\Documents\\mindplus-py\\environment\\Python3.6.5-64\\lib\\_sitebuiltins.py'>, <module 'sysconfig' from 'C:\\Users\\dell\\Documents\\mindplus-py\\environment\\Python3.6.5-64\\lib\\sysconfig.py'>, <module '_bootlocale' from 'C:\\Users\\dell\\Documents\\mindplus-py\\environment\\Python3.6.5-64\\lib\\_bootlocale.py'>, <module '_locale' (built-in)>, <module 'encodings.gbk' from 'C:\\Users\\dell\\Documents\\mindplus-py\\environment\\Python3.6.5-64\\lib\\encodings\\gbk.py'>, <module '_codecs_cn' (built-in)>, <module '_multibytecodec' (built-in)>, <module 'pywin32_bootstrap' from 'C:\\Users\\dell\\Documents\\mindplus-py\\environment\\Python3.6.5-64\\lib\\site-packages\\win32\\lib\\pywin32_bootstrap.py'>, <module 'pywin32_system32' (namespace)>])<module 'os' from 'C:\\Users\\dell\\Documents\\mindplus-py\\environment\\Python3.6.5-64\\lib\\os.py'>

由于环境不同，所以结果也可能会不同。 

NO.2:os

Python的os模块封装了操作系统的文件和目录操作。

1.获取当前文件所在目录。

    import osprint(_file_)print(os.path.dirname(_file_))

\_file\_是Python的内置变量，os.path.dirname(\_file\_))表示的是文件当前的位置，可以替换成别的文件。

2.获取当前路径。

    import os print(os.getcwd())

这个例子中的路径对应的是windows平台。其他的平台请视情况修改路径。

3.重命名文件。

    import os os.renane("a.text","b.txt")

Rename函数会将文件a.text。重命名为b.txt

* * *

喜欢这篇文章的朋友可以关注我，在学习编程的路上，我们共同前进！
-------------------------------
