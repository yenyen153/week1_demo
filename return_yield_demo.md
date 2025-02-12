## Function - Return
- 在def func()中，print只是把結果展示出，但沒辦法賦予他一個變數，而使用return則是把結果傳回程式，我們可以對這個return的結果賦予一個變數

```
def num_sum(*args):
    print(sum(args))


num1 = num_sum(13, 5, 267, 7, 45)

num_sum(13, 5, 267, 7, 45)
print(num1)
```

> 337
> 
> 337
> 
> None
- 並沒有辦法把print的值給予一個變數，因此num1回傳的值是None

```
def num_sum2(*args):
    return sum(args)


num2 = num_sum2(13, 5, 267, 7, 45)

num_sum2(13, 5, 267, 7, 45)
print(num2)
```

> 337
- num_sum2只有把值回傳給程式，並沒有print的概念，因此不會把結果展示出
- 而當賦予一個變數名稱，就可以用在print上


- 因此可以總結，當接下來的程式需要用到function所產生的結果時，可用return回傳數值，並給予變數名稱
- 單純要檢視function產生結果時，用print，或是不確定return值的型態，也可以用print檢查


## Function - yield

- return 與 yield對比，return像是一次放一部影片，yield則是可以暫停後，再接著暫停點播放

### return
```
def cook_noodles():
    
    return "倒入水"
    return "水煮沸了"
    return "放入麵"
    return "泡麵煮好了！"

print(cook_noodles())
```
> 倒入水

### yield

```
def cook_noodles_step_by_step():

    yield "倒入水"
    yield "水煮沸了"
    yield "放入麵"
    yield "麵煮好了！"

print(cook_noodles_step_by_step
```
><generator object cook_noodles at 0x000001F8521EFE20>
- yield是一種generator，不像return或print可以直接呼叫

```
for step in cook_noodles_step_by_step():
    print(step)
```
>倒入水
> 
>水煮沸了
> 
>放入麵
> 
>麵煮好了！
> 
- 總結，會使用到yield的情況，是專案需要按步驟，且步驟是能接續的
- 而return適合用在結果需要一次性就產出在程式中