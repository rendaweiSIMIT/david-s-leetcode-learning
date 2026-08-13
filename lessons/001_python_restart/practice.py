"""Lesson 001 小练习。

可以查看 examples.py。每完成一个 TODO，就运行一次这个文件。
"""

# TODO 1：把字符串改成你希望显示的名字。
name = "任大为"
print("你好，", name)

# TODO 2：在列表里增加两个整数，然后运行程序观察每个数字的输出。
numbers = [2, 5, 8, 1, 3, 4]
for number in numbers:
    print("当前数字：", number)


def triple(number):
    """返回一个数字的三倍。"""
    # TODO 3：模仿 examples.py 中的 double，替换下一行。
    return number * 3


print("7 的三倍应该是 21，实际结果是：", triple(7))

