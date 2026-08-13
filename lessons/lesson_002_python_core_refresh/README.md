# Lesson 002：Python 面试核心语法快速恢复

这一课不再逐行带写。下面是完成练习需要的全部语法，可直接查阅。

## 函数、判断与返回值

```python
def larger_than(number, threshold):
    if number > threshold:
        return True
    return False
```

参数是调用函数时传入的数据。`return` 会立即结束函数，并把结果返回给调用处。

## 列表 `list`

列表有顺序，可以包含重复元素：

```python
result = []
result.append(10)
result.append(20)
print(result)  # [10, 20]
```

## 字典 `dict`

字典保存“键 → 值”的对应关系：

```python
counts = {}
word = "ai"
counts[word] = counts.get(word, 0) + 1
```

`counts.get(word, 0)` 表示：如果 `word` 已存在就取出原值，否则使用默认值 `0`。

## 集合 `set`

集合用于保存不重复的元素，并快速判断元素是否已经出现：

```python
seen = set()
seen.add(7)

if 7 in seen:
    print("已经出现")
```

## 练习要求

打开 `practice.py` 完成三个函数。允许反复查看本页，但先不要搜索完整答案。

完成后在仓库根目录运行：

```powershell
python -m unittest lessons.lesson_002_python_core_refresh.test_practice -v
```

测试失败时，先读最后一段：`FAIL` 通常表示结果不符合预期，`ERROR` 通常表示程序运行过程中报错。

