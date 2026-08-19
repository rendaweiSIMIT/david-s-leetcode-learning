# Session 002：Python 面试核心语法快速恢复

日期：2026-08-13  
计划用时：45–75 分钟  
目标：用三个可测试函数快速恢复循环、判断和核心容器操作。

## 节奏调整

学习者已正确解释列表循环，并反馈最初课程拆分过细。本节开始减少逐行引导：先给必要语法速查，再独立完成小函数，通过测试反馈问题。

## 本次内容

- 函数的参数和 `return`
- 列表追加：`list.append`
- 字典读取与更新：`dict.get`、下标赋值
- 集合查找与添加：`in`、`set.add`
- 空输入、重复值和严格比较边界

## 练习

见 `lessons/lesson_002_python_core_refresh/practice.py`：

1. `count_greater_than`
2. `word_frequencies`
3. `unique_in_order`

完成后运行：

```powershell
python -m unittest lessons.lesson_002_python_core_refresh.test_practice -v
```

## 完成记录

- 实际用时：
- 完成日期：2026-08-19
- 首次测试通过数：5/6
- 最终测试结果：6/6
- 查阅内容：允许查看本节 README，不使用 AI/搜索
- `count_greater_than`：独立完成并通过边界测试
- `word_frequencies`：询问如何在未知单词种类数时计数；理解字典会动态增加键，并正确使用 `counts.get(word, 0) + 1`
- `unique_in_order` 第一次错误：先转为集合再遍历集合，完成去重但丢失输入顺序
- `unique_in_order` 第二次错误：先把所有元素放入 `seen`，随后检查 `item in seen`，条件对所有元素恒为真，因而没有去重
- 最终修正：按输入顺序单次遍历；仅当元素不在 `seen` 时，同时加入集合和结果列表
- 错误类型：主要是数据结构语义与循环时序，不是语法错误
- 后续问题：询问判断和添加是否花时间、时间花在哪里；由此引入单次操作成本、集合平均 `O(1)`、列表追加摊还 `O(1)` 和整体 `O(n)` 的区别
- 复杂度检查：能正确判断 `n` 个元素遍历 `n` 次，输入翻倍时线性算法耗时约翻倍；随后理解双层遍历的 `O(n²)` 在输入翻倍时约为四倍
- 下一步：进入数组和哈希基础
