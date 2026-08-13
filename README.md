# David's LeetCode Learning

这是一个以“大厂机试 + 手撕代码”为目标的 Python 算法训练仓库。

这里不追求机械刷题数量，而是建立一套能在压力下独立完成代码的能力：

1. 准确分析时间、空间复杂度；
2. 熟练手写基础数据结构与常见算法；
3. 从题目约束识别算法模式，并能解释为什么；
4. 写出边界清晰、可运行、可测试的 Python 代码；
5. 在限时环境中完成思路说明、编码、测试和复杂度分析。

## 学习方式

每个主题按以下闭环训练：

`概念回忆 → 从零实现 → 典型题 → 变式题 → 限时题 → 错题复盘 → 间隔复习`

默认规则：

- 语言统一使用 Python 3；本机使用 `python` 命令。
- 正式练习时，先独立思考，再逐级获取提示，最后才看完整答案。
- 每道题必须说清楚：朴素解、优化依据、正确性、复杂度、边界条件。
- 题解必须可运行；重要题目要有自动化测试。
- AI 用来提问、审查、给提示和模拟面试，不替代第一次独立作答。
- 学习过程记录在 Git 中，小步提交，保留思路演进和错误。

## 仓库结构

```text
docs/            学习路线、进度与约定
notes/           按主题整理的知识笔记
problems/        题解与对应测试
sessions/        每次学习的过程记录与复盘
templates/       题解、学习记录模板
```

## 当前起点

- Python：3.13.13
- Git：2.54.0
- 当前阶段：Phase 0，Python 手写能力与复杂度基础
- 下一步：完成第一次基线诊断，再按结果调整节奏

详细计划见 [docs/roadmap.md](docs/roadmap.md)，实时状态见 [docs/progress.md](docs/progress.md)。

## 常用命令

```powershell
# 运行单个 Python 文件
python .\problems\example.py

# 运行全部 unittest 测试
python -m unittest discover -s problems -p "test_*.py"

# 查看学习记录改动
git status
git diff
```

