## if __name__ == '__main__'的概念與應用

- if __name__ == '__main__'能用來切割程式內自定義function與主程式


- 之所以能切割，首先要了解__name__代表甚麼


- __name__ 在py檔執行時，會被自動設為 '__main__'，以下面為例，如果執行這分檔案，他會將__name__設為__main__

```
print(__name__)
```
> __main__


### 所以當if __name__ == '__main__'表示
### 當這個假設被觸發時，代表這份檔案正在被執行，也因此下面的主程式才會跟著執行
- 之所以要切割自定義function與主程式，以hello1.py、hello2.py、goodbye.py舉例


- 假設以下程式在hello1.py中

```
def say_hello():
    print("hello world")
    print(__name__)


print('你好啊')
say_hello()
```

> 你好啊
> 
> hello world
> 
> __main__

- 假設以下程式在hello2.py中
```
def say_hello():
    print("hello world")
    print(__name__)


if __name__ == '__main__':
    print('你好啊')
    say_hello()
```
> 你好啊
>
> hello world
>
> __main__


- 假設以下程式在goodbye.py中


hello1.py沒使用if __name__ == '__main__'分割自定義function與主程式情況下


hello1.py中的主程式也會被goodbye.py引用
```
from hello1 import say_hello

say_hello()
print('掰掰')
```
> 你好啊
> 
> hello world
> 
> hello
> 
> hello world
> 
> hello
>
> 掰掰


- hello2.py有分割自定義function與主程式情況下


僅會引用hello2.py中的自定義function，hello2.py本身並沒有被觸發


因此if __name__ == '__main__':的條件不成立，接下來的程式不會被執行
```
from hello2 import say_hello

say_hello()
print('掰掰')
```

> hello world
> 
> hello
> 
> 掰掰
