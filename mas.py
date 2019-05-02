import urllib
import urllib.request
import http.cookiejar
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup
cookie = http.cookiejar.CookieJar()
handler=urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

login = False

def get_content(user_var, pwd_var):
    url = 'https://www.medanswering.com/login.taf?_function=check'
    user_name = user_var
    pwd = pwd_var
    # print (user_name)
    # print (pwd)
    referer = 'https://www.medanswering.com/login.taf'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    values = { 'User_Name' : user_name, 'Password' : pwd, 'eulaAgree' : 1}
    headers = { 'User-Agent' : user_agent , 'Referer' : referer}
    data = urllib.parse.urlencode(values).encode("utf-8")

    # session = requests.Session()

    result = opener.open(url, data = data)
    status = result.getcode()


    # url_TPCL = 'https://www.medanswering.com/admintransproviders.taf?_function=listselfproviders&'
    url_temp = 'https://www.medanswering.com'
    url_next = 'https://www.medanswering.com/admintransproviders.taf?_function=listselfproviders&'
    content_next = opener.open(url_next).read().decode('utf-8','ignore')
    soup = BeautifulSoup(content_next, 'lxml')
    element = soup.find('td', text=re.compile(".*?NYC"))
    # print(element)
    url_NYC = url_temp + element.find_previous_sibling('td').a['href']

    # url_NYC = 'https://www.medanswering.com/admintransproviders.taf?_function=detail&Provider_ID=31462'

    result = opener.open(url_NYC)
    content = result.read().decode('utf-8','ignore')
    # print content
    return content



def get_excel(content):
    soup=BeautifulSoup(content, 'lxml')
    table_result = soup.find_all('table')

    drivers = ''
    vehicles = ''
    for table in table_result:
        if table.font != None:
            if table.font.string != None:
                if table.font.string.startswith('Drivers'):
                    drivers = table
                if table.font.string.startswith('Vehicles'):
                    vehicles = table

    if drivers == '' and vehicles == '':
        global login
        login = False
        return False

    login = True

    pattern = re.compile('<tr.*?<td.*?<a.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?</tr>', re.S)
    items = re.findall(pattern, str(drivers))
    # print items
    d1 = []
    d2 = []
    d3 = []
    d4 = []
    d5 = []
    i = 0
    for item in items:
        if i == 0:
            i = -1
            continue
        d1.append(item[0].strip())
        d2.append(item[1].strip())
        d3.append(item[2].strip())
        d4.append(item[3].strip())
        d5.append(item[4].strip())



    df = pd.DataFrame(data = {'Status': d1, 'Last Name': d2, 'First Name': d3, 'MID': d4, 'Expiration': d5}, columns = ['Status', 'Last Name',
    'First Name', 'MID', 'Expiration'])
    # print df
    df.to_excel('drivers.xlsx', sheet_name='sheet1', index=False, encoding = 'utf8')



    pattern = re.compile('<tr.*?<td.*?<a.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?</tr>', re.S)
    items = re.findall(pattern, str(vehicles))
    # print items
    d1 = []
    d2 = []
    d3 = []
    d4 = []
    d5 = []
    i = 0
    for item in items:
        if i == 0:
            i = -1
            continue
        d1.append(item[0].strip())
        d2.append(item[1].strip())
        d3.append(item[2].strip())
        d4.append(item[3].strip())
        d5.append(item[4].strip())


    df2 = pd.DataFrame(data = {'Status': d1, 'Vehicle Type': d2, 'Vehicle Name': d3, 'License Plate Number': d4, 'Expiration': d5}, columns = ['Status', 'Vehicle Type', 'Vehicle Name', 'License Plate Number', 'Expiration'])
    # print df2
    df2.to_excel('vehicles.xlsx', sheet_name='sheet1', index=False, encoding = 'utf8')
    return True


def get_correction(user_var, pwd_var):
    global login
    if login == False:
        url = 'https://www.medanswering.com/login.taf?_function=check'
        # user_name = "operr126"
        # pwd = "Hawkins2@"
        values = { 'User_Name' : user_var, 'Password' : pwd_var, 'eulaAgree' : 1}
        # data = urllib.urlencode(values)
        # opener.open(url, data)
        data = urllib.parse.urlencode(values).encode("utf-8")

        # session = requests.Session()

        opener.open(url, data = data)

    # _UserReference = ""
    # for item in cookie:
    #     if item.name == "TeraScript_UserReference":
    #         _UserReference = item.value
            # print item.value

    # print(cookie)

    url_main = "https://www.medanswering.com"

    url_correction="https://www.medanswering.com/admincorrectionrequests.taf?_function=transproviderlist&"
    result = opener.open(url_correction)
    # print(result.read())

    content = result.read().decode('utf-8','ignore')
    # print(content)
    d1 = []
    d2 = []
    d3 = []
    d4 = []
    d5 = []
    d6 = []
    d7 = []
    d8 = []
    d9 = []

    soup = BeautifulSoup(content, 'lxml')
    element = soup.find('input', attrs={'type': "SUBMIT", 'value': re.compile("Next.*?Matches")})
    # print element

    pattern = re.compile('<tr.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?<a.*?>(.*?)</a>.*?</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?</tr>', re.S)


    items = re.findall(pattern, content)
    i = 0
    for item in items:
        if i == 0:
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

        # print(item[0].strip(), item[1].strip(), item[2].strip(), item[3].strip(), item[4].strip(), item[5].strip(), item[6].strip(), item[7].strip(), item[8].strip())


    while element != None:
        # print(element.parent)
        next = element.parent
        # print(next,'=================')
        url_next = url_main + next['action']
        print(url_next)
        result = opener.open(url_next)
        content = result.read().decode('utf-8','ignore')
        soup = BeautifulSoup(content, 'lxml')
        element = soup.find('input', attrs={'type': "SUBMIT", 'value': re.compile("Next.*?Matches")})
        # print(element)


        pattern = re.compile('<tr.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?<a.*?>(.*?)</a>.*?</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?</tr>', re.S)
        items = re.findall(pattern, content)

        i = 0
        for item in items:
            if i == 0:
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

            # print(item[0].strip(), item[1].strip(), item[2].strip(), item[3].strip(), item[4].strip(), item[5].strip(), item[6].strip(), item[7].strip(), item[8].strip())


    df = pd.DataFrame(data = {'Request Date': d1, 'Correction Requested': d2, 'Status': d3, 'Outome':d4, 'Explanation': d5, 'Completion Date': d6, 'Invoice Number': d7, 'County': d8, 'Service Start Date': d9}, columns = ['Request Date', 'Correction Requested', 'Status', 'Outome', 'Explanation', 'Completion Date', 'Invoice Number', 'County', 'Service Start Date'])
    # print df
    if df.shape[0] == 0:
        return False
    df.to_excel('corrections.xlsx', sheet_name='sheet1', index=False, encoding = 'utf8')
    return True
    # url_next = next.form.action



import tkinter
from tkinter import messagebox



if __name__ == "__main__":
    ui = tkinter.Tk()
    ui.geometry('450x380')
    ui.configure(background='light green')
    L1 = tkinter.Label(ui, text="user")
    L1.place(x = 50, y = 50)
    user_name = tkinter.StringVar()
    user_name.set("jrodriguez219")
    E1 = tkinter.Entry(ui, width=30, textvariable = user_name)
    E1.place(x = 150, y = 50)

    L2 = tkinter.Label(ui, text="password")
    L2.place(x = 50, y = 150)
    pwd = tkinter.StringVar()
    pwd.set("Newbell1234#")
    E2 = tkinter.Entry(ui, width=30, textvariable = pwd)
    E2.place(x = 150, y = 150)

    def butt_data():
        # print (user_name.get())
        content = get_content(user_name.get(), pwd.get())
        # print (content)
        if content == None:
            messagebox.showerror('Error 01','Cannot connect to server')
        else:
            if get_excel(content):
                messagebox.showinfo('Success','Get all the data')
            else:
                messagebox.showerror('Error 02','Cannot get data')

    def butt_correction():
        content = get_correction(user_name.get(), pwd.get())
        if content == True:
            messagebox.showinfo('Success','Get all the data')
        else:
            messagebox.showerror('Error','Cannot get data')

    button = tkinter.Button(ui, text = 'get drivers & vehicles data', command = butt_data)
    button.place(x = 130, y = 250)

    button2 = tkinter.Button(ui, text = 'get correction', command = butt_correction)
    button2.place(x = 130, y = 300)

    ui.mainloop()
