from collections import Counter
from random import randint
from copy import deepcopy
from math import ceil, floor
import operator
import time
import sys
import re


# 1.判断给定列表是否存在重复元素
def all_unique(lst):
    return len(lst) == len(set(lst))


x = [1, 1, 2, 2, 3, 2, 3, 4, 5, 6]
y = [1, 2, 3, 4, 5]
all_unique(x)  # False
all_unique(y)  # True


# 2.检查两个字符串组成元素是否相同
def anagram(first, second):
    return Counter(first) == Counter(second)


anagram("abcd1", '1dcba')  # True


# 3.内存占用
variable = 30
print(sys.getsizeof(variable))  # 24


# 4.字节占用
def byte_size(string):
    return len(string.encode("utf-8"))


print(byte_size("hello world"))


# 5.打印N次字符串
n = 2
s = "Programming"
print(s * n)


# 6.大写第一个字母
s = "programming is awesome"
print(s.title())


# 7.分块
def chunk(lst, size):
    return list(map(lambda x: lst[x * size: x * size + size],
                    list(range(0, ceil(len(lst) / size)))))


chunk([1, 2, 3, 4, 5], 2)  # [[1, 2], [3, 4], [5]]


# 8.压缩 去除布尔型的值
def compact(lst):
    return list(filter(bool, lst))


# 9.解包
array = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*array)
print(transposed)


# 10.链式对比
a = 3
print(2 < a < 8)
print(1 == a < 2)


# 11.逗号连接
hobbies = ['basketball', 'football', 'swimming']
print('My hobbies are: ' + ', '.join(hobbies))


# 12.元音统计
def count_vowels(str1):
    return len(re.findall(r'[aeiou]', str1, re.IGNORECASE))


print(count_vowels('foobar'))


# 13.首字母小写
def decapitalize(string):
    return string[:1].lower() + str[1:]


# 14.展开列表
def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


def deep_flatten(lst):
    result = []
    result.extend(spread(list(map(lambda x: deep_flatten(x) if type(x) == list else x, lst))))
    return result


print(deep_flatten([1, [2], [[3], [4, [5]], 6], 7]))


# 15.列表的差
def difference(a, b):
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return list(comparison)


# 16.通过函数取差
def difference_by(a, b, fn):
    b = set(map(fn, b))
    return [item for item in a if fn(item) not in b]


difference_by([2.1, 1.2], [2.3, 3.4], floor)
difference_by([{'x': 2}, {'x': 1}, {'x': 1}], lambda v: v['x'])


# 17.链式函数调用
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


a, b = 4, 5
print((subtract if a > b else add)(a, b))


# 18.检查重复项
def has_duplicates(lst):
    return len(lst) != len(set(lst))


# 19.合并两个字典
def merge_two_dicts(a, b):
    c = a.copy()
    c.update(b)
    return c


a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}
print(merge_two_dicts(a, b))


# 在Python3.5以上版本中
def merge_dictionaries(a, b):
    return {**a, **b}


# 20.将两个列表转化为字典
def to_dictionary(keys, vals):
    return dict(zip(keys, vals))


keys = ["a", "b", "c"]
values = [2, 3, 4]
print(to_dictionary(keys, values))


# 21.使用枚举
lst1 = ['a', 'b', 'c', 'd']
for index, element in enumerate(lst1):
    print('value', element, 'index', index)


# 22.执行时间
start_time = time.time()
a = 1
b = 2
c = a + b
print(c)
end_time = time.time()
total_time = end_time - start_time
print('Time: ', total_time)


# 23.Try else
try:
    2 * 3
except TypeError:
    print("An exception was raised")
else:
    print("Thank God, no exceptions were raised")


# 24.元素频率
def most_frequent(lst):
    return max(set(lst), key=lst.count)  # 选取最常见的元素


# 25.回文序列
def palindrome(string):
    pass


# 26.不使用if-else的计算子
action = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv,
    '*': operator.mul,
    '**': pow,
}
print(action['-'](50, 25))  # 25


# 27.Shuffle
def shuffle(lst):
    temp_lst = deepcopy(lst)
    m = len(temp_lst)
    while m:
        m -= 1
        i = randint(0, m)
        temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
    return temp_lst


# 28.交换值
a, b = b, a


# 29.字典默认值
d = {'a': 1, 'b': 2}
d.get('c', 3)
