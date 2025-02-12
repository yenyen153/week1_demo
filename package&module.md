## package與module檔案層級
```
 project
 |-tools(package)
     |-__init__.py
     |-tool.py
 |-tool_demo.py
```

- 演示如何在tool_demo引用tools中的module
```
from tools import tool
print(tool.sum_num(1, 2, 3))
```