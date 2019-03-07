import urllib
import urllib2
import cookielib
import re
from bs4 import BeautifulSoup

cookie = cookielib.CookieJar()
handler=urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

# url = 'https://www.medanswering.com/login.taf?_function=check'
# user_name = 'operr126'
# pwd = 'Hawkins1@'
# referer = 'https://www.medanswering.com/login.taf'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# values = { 'User_Name' : user_name, 'Password' : pwd, 'eulaAgree' : 1}
# headers = { 'User-Agent' : user_agent , 'Referer' : referer}
# data = urllib.urlencode(values)
# result = opener.open(url, data)
# status = result.getcode()
#
# url_TPCL = 'https://www.medanswering.com/admintransproviders.taf?_function=listselfproviders&'
# url_NYC = 'https://www.medanswering.com/admintransproviders.taf?_function=detail&Provider_ID=31462'
#
# result = opener.open(url_NYC)
# content = result.read()

content = '<tr valign="top" bgcolor="#F7F3FF"> <td align="center" style="font-family: Arial; font-size: 11;"> 12/10/18 </td> <td> please update on PA number, thanks. </td> <td> Completed </td> <td> Updated Med Provider Info. </td> <td> </td> <td align="center"> 12/19/2018 08:08 AM </td> <td align="center"> <a href="/admintrips.taf?_function=detail&Trip_Auth_ID=68455411">684554110</a> </td> <td> NYC </td> <td align="center"> 11/15/2018 </td> </tr> <tr valign="top" bgcolor="#F7F3FF"> <td align="center" style="font-family: Arial; font-size: 11;"> 12/10/18 </td> <td> please update on PA number, thanks. </td> <td> Completed </td> <td> Updated Med Provider Info. </td> <td>'
url = 'https://www.medanswering.com/login.taf?_function=check'
user_name = "operr126"
pwd = "Hawkins2@"
values = { 'User_Name' : user_name, 'Password' : pwd, 'eulaAgree' : 1}
data = urllib.urlencode(values)
opener.open(url, data)
# url_correction="https://www.medanswering.com/admincorrectionrequests.taf?_function=transproviderlist&"
# result = opener.open(url_correction)
url = 'https://www.medanswering.com/admincorrectionrequests.taf?_function=transproviderlist&_start=001'
result = opener.open(url)
content = result.read()

soup = BeautifulSoup(content, 'lxml')
table_corr = soup.find('table', attrs={'border': "0", 'cellspacing': "1", 'cellpadding': "3"})
# corrs = table_corr.findChildren('tr')
print(table_corr)
pattern = re.compile('<tr.*?>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?<a.*?>(.*?)</a>.*?</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?</tr>', re.S)


d1 = []
d2 = []
d3 = []
d4 = []
d5 = []
d6 = []
d7 = []
d8 = []
d9 = []
items = re.findall(pattern, content)
print len(items)
i = 0
for item in items:

    if i == 0:
        # for i in range(9):
        #     print i, '+++++++++', item[i]
        i = -1
        continue

    d1.append(item[0].strip())
    d2.append(item[1].strip())
    d3.append(item[2].strip())
    d4.append(item[3].strip())
    d5.append(item[4].strip())
    d6.append(item[5].strip())
    d7.append(item[6].strip())
    d8.append(item[7].strip())
    d9.append(item[8].strip())

# print(d7)
