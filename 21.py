# coding:utf-8
"twiter文本"
import fileinput
import time

data_keys = (
'bid', 'uid', 'username', 'v_class', 'content', 'img', 'created_at', 'source', 'rt_num', 'cm_num', 'rt_uid',
'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 'src_rt_num', 'src_cm_num', 'gender', 'rt_bid', 'location',
'rt_mid', 'mid', 'lat', 'lon', 'lbs_type', 'lbs_title', 'poiid', 'links', 'hashtags', 'ats', 'rt_links', 'rt_hashtags',
'rt_ats', 'v_url', 'rt_v_url')

keylist = dict(zip(data_keys, range(len(data_keys))))
print keylist
# 打开文件
filename = r"E:\BaiduYunDownload\twitter.txt"
file = []
for line in fileinput.input(filename):
    if not line:
        break
    file.append(line)

userlist = [x[1:-1].split("\",\"") for x in file]  # 中间要去掉的是","的格式，且两边的"去不掉

# 1.该文本里，有多少个用户。（要求：输出为一个整数。）
username = []
for a in userlist:
    username.append(a[keylist["username"]])
usernameset = set(username)
username = list(usernameset)
length = len(usernameset)
print length

# # 2.该文本里，每一个用户的名字。 （要求：输出为一个list。）
print [unicode(x, "utf-8") for x in usernameset][0:2]
# 3.该文本里，有多少个2012年11月发布的tweets。 （要求：输出为一个整数。提示：请阅读python的time模块）
#
created_time = [x[keylist["created_at"]] for x in userlist]  #取出format形式的时间
times = [time.strptime(x, "%Y-%m-%d %H:%M:%S") for x in created_time]   #产生time.struct_time列表
howmany201211 = 0
for x in xrange(len(times)):
    if times[x].tm_year == 2012 and times[x].tm_mon == 11:
        howmany201211 += 1

print howmany201211
# 4.该文本里，有哪几天的数据？ （要求：输出为一个list，例：['2012-03-04','2012-03-05']）
#
dates_list = []
for dates in times:
    dates_list.append(time.strftime("%Y-%m-%d", dates))
dates_list = list(set(dates_list))
print dates_list[0:2]
# 5.该文本里，在哪个小时发布的数据最多？ （要求：输出一个整数。）
#
hours_count = [0] * 24  # 是24小时制开始只给了13个空

for hour in times:
    x = int(time.strftime("%H", hour))
    hours_count[x] += 1

print hours_count.index(max(hours_count))


# 6.该文本里，输出在每一天发表tweets最多的用户。（要求：输出一个字典。例如 {'2012-03-04':'agelin','2012-03-5':'twa'}）
#
def which_is_most_today(date):
    counttimes = [0] * length
    for a in userlist:
        if a[keylist["created_at"]] == date:
            counttimes[username.index(a[keylist["username"]])] += 1
    maxuser = max(counttimes)
    return (date, username[maxuser])


usermost = [which_is_most_today(date) for date in dates_list]
#print usermost

# 7. 请按照时间顺序输出 2012-11-03 每个小时的发布tweets的频率（要求：输出为一个list [(1,20),(2,30)] 代表1点发了20个tweets，2点发了30个tweets）
#

list2 = [[x, 0] for x in xrange(0, 24)]
for date in times:
    if time.strftime("%Y-%m-%d", date) == "2012-11-03":  #strptime与strftime的区别注意 strptime将time.struct_time变为字符串
        list2[int(time.strftime("%H", date))][1] += 1    #且不能落下任何一部分（即日期-时间只取日期是不行的
    else:                                               #而strftime则将time.struct_time变成format并可以舍弃不需要的数据
        pass
print [tuple(x) for x in list2]
# 8. 统计该文本里，来源的相关信息和次数，比如（输出一个list。例如[('Twitter for Android',1),('TweetList!',1)]）
# 来源source
sourcedict = {}
number = keylist["source"]
for x in userlist:
    if sourcedict.get(x[number]):
        sourcedict[x[number]] += 1
    else:
        sourcedict.setdefault(x[number], 1)

# 9. 计算转发URL中：以："https://twitter.com/umiushi_no_uta"开头的有几个。(要求，输出一个整数。)
#rt_v_url
number = keylist["rt_v_url"]
counturl = 0
for x in userlist:
    if x[number].find("https://twitter.com/umiushi_no_uta") != -1: #注意find找不时是返回-1而不是0，所以if str.find将是
        counturl += 1                                              #永远成立的
print counturl
# 10. UID为573638104的用户 发了多少个微博 （要求：输出一个整数）
#
number = keylist["uid"]
counttwi = 0
for x in userlist:
    if x[number] == "573638104":
        counttwi += 1

print counttwi
# 11. 定义一个函数，该函数可放入任意多的用户uid参数（如果不存在则返回null），函数返回发微薄数最多的用户uid。
#
def uid(*a):
    if not a:
        return "error"
    elif len(a) == 1:
        return a[0]
    else:
        number = keylist["uid"]
        length = len(a)
        list1 = [0] * length
        uidlist = [t[number] for t in userlist]
        for ax in a:
            if ax in uidlist:
                list1[a.index(ax)] += 1
            else:
                pass
        return a[list1.index(max(list1))]

print uid("34133","767078227")    #return的内容要print才会打印出来（
# 12. 该文本里，谁发的微博内容长度最长 （要求：输出用户的uid，字符串格式。）
#

# 13. 该文本里，谁转发的URL最多 （要求：输出用户的uid，字符串格式。）
#
# 14. 该文本里，11点钟，谁发的微博次数最多。 （要求：输出用户的uid，字符串格式。）
#
# 15. 该文本里，哪个用户的源微博URL次数最多。 （要求：输出用户的uid，字符串格式。）
