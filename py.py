import urllib
import urllib.request
import http.cookiejar
import re
from urllib.request import Request
import requests
import pandas as pd
from bs4 import BeautifulSoup

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

# payload = {'medicaid_county_number': 66, 'dob_op': '>=','date_range_start': '05/01/2019','date_range_end': '05/02/2019','payment_date_op': '>=','from_city_op': 'LIKE%','from_street_op': 'LIKE%','to_city_op': 'LIKE%','to_street_op': 'LIKE%','trans_prov_all_counties': '1','Trip_Status': 'Eligible','Trip_Status': 'Ineligible/Proceed','columns': 'Date','columns': 'Status','columns': 'Invoice','columns': 'Pick-up Time','columns': 'Drop-off Time','columns': 'Pick-up Address','columns': 'Destination Address','columns': 'Estimated Trip Mileage','columns': 'Transportation Type','columns': 'Transportation Provider','Sort': 'From_Street','_function': 'detaileddestinationreport','Submit': 'Submit'}

payload = {'medicaid_county_number': '66', 'county_of_residence':'','medical_reason':'','medicaid_number':'','quant_trips_approved':'','dob_op': '>=','dob':'','Coverage_Code':'','date_range_start': '05/01/2019','date_range_end': '05/02/2019','payment_date_op': '>=','payment_date':'','from_zips':'','from_medicaid_county_number':'','from_city_op': 'LIKE%','from_city':'','from_street_op': 'LIKE%','from_street':'','to_zips':'','to_medicaid_county_number':'','to_city_op': 'LIKE%','to_city':'','to_street_op':'LIKE%','to_street':'','trans_prov_all_counties': '1','standing_order':'','part_of_split_series':'','Trip_Status': 'Eligible','Trip_Status': 'Ineligible/Proceed','columns': 'Date','columns': 'Status','columns': 'Invoice','columns': 'Pick-up Time','columns': 'Drop-off Time','columns': 'Pick-up Address','columns': 'Destination Address','columns': 'Estimated Trip Mileage','columns': 'Transportation Type','columns': 'Transportation Provider','Sort': 'From_Street','_function': 'detaileddestinationreport','Submit': 'Submit'}

# data = HTTPHeaderDict()

payload2 = 'medicaid_county_number=66&county_of_residence=&medical_reason=&medicaid_number=&quant_trips_approved=&dob_op=%3E%3D&dob=&Coverage_Code=&date_range_start=05%2F01%2F2019&date_range_end=05%2F03%2F2019&payment_date_op=%3E%3D&payment_date=&from_zips=&from_medicaid_county_number=&from_city_op=LIKE%25&from_city=&from_street_op=LIKE%25&from_street=&to_zips=&to_medicaid_county_number=&to_city_op=LIKE%25&to_city=&to_street_op=LIKE%25&to_street=&trans_prov_all_counties=1&standing_order=&part_of_split_series=&Trip_Status=Eligible&Trip_Status=Ineligible%2FProceed&columns=Date&columns=Status&columns=Invoice&columns=Pick-up+Time&columns=Drop-off+Time&columns=Pick-up+Address&columns=Destination+Address&columns=Estimated+Trip+Mileage&columns=Transportation+Type&columns=Transportation+Provider&Sort=From_Street&_function=detaileddestinationreport&Submit=Submit'

# 'medicaid_county_number=66&county_of_residence=&medical_reason=&medicaid_number=&quant_trips_approved=&dob_op=%3E%3D&dob=&Coverage_Code=&date_range_start=05%2F01%2F2019&date_range_end=05%2F02%2F2019&payment_date_op=%3E%3D&payment_date=&from_zips=&from_medicaid_county_number=&from_city_op=LIKE%25&from_city=&from_street_op=LIKE%25&from_street=&to_zips=&to_medicaid_county_number=&to_city_op=LIKE%25&to_city=&to_street_op=LIKE%25&to_street=&trans_prov_all_counties=1&standing_order=&part_of_split_series=&Trip_Status=Eligible&Trip_Status=Ineligible%2FProceed&columns=Transportation+Provider&Sort=From_Street&_function=detaileddestinationreport&Submit=Submit'

url_destination = 'https://www.medanswering.com/detailed_destination_report.taf?&'
# data2 = urllib.parse.urlencode(payload).encode("utf-8")



data2 = payload2.encode()
r = opener.open(Request(url_destination, data2))
#r = requests.post(url_destination, data = data2)
print(r.read().decode())
