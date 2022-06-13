"""
序列: 是指他的成员都是有序排列，并且可以通过下标偏移量访问到他的一个或几个成员
1.字符串 "abcd"
2.列表 [0, "abcd"]
3.元组 ("abc", "def")


"""

# 记录生肖，根据年份来判断生肖
# 字符串的基本操作
chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"

# 1、切片
print(chinese_zodiac[0:4])
print(chinese_zodiac[-1])

# year = 2018

# year = int(input("请用户输入年份: "))
#
#
#
# print(year % 12)
#
# print(chinese_zodiac[year % 12])
#
# # 2、成员关系操作符号
# print('牛' not in chinese_zodiac)
# print('牛' in chinese_zodiac)
#
# # 3、连接操作符
# print(chinese_zodiac + 'abcd')
#
# # 4、 重复操作符
# print(chinese_zodiac * 2)


for cz in chinese_zodiac:
    print(cz)

for i in range(1, 13):
    print(i)


for year in range(2000, 2020):
    print('{}年的生肖是{}'.format(year, chinese_zodiac[year % 12]))