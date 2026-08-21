# Lesson 005：滑动窗口与前缀和

这两个模式都在解决同一个问题：连续区间之间有大量重叠，不要每次从头重新计算。

- 滑动窗口：一个连续区间向右移动时，只处理离开的元素和进入的元素。
- 前缀和：预先保存“从开头到当前位置的累计和”，区间和可以用两个前缀相减得到。

## 0. Python 语法速查

### `sum`：计算一组数字的和

```python
numbers = [2, 1, 5]
total = sum(numbers)
print(total)  # 8
```

注意：`sum` 是 Python 内置函数，调用时需要括号。不要把它和变量 `target` 混淆，也尽量不要写 `sum = 10` 覆盖这个函数名。

### 列表切片

```python
numbers = [2, 1, 5, 3]

print(numbers[0:3])  # [2, 1, 5]
print(numbers[:3])   # [2, 1, 5]
```

切片包含开始下标，不包含结束下标。

### `append`：在列表末尾增加元素

```python
prefix = [0]
prefix.append(2)
prefix.append(5)

print(prefix)  # [0, 2, 5]
```

### 读取最后一个元素

```python
prefix = [0, 2, 5]
print(prefix[-1])  # 5
```

`-1` 表示最后一个位置，`-2` 表示倒数第二个位置。

### 元组与解包

一个查询可以用 `(left, right)` 表示：

```python
query = (1, 3)
left, right = query

print(left)   # 1
print(right)  # 3
```

遍历多个查询：

```python
queries = [(0, 2), (1, 3)]

for left, right in queries:
    print(left, right)
```

### 更新最大值和最小值

```python
best = max(best, current_value)
best = min(best, current_value)
```

也可以写成普通判断：

```python
if current_value > best:
    best = current_value
```

## 1. 固定长度滑动窗口 `max_sum_fixed_window`

### 题意

给定整数列表 `numbers` 和正整数 `k`，返回所有长度恰好为 `k` 的连续子数组中，最大的元素和。

保证：

```text
1 <= k <= len(numbers)
```

例如：

```python
numbers = [2, 1, 5, 1, 3, 2]
k = 3
```

长度为 3 的窗口：

```text
[2, 1, 5]          和为 8
   [1, 5, 1]       和为 7
      [5, 1, 3]    和为 9  ← 最大
         [1, 3, 2] 和为 6
```

答案是 `9`。

### 朴素方法为什么慢

如果每个窗口都调用一次：

```python
sum(numbers[start:start + k])
```

每次需要重新处理 `k` 个元素，而相邻窗口有 `k - 1` 个元素相同。总时间约为 `O(nk)`。

### 窗口怎么滑动

先计算第一个窗口：

```python
window_sum = sum(numbers[:k])
best = window_sum
```

窗口向右移动一格时：

```text
旧窗口：[2, 1, 5]
新窗口：   [1, 5, 1]

离开的元素：2
进入的元素：1
```

所以不必重新求和，只需：

```text
新窗口和 = 旧窗口和 - 离开的元素 + 进入的元素
```

当 `right` 是新进入元素的下标时，离开元素的下标是 `right - k`。

### 代码骨架

```python
window_sum = sum(numbers[:k])
best = window_sum

for right in range(k, len(numbers)):
    incoming = numbers[right]
    outgoing = numbers[right - k]

    # TODO：从 window_sum 减去 outgoing，再加上 incoming
    # TODO：更新 best

return best
```

不能把 `best` 初始化为 `0`，因为列表可能全是负数。例如 `[-4, -2, -7]` 的长度 2 最大窗口和是 `-6`，不是 `0`。

复杂度目标：时间 `O(n)`，额外空间 `O(1)`。

## 2. 前缀和区间查询 `range_sum_queries`

### 题意

给定整数列表和多个查询。每个查询 `(left, right)` 要求返回从下标 `left` 到 `right` 的和，左右端点都包含。

```python
numbers = [2, 4, 1, 3]
queries = [(0, 2), (1, 3), (2, 2)]
```

对应结果：

```text
0 到 2：2 + 4 + 1 = 7
1 到 3：4 + 1 + 3 = 8
2 到 2：1

返回 [7, 8, 1]
```

### 前缀数组表示什么

定义：

```text
prefix[i] = numbers 前 i 个元素的和
```

特意让 `prefix[0] = 0`：

```text
numbers:       2   4   1   3
prefix:    0   2   6   7  10
下标:      0   1   2   3   4
```

构建方式：

```python
prefix = [0]

for number in numbers:
    prefix.append(prefix[-1] + number)
```

### 为什么两个前缀相减就是区间和

查询 `[left, right]` 时：

```text
prefix[right + 1]：从开头到 right 的总和
prefix[left]：     left 之前所有元素的总和
```

因此：

```python
interval_sum = prefix[right + 1] - prefix[left]
```

例如查询 `[1, 3]`：

```text
prefix[4] - prefix[1]
= 10 - 2
= 8
```

### 代码骨架

```python
prefix = [0]

for number in numbers:
    # TODO：把新的累计和 append 到 prefix

answers = []

for left, right in queries:
    # TODO：计算区间和并 append 到 answers

return answers
```

若有 `n` 个数字和 `q` 个查询：构建前缀和为 `O(n)`，每个查询 `O(1)`，总时间 `O(n + q)`；前缀数组额外空间 `O(n)`。

## 3. 进阶：可变长度窗口 `min_subarray_len`

### 题意

`numbers` 中全部是正整数。找到和大于或等于 `target` 的最短连续子数组长度；不存在则返回 `0`。

```python
numbers = [2, 3, 1, 2, 4, 3]
target = 7
```

最短窗口是 `[4, 3]`，答案为 `2`。

“全部是正整数”非常重要：右端加入新元素，窗口和只会增加；左端移出元素，窗口和只会减小，因此可以根据和单调移动指针。

### 扩张和收缩

- `right` 每轮向右扩张窗口，并把新元素加入 `window_sum`；
- 当 `window_sum >= target` 时，当前窗口有效；记录长度后不断移动 `left`，尝试缩短；
- 移动 `left` 前，要先从 `window_sum` 中减去即将离开的元素。

窗口 `[left, right]` 的长度是：

```python
right - left + 1
```

### 代码骨架

```python
left = 0
window_sum = 0
best = len(numbers) + 1  # 比任何可能答案都大，表示尚未找到

for right in range(len(numbers)):
    # TODO：把 numbers[right] 加入 window_sum

    while window_sum >= target:
        current_length = right - left + 1
        # TODO：更新 best

        # TODO：从 window_sum 减去 numbers[left]
        # TODO：left 加 1

if best == len(numbers) + 1:
    return 0
return best
```

代码虽然有嵌套的 `while`，但 `right` 最多前进 `n` 次，`left` 也最多前进 `n` 次，因此总时间仍为 `O(n)`，额外空间为 `O(1)`。

## 4. 测试

```powershell
python -m unittest lessons.lesson_005_sliding_window_and_prefix_sum.test_practice -v
```

建议先只完成第一题。其余函数中的 `raise NotImplementedError` 会显示为 `ERROR`，这是尚未完成的正常状态。

