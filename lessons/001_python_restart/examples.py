"""可直接运行的 Python 最小示例。"""

name = "David"
years_since_coding = 7
is_restarting = True

print("名字：", name)
print("距上次持续写代码约：", years_since_coding, "年")
print("正在重新开始：", is_restarting)

numbers = [3, 1, 4]
print("完整列表：", numbers)
print("第一个数字：", numbers[0])

threshold = 5
if years_since_coding > threshold:
    print("我们从最基础的写法开始。")
else:
    print("我们先快速复习。")

total = 0
for number in numbers:
    total = total + number
print("所有数字之和：", total)


def double(number):
    """返回一个数字的两倍。"""
    return number * 2


answer = double(6)
print("6 的两倍：", answer)

