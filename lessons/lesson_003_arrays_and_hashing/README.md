# Lesson 003：数组下标与哈希查找

## 1. 同时获得下标和值

直接遍历列表时只得到元素：

```python
for number in numbers:
    print(number)
```

`enumerate` 可以同时得到下标和值：

```python
for index, number in enumerate(numbers):
    print(index, number)
```

例如 `[10, 20]` 会依次产生 `(0, 10)`、`(1, 20)`。

## 2. 查找方式与复杂度

| 操作 | 平均时间 |
| --- | ---: |
| 遍历长度为 `n` 的列表 | `O(n)` |
| `value in some_list` | `O(n)` |
| `value in some_set` | `O(1)` |
| `key in some_dict` | `O(1)` |
| 通过下标读取 `numbers[index]` | `O(1)` |

集合适合回答“这个值是否出现过”。字典适合保存“一个值对应的额外信息”，例如某个数字第一次出现的下标。

## 3. 本节三题

打开 `practice.py`：

- 第一题只需 `enumerate`、判断和 `return`。
- 第二题需要维护“此前见过的元素”。
- 第三题需要思考：处理当前位置的数字 `number` 时，另一个需要的数字是多少？此前是否已经见过它？

第三题先尝试 15–20 分钟。卡住时告诉我当前思路，我会按级别给提示。

运行全部测试：

```powershell
python -m unittest lessons.lesson_003_arrays_and_hashing.test_practice -v
```

