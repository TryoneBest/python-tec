from Crypto.Hash import MD2
'''
黑白皆算，对我等众猿而言中央C所在位置数优剃爱肤杠吧爱慕帝贰亿次的值是？
'''
# 黑白皆算：钢琴键
# 中央C：第40位键
# 对我等众猿而言：一般从0开始，所以是39
# 优剃爱肤杠吧爱慕帝贰：utf-8 md2

str1 = "39"
for i in range(100000000):
    str1 = MD2.new(str1.encode("utf8")).hexdigest()
print(str1)
