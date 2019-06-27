import unittest
import pysnooper

# 大数加法
class TestClass(unittest.TestCase):

    # 测试前的准备工作
    def setUp(self):
        pass

    # 测试后的扫尾工作
    def tearDown(self):
        pass

    # 测试代码
    # @pysnooper.snoop()
    def test_my_sum(self, num1, num2):
        # 判断用户输入的字符串是否是数字，如果不是则提示错误信息
        if num1.isdigit() and num2.isdigit():
            pass
        else:
            print("您的输入不合法，请重新输入")
            return

        # 判断两个列表的长度，使list1和list2的长度相等，不够的，就补0
        max_len = len(num1) if len(num1) > len(num2) else len(num2)
        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)

        # 创建列表，用来保存输入的数字
        # 这里的列表里必须先放入0,以解决两数相加要创建新的一位的问题，例如 99 + 2 = 101
        li1 = [0]
        li2 = [0]

        # 循环遍历输入的字符串类型的数字，将其转化成int类型，并添加到创建的列表中
        for i in num1:
            li1.append(int(i))
        for i in num2:
            li2.append(int(i))

        # 将两个列表中的数据相加合并到li1中
        for i in range(len(li1)):
            li1[i] = li1[i] + li2[i]
        # print(li1)
        # 循环判断每一个元素的大小，如果大于10，就让原来大于10的数字变成取余之后的数字,使大于10的元素的前一个元素加一，模拟进位制
        # 这里的i表示的是li1列表的下标，从最后一个元素起，便遍历到第一个元素（反向遍历）
        for i in range(len(li1) - 1, 0 - 1, -1):
            if li1[i] >= 10:
                li1[i] = li1[i] % 10
                li1[i - 1] = li1[i - 1] + 1

        # 如果数字前面是0，则默认去掉前面的0，例如00123应该输出的是123
        # 使用字符串切片，把数字前面的0去掉
        string = ""
        for i in li1:
            string += str(i)
        if string.startswith("0"):
            string = string[1:]

        # 把处理过后的结果转成int类型，之后返回
        return int(string)

# 程序入口
if __name__ == '__main__':
    num1 = input("请输入第一个数字：")
    num2 = input("请输入第二个数字：")
    tc = TestClass()
    result =tc.test_my_sum(num1, num2)
    print(result)

   
# python脚本运行方式：python largeNumber.py
