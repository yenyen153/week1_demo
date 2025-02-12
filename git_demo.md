# 什麼是git

- git 可以想像是一種可以追蹤檔案變更+寫說明的工具


- 從git bash、terminal可以對git下達指令，這些指令是針對被追蹤的檔案


- 常見的有使將檔案加入追蹤的git add，以及對被追蹤檔案提交並給予說明的git commit

## 如何建立git repository - 全新的專案
```
mkdir <repository_name>
git init 
```
- (這一步完成後會發現檔名後面多了.git，表示該資料夾已被git追蹤，但不等於資料夾裡面的檔案也被追蹤)

- 用git status查看，repository中的檔案是紅色字，顯示untracked file，表示檔案沒被追蹤)
```
git add <file_name>
```
- 用git status查看，檔案名變成綠色，並顯示Changes to be committed，代表已經被git追蹤

## 整體流程
>mkdir my_first_repository

>git init

>git add \<file name>

>git commit =m"commit message"

## 如何建立git repository - 已經有使⽤git版控的專案
- 如果是指如何使用已經存在於github上的repository
- 1.可以從github上找到指定的repository，找尋code --> 複製http
- 2 .於自己電腦的terminal輸入 git clone <剛剛複製的http>
- 3 .即可下載github上存在的專案於自己電腦中

>git clone \<repository url>


## .gitignore的意義
- 雖然git可以追蹤檔案變更，有助於開發者理解程式版本不同的影響，但**有些資料並不希望被git追蹤**
- 例如**API_KEY、密碼**等等，或是一些**與程式開發無直接關聯的.exe**，如果一直顯示在untracked file中，也會使版面混亂
- 因此可以建立一個.gitignore檔，將不想被git追蹤的檔案名稱打在.gitignore檔中(通常gitignore會隨著repository建立，但也可以自己建立)

> 可參考.gitignore示範檔


## 如何進⾏提交(commit)
- 1 . 使用git status確認檔案是否已經被追蹤


- 2 . 若為untracked file，要先git add <file name>，若已經被追蹤，可以跳到第3步


- 3 . 接下來git commit -m"欲輸入訊息"

>目前都還在本地commit，還沒commit到遠端github或其他雲端中

- 4 . 確認github已有一個repository，在git bash或terminal中輸入git remote add origin "你的github網址"


- 5 . 提交到github雲端中，使用git push -u origin main

> main與master有差異，要注意自己本地git給予的default名稱是甚麼，origin就是指本地名)

## 整體流程
```
git add <file name>

git commit -m"commit message"
```
## push到github上
```
git remote add origin <github repository url> # 僅限第一次push

git push -u origin master # 僅限第一次push，之後可直接用git push
```

## 檔案還原
- 檔案還原分成**狀態還原**、**內容還原**、**commit還原**

### 狀態還原 - add後的檔案還原
- 狀態改成untracked，檔案內容不變
```
git reset <file name>
```

### 內容還原 - 修改了檔案，但還沒add，想回覆上一次commit
- 內容回到上個commit時的版本，且狀態改為changes to be committed
```
git checkout -- <file name>
```

### commit還原 - 已經commit了，但想收回
- 內容不變，commit被收回，檔案狀態改成changes to be committed
```
git reset soft HEAD~1
```

## 如何切換branch
- branch可用來切分**main/master**，在沒有merge情況下，branch並不會影響到main/master

### 已有branch情況下，切換到指定branch
```
git switch <branch name>
```

### 建立branch並切換
```
git checkout -b <branch name>
```

### 查看目前有哪些branch
```
git branch
```