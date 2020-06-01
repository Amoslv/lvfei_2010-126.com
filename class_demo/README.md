包/
├── __init__.py
├── 模块1.py
├── 模块2.py
├── 子包1/
    ├── __init__.py
    ├── 模块3.py
    └── 模块4.py
└── 子包2/
    ├── __init__.py
    ├── 模块5.py
    └── 孙子包1/
        ├── __init__.py
        └── 模块6.py

需要注意的是，每个层级的包下都需要有一个 __init__.py 模块。这是因为只有当目录中存在 __init__.py 时，Python 才会把这个目录当作包。

#### 包的导入

导入包中模块的方法
```
import 包.子包.模块
```

模块导入后，可以使用该模块中所定义的名字（变量、函数类）。方式如下：

```
模块名.变量
模块名.函数
模块名.类
```