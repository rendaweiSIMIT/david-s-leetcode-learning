# Lesson 004：双指针

双指针不是固定代码，而是用两个位置共同表示“当前还需要处理的范围”或“已经处理好的区域”。

## 1. 相向指针

适用信号：

- 从左右两端比较；
- 输入已经有序，可以根据结果排除一侧；
- 要寻找一对元素。

基本结构：

```python
left = 0
right = len(items) - 1

while left < right:
    # 检查 items[left] 和 items[right]
    # 根据结果移动 left 或 right
```

### 回文

回文从左往右和从右往左相同。例如：

```text
"level" → True
"hello" → False
```

比较两端字符：不同就能立即返回；相同则两个指针同时向中间移动。

### 有序数组 Two Sum

如果数组已经从小到大排序：

- 当前和小于目标：需要更大的和，移动左指针；
- 当前和大于目标：需要更小的和，移动右指针；
- 当前和等于目标：返回两个下标。

这能把暴力解的 `O(n²)` 降为 `O(n)`，并且只使用 `O(1)` 额外空间。

## 2. 快慢指针

适用信号：

- 原地删除或覆盖元素；
- 读取速度和有效结果的写入速度不同；
- 要把符合条件的元素压缩到数组前部。

对于有序数组去重，可以把列表前部看成“已经去重的有效区域”：

```text
[有效且不重复 | 尚未处理]
                ↑ read
       ↑ write
```

- `read` 依次检查每个元素；
- `write` 指向下一个应该写入新值的位置；
- 因为数组有序，重复值必然相邻，只需和最近保留的值比较。

## 3. Python 语法速查

```python
left += 1       # 等价于 left = left + 1
right -= 1      # 等价于 right = right - 1

for read in range(1, len(numbers)):
    print(read, numbers[read])
```

完成后运行：

```powershell
python -m unittest lessons.lesson_004_two_pointers.test_practice -v
```

