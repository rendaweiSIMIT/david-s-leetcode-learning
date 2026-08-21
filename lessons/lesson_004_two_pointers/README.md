# Lesson 004：双指针

双指针不是某一份固定代码，而是用两个变量记录两个位置。本节会用到两种形式：

1. `left` 和 `right` 从两端向中间移动；
2. `read` 负责读取，`write` 负责把有效元素写到列表前部。

先读“Python 语法速查”，再依次做三题。

## 0. 本节 Python 语法速查

### `len`：获得长度

```python
text = "level"
print(len(text))  # 5

numbers = [10, 20, 30]
print(len(numbers))  # 3
```

### 通过下标读取元素

Python 下标从 `0` 开始：

```python
numbers = [10, 20, 30]

print(numbers[0])  # 10，第一个元素
print(numbers[1])  # 20，第二个元素
print(numbers[2])  # 30，第三个元素
```

最后一个元素的下标是 `len(numbers) - 1`：

```python
right = len(numbers) - 1
print(right)          # 2
print(numbers[right]) # 30
```

字符串也能通过下标读取字符：

```python
text = "cat"
print(text[0])  # "c"
print(text[2])  # "t"
```

### `while`：条件成立时反复执行

```python
number = 0

while number < 3:
    print(number)
    number += 1
```

输出：

```text
0
1
2
```

`number += 1` 等价于：

```python
number = number + 1
```

类似地：

```python
right -= 1  # 等价于 right = right - 1
```

如果循环中的变量始终不变，条件可能永远为真，程序就会陷入死循环。因此双指针循环每轮必须根据情况移动指针或直接 `return`。

### `if / elif / else`：三种互斥情况

```python
if current_sum == target:
    print("相等")
elif current_sum < target:
    print("太小")
else:
    print("太大")
```

- `==`：判断相等；
- `<`：小于；
- `>`：大于；
- `!=`：判断不相等。

如果暂时还没写某个分支，可以用 `pass` 保持语法完整：

```python
if current_sum == target:
    pass  # 暂时什么也不做，之后需要替换
```

### 修改列表中的元素

读取列表：

```python
value = numbers[read]
```

把一个值写入指定位置：

```python
numbers[write] = value
```

也可以直接把读取位置的元素复制到写入位置：

```python
numbers[write] = numbers[read]
```

字符串不能这样原地修改，但列表可以。

### `range(start, stop)`：产生下标

```python
for index in range(1, 4):
    print(index)
```

输出 `1、2、3`，不包含终点 `4`。

所以：

```python
for read in range(1, len(numbers)):
    print(read, numbers[read])
```

表示从下标 `1` 开始，一直读到最后一个元素。

### 切片 `numbers[:k]`

```python
numbers = [1, 2, 3, 99, 99]
k = 3
print(numbers[:k])  # [1, 2, 3]
```

`numbers[:k]` 表示从开头取到下标 `k` 之前，不包含 `k`。第三题只要求列表的前 `k` 个元素正确。

## 1. 第一题：判断回文 `is_palindrome`

### 题意

如果一个字符串从左向右和从右向左完全相同，就返回 `True`，否则返回 `False`。

```text
"level" → True
"abba"  → True
"hello" → False
""      → True
```

本题不忽略空格、标点或大小写，只按字符原样比较。

### 指针怎么变化

以 `"level"` 为例：

```text
下标：  0 1 2 3 4
字符：  l e v e l
       ↑       ↑
     left    right
```

第一次比较 `text[0]` 和 `text[4]`。相同后：

```text
下标：  0 1 2 3 4
字符：  l e v e l
         ↑   ↑
       left right
```

继续比较，直到 `left >= right`。如果中途发现两边不同，可以立即返回 `False`；循环正常结束说明所有对应字符都相同。

### 代码骨架

```python
left = 0
right = len(text) - 1

while left < right:
    if text[left] != text[right]:
        pass  # TODO：替换为立即返回 False

    # TODO：让 left 加 1，让 right 减 1

# TODO：循环正常结束后返回 True
```

空字符串时 `right == -1`，一开始 `left < right` 就是 `False`，不会进入循环，因此也能自然返回 `True`。

## 2. 第二题：有序数组 Two Sum `two_sum_sorted`

### 题意

输入列表已经按从小到大排列，并且恰好存在一组答案。返回两个元素的下标。

```python
numbers = [1, 2, 4, 8, 13]
target = 14

# 返回 [0, 4]，因为 numbers[0] + numbers[4] == 14
```

### 为什么可以移动指针

开始时取最左和最右的元素：

```python
current_sum = numbers[left] + numbers[right]
```

因为列表有序：

- `current_sum == target`：找到答案；
- `current_sum < target`：当前和太小，左边元素需要变大，所以 `left += 1`；
- `current_sum > target`：当前和太大，右边元素需要变小，所以 `right -= 1`。

### 代码骨架

```python
left = 0
right = len(numbers) - 1

while left < right:
    current_sum = numbers[left] + numbers[right]

    if current_sum == target:
        pass  # TODO：返回两个下标
    elif current_sum < target:
        pass  # TODO：让 left 加 1
    else:
        pass  # TODO：让 right 减 1
```

每轮至少排除一个位置，两个指针总共最多移动 `n` 次，所以时间复杂度是 `O(n)`，额外空间是 `O(1)`。

## 3. 第三题：有序数组原地去重 `remove_duplicates_sorted`

### 题意

给定一个已经排序的列表，把不同的元素依次覆盖到列表前部，并返回不同元素的数量 `k`。

输入：

```python
numbers = [1, 1, 2, 2, 3]
```

完成后只要求：

```python
k == 3
numbers[:k] == [1, 2, 3]
```

下标 `k` 后面的旧内容是什么并不重要。不能创建另一个保存全部结果的列表。

### `read` 和 `write` 分别表示什么

- `read`：当前正在检查哪个元素；
- `write`：下一个新元素应该写到哪里；
- `numbers[:write]`：已经完成去重的有效区域。

由于列表已经排序，相同元素都挨在一起。判断当前元素是不是新元素，只需将它与最近保留的元素 `numbers[write - 1]` 比较。

以 `[1, 1, 2, 2, 3]` 为例：

```text
开始：第一个 1 直接视为已保留
write = 1

read = 1：numbers[1] 是 1，与最近保留的 1 相同，跳过
read = 2：numbers[2] 是 2，与最近保留的 1 不同
          把 2 写到 numbers[write]，然后 write 加 1
read = 3：当前是 2，与最近保留的 2 相同，跳过
read = 4：当前是 3，与最近保留的 2 不同，写入并移动 write
```

最终列表前部会是：

```text
[1, 2, 3, ?, ?]
          ↑
       write = 3
```

### 空列表是特殊边界

空列表没有第一个可保留元素，所以需要先处理：

```python
if len(numbers) == 0:
    return 0
```

### 代码骨架

```python
if len(numbers) == 0:
    return 0

write = 1

for read in range(1, len(numbers)):
    if numbers[read] != numbers[write - 1]:
        pass  # TODO：写入 numbers[write]，然后让 write 加 1

return write
```

## 4. 测试

完成后在仓库根目录运行：

```powershell
python -m unittest lessons.lesson_004_two_pointers.test_practice -v
```

如果文件还包含 `raise NotImplementedError`，对应函数被调用时会显示 `ERROR`。一次只完成一个函数也可以：测试输出会告诉你哪些函数已经通过。
