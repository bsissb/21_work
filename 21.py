# coding:utf-8
"twiter文本"

data_keys = ('bid', 'uid', 'username', 'v_class', 'content', 'img', 'created_at', 'source', 'rt_num', 'cm_num', 'rt_uid', 'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 'src_rt_num', 'src_cm_num', 'gender', 'rt_bid', 'location', 'rt_mid', 'mid', 'lat', 'lon', 'lbs_type', 'lbs_title', 'poiid', 'links', 'hashtags', 'ats', 'rt_links', 'rt_hashtags', 'rt_ats', 'v_url', 'rt_v_url')

# 打开文件
filename = r"E:\BaiduYunDownload\twitter.txt"
readfile = open(filename)
userlist = []
while True:
    line = readfile.readline()
    userlist.append(line)
    if not line:
        break

readdict = [dict(zip(data_keys, users.split(','))) for users in userlist]
print readdict[0]
# 1.该文本里，有多少个用户。（要求：输出为一个整数。）
length = len(userlist)
print length
#
# # 2.该文本里，每一个用户的名字。 （要求：输出为一个list。）
# #
username = set()
for x in range(length):
    username.add(readdict[x]['username'])
print username[3:34]
# 3.该文本里，有多少个2012年11月发布的tweets。 （要求：输出为一个整数。提示：请阅读python的time模块）
#

# 4.该文本里，有哪几天的数据？ （要求：输出为一个list，例：['2012-03-04','2012-03-05']）
#
# 5.该文本里，在哪个小时发布的数据最多？ （要求：输出一个整数。）
#
# 6.该文本里，输出在每一天发表tweets最多的用户。（要求：输出一个字典。例如 {'2012-03-04':'agelin','2012-03-5':'twa'}）
#
# 7. 请按照时间顺序输出 2012-11-03 每个小时的发布tweets的频率（要求：输出为一个list [(1,20),(2,30)] 代表1点发了20个tweets，2点发了30个tweets）
#
# 8. 统计该文本里，来源的相关信息和次数，比如（输出一个list。例如[('Twitter for Android',1),('TweetList!',1)]）
#
# 9. 计算转发URL中：以："https://twitter.com/umiushi_no_uta"开头的有几个。(要求，输出一个整数。)
#
# 10. UID为573638104的用户 发了多少个微博 （要求：输出一个整数）
#
# 11. 定义一个函数，该函数可放入任意多的用户uid参数（如果不存在则返回null），函数返回发微薄数最多的用户uid。
#
# 12. 该文本里，谁发的微博内容长度最长 （要求：输出用户的uid，字符串格式。）
#
# 13. 该文本里，谁转发的URL最多 （要求：输出用户的uid，字符串格式。）
#
# 14. 该文本里，11点钟，谁发的微博次数最多。 （要求：输出用户的uid，字符串格式。）
#
# 15. 该文本里，哪个用户的源微博URL次数最多。 （要求：输出用户的uid，字符串格式。）


readfile.close()
