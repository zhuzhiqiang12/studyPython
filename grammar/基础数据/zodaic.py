# zodiac_name = ("摩羯座", "水瓶座", "双鱼座", "白羊座", "金牛座", "双子座", "巨蟹座",
#                "狮子座", "处女座", "天秤座", "天蝎座", "射手座")
#
# zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23),
#               (9, 23), (10, 23), (11, 23), (12, 23))
#
# (month, days) = (2, 15)
#
# zodiac_days = filter(lambda x: x <= (month, days), zodiac_days)
# print(zodiac_days)
# zodiac_len = len(list(zodiac_days)) % 12
# print(zodiac_name[zodiac_len])

a_list = ['abc', 'xyz']

a_list.append('CV')
print(a_list)
a_list.remove('xyz')
print(a_list)