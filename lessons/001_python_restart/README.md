# Lesson 001：重新写下 Python

今天不学算法，也不背概念。目标只有一个：重新习惯“写一点、运行一下、看到结果”。

## 1. 怎么运行

在仓库根目录 `C:\Users\85365\Desktop\leetcode` 打开 PowerShell，输入：

```powershell
python .\lessons\001_python_restart\examples.py
```

按回车后，Python 会从上到下执行文件。`print(...)` 会把括号里的内容显示在终端。

## 2. 今天需要看懂的最小语法

```python
name = "David"              # 把字符串保存到变量 name
years = 7                    # 整数
is_restarting = True         # 布尔值：真
numbers = [3, 1, 4]          # 列表

print(name)
print(numbers[0])            # 下标从 0 开始，所以这是第一个元素
```

判断使用 `if`。冒号和下一行的四个空格都很重要：

```python
if years > 5:
    print("很久没写了")
else:
    print("还比较熟悉")
```

循环会依次取出列表里的元素：

```python
for number in numbers:
    print(number)
```

函数把一段操作命名，`return` 把结果交还给调用者：

```python
def double(number):
    return number * 2

answer = double(6)
print(answer)  # 12
```

## 3. 动手顺序

先运行 `examples.py`。然后只做这些修改，每改一次都运行一次：

1. 把 `name` 改成你想显示的名字。
2. 给 `numbers` 再增加一个整数。
3. 把 `threshold` 从 `5` 改成 `10`，观察判断结果。
4. 把 `double(6)` 改成另一个数字。

接着打开 `practice.py`，完成三个 `TODO`。可以随时回来看示例，这一课不要求闭卷。

## 4. 报错时怎么办

先不要慌，也不要只截最后一行。Python 报错通常会告诉你：

- 哪个文件；
- 第几行；
- 错误类型；
- 对错误的简短描述。

保留完整报错并发给我，我们会把“读懂报错”也训练成基本能力。

