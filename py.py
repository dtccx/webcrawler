import urllib
import urllib.request
import http.cookiejar
import re
from urllib.request import Request
import requests
import pandas as pd
from bs4 import BeautifulSoup
import pymongo
import tkinter
from tkinter import messagebox

# connect to database
client = pymongo.MongoClient(host='localhost', port=27017)

def get_excel1(user_name, pwd, time1, time2):
    url='https://www.medanswering.com/menu.taf?menu=Medicaid&'
    #'https://www.medanswering.com/detailed_destination_report.taf?&'

    cookie = http.cookiejar.CookieJar()
    handler=urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)

    url = 'https://www.medanswering.com/login.taf?_function=check'
    # user_name = 'jrodriguez219'
    # pwd = 'Newbell1234#'
    referer = 'https://www.medanswering.com/login.taf'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    values = { 'User_Name' : user_name, 'Password' : pwd, 'eulaAgree' : 1}
    headers = { 'User-Agent' : user_agent , 'Referer' : referer}
    data = urllib.parse.urlencode(values).encode("utf-8")

    # session = requests.Session()

    result = opener.open(url, data = data)

    # payload = {'medicaid_county_number': 66, 'dob_op': '>=','date_range_start': '05/01/2019','date_range_end': '05/02/2019','payment_date_op': '>=','from_city_op': 'LIKE%','from_street_op': 'LIKE%','to_city_op': 'LIKE%','to_street_op': 'LIKE%','trans_prov_all_counties': '1','Trip_Status': 'Eligible','Trip_Status': 'Ineligible/Proceed','columns': 'Date','columns': 'Status','columns': 'Invoice','columns': 'Pick-up Time','columns': 'Drop-off Time','columns': 'Pick-up Address','columns': 'Destination Address','columns': 'Estimated Trip Mileage','columns': 'Transportation Type','columns': 'Transportation Provider','Sort': 'From_Street','_function': 'detaileddestinationreport','Submit': 'Submit'}

    url_destination = 'https://www.medanswering.com/detailed_destination_report.taf?&'
    # data2 = urllib.parse.urlencode(payload).encode("utf-8")

    dic2 = {'End_Effective_Date':time2}
    dic1 = {'Start_Effective_Date':time1}
    temp1 = 'Invoice_Number=&Medicaid_County_Number=&Status=&PA_Submission_Result=&Correction_Status=&Changed_Since_Vendor_Notified=&Exported=&Medicaid_Number=&First_Name=&Last_Name=&Start_DOB=&Standing_Order=&Part_of_Split_Series=&Printed=&Transport_Type_ID=&'
    temp2 = '&'
    temp3 = '&Start_Service_End=&End_Service_End=&Start_Date_Exported=&End_Date_Exported=&Sort_By=Service_Starts_Oldest_to_Newest&_function=list'
    data_trip_2 = temp1 + urllib.parse.urlencode(dic1).encode("utf-8").decode() + temp2 + urllib.parse.urlencode(dic2).encode("utf-8").decode() + temp3
    url_trip = 'https://www.medanswering.com/admintrips.taf?&'
    url_main = 'https://www.medanswering.com'


    data_trip = data_trip_2.encode()

    r = opener.open(url_trip, data_trip)
    content = r.read().decode()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    element = soup.find('b', text='Export Roster')
    url_export = url_main + element.parent['href']
    # print(url_export)


    r2 = opener.open(url_export)
    content2 = r2.read().decode()
    soup2 = BeautifulSoup(content2, 'lxml')
    element = soup2.find('a', text='Download Roster Export')
    url_text = url_main + element['href']

    res = opener.open(url_text)
    # print(res.read().decode())

    text = res.read().decode()
    data = pd.read_csv(text, sep="\t", header=None)
    data.columns = ["", "recipiendId", "Recipient Name", "YOB", "Sex", "invoiceNumber", "priorApprovalNumber ", "Item Code", "Item Code Mod", "serviceStarts", "Service Ends", "Approved To", "orderingProvider", "amt", "Qty", "Days/Times", "C D A"]
    data = data.drop([0])
    # print(data)
    records = json.loads(data.T.to_json()).values()
    # client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.billing
    collection = db.totalJobExcel
    collection.insert(records)
    return True

# print(element.parent.a['href'])
# url_NYC = url_temp + element.find_previous_sibling('td').a['href']

def get_excel2():
    url='https://www.medanswering.com/menu.taf?menu=Medicaid&'
    #'https://www.medanswering.com/detailed_destination_report.taf?&'

    cookie = http.cookiejar.CookieJar()
    handler=urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)

    url = 'https://www.medanswering.com/login.taf?_function=check'
    user_name = 'jrodriguez219'
    pwd = 'Newbell1234#'
    referer = 'https://www.medanswering.com/login.taf'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    values = { 'User_Name' : user_name, 'Password' : pwd, 'eulaAgree' : 1}
    headers = { 'User-Agent' : user_agent , 'Referer' : referer}
    data = urllib.parse.urlencode(values).encode("utf-8")

    # session = requests.Session()

    result = opener.open(url, data = data)

    payload = {'medicaid_county_number': '66', 'county_of_residence':'','medical_reason':'','medicaid_number':'','quant_trips_approved':'','dob_op': '>=','dob':'','Coverage_Code':'','date_range_start': '05/01/2019','date_range_end': '05/02/2019','payment_date_op': '>=','payment_date':'','from_zips':'','from_medicaid_county_number':'','from_city_op': 'LIKE%','from_city':'','from_street_op': 'LIKE%','from_street':'','to_zips':'','to_medicaid_county_number':'','to_city_op': 'LIKE%','to_city':'','to_street_op':'LIKE%','to_street':'','trans_prov_all_counties': '1','standing_order':'','part_of_split_series':'','Trip_Status': 'Eligible','Trip_Status': 'Ineligible/Proceed','columns': 'Date','columns': 'Status','columns': 'Invoice','columns': 'Pick-up Time','columns': 'Drop-off Time','columns': 'Pick-up Address','columns': 'Destination Address','columns': 'Estimated Trip Mileage','columns': 'Transportation Type','columns': 'Transportation Provider','Sort': 'From_Street','_function': 'detaileddestinationreport','Submit': 'Submit'}

    # data = HTTPHeaderDict()

    payload2 = 'medicaid_county_number=66&county_of_residence=&medical_reason=&medicaid_number=&quant_trips_approved=&dob_op=%3E%3D&dob=&Coverage_Code=&date_range_start=05%2F01%2F2019&date_range_end=05%2F03%2F2019&payment_date_op=%3E%3D&payment_date=&from_zips=&from_medicaid_county_number=&from_city_op=LIKE%25&from_city=&from_street_op=LIKE%25&from_street=&to_zips=&to_medicaid_county_number=&to_city_op=LIKE%25&to_city=&to_street_op=LIKE%25&to_street=&trans_prov_all_counties=1&standing_order=&part_of_split_series=&Trip_Status=Eligible&Trip_Status=Ineligible%2FProceed&columns=Date&columns=Status&columns=Invoice&columns=Pick-up+Time&columns=Drop-off+Time&columns=Pick-up+Address&columns=Destination+Address&columns=Estimated+Trip+Mileage&columns=Transportation+Type&columns=Transportation+Provider&Sort=From_Street&_function=detaileddestinationreport&Submit=Submit'

    # 'medicaid_county_number=66&county_of_residence=&medical_reason=&medicaid_number=&quant_trips_approved=&dob_op=%3E%3D&dob=&Coverage_Code=&date_range_start=05%2F01%2F2019&date_range_end=05%2F02%2F2019&payment_date_op=%3E%3D&payment_date=&from_zips=&from_medicaid_county_number=&from_city_op=LIKE%25&from_city=&from_street_op=LIKE%25&from_street=&to_zips=&to_medicaid_county_number=&to_city_op=LIKE%25&to_city=&to_street_op=LIKE%25&to_street=&trans_prov_all_counties=1&standing_order=&part_of_split_series=&Trip_Status=Eligible&Trip_Status=Ineligible%2FProceed&columns=Transportation+Provider&Sort=From_Street&_function=detaileddestinationreport&Submit=Submit'
    data2 = payload2.encode()
    r = opener.open(url_destination, data = data2)
    print(r.read().decode())

import json

if __name__ == "__main__":
    ui = tkinter.Tk()
    ui.geometry('900x480')
    ui.configure(background='light green')
    L1 = tkinter.Label(ui, text="From:(MM/DD/YYYY)")
    L1.place(x = 100, y = 200)
    time1 = tkinter.StringVar()
    time1.set("05/01/2019")
    E1 = tkinter.Entry(ui, width=30, textvariable = time1)
    E1.place(x = 100, y = 250)

    L2 = tkinter.Label(ui, text="To:(MM/DD/YYYY)")
    L2.place(x = 450, y = 200)
    time2 = tkinter.StringVar()
    time2.set("05/03/2019")
    E2 = tkinter.Entry(ui, width=30, textvariable = time2)
    E2.place(x = 450, y = 250)

    # drop down list
    OPTIONS = {}
    db = client.billing
    collection = db.collection
    result = collection.find({'userName': {'$ne': None}})
    for x in result:
        OPTIONS[x['userName']] = x['password']


    variable = tkinter.StringVar(ui)
    # variable.set(OPTIONS[0].key) # default value

    w = tkinter.OptionMenu(ui, variable, *OPTIONS.keys())
    w.pack()
    w.configure(width = 15)
    w.place(x = 400, y = 50)

    def ok():
        usrname = variable.get()
        pwd = OPTIONS.get(variable.get())
        # print(usrname, pwd)
        ok = get_excel1(usrname, pwd, time1.get(), time2.get())
        if ok == True:
            messagebox.showinfo('Success','Insert all the data')
        else:
            messagebox.showerror('Error','Error')



    button = tkinter.Button(ui, text="OK", command=ok)
    button.pack()
    button.place(x = 400, y = 100)


    # def butt_data():
    #     # print (user_name.get())
    #     content = get_content(user_name.get(), pwd.get())
    #     # print (content)
    #     if content == None:
    #         messagebox.showerror('Error 01','Cannot connect to server')
    #     else:
    #         if get_excel(content):
    #             messagebox.showinfo('Success','Get all the data')
    #         else:
    #             messagebox.showerror('Error 02','Cannot get data')
    #
    # def butt_correction():
    #     content = get_correction(user_name.get(), pwd.get())
    #     if content == True:
    #         messagebox.showinfo('Success','Get all the data')
    #     else:
    #         messagebox.showerror('Error','Cannot get data')
    #
    # button = tkinter.Button(ui, text = 'get drivers & vehicles data', command = butt_data)
    # button.place(x = 130, y = 250)
    #
    # button2 = tkinter.Button(ui, text = 'get correction', command = butt_correction)
    # button2.place(x = 130, y = 300)

    ui.mainloop()
