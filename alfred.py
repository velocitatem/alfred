#!/usr/bin/env python3

import os
import datetime
import requests
import pyfiglet

accounts = [
    "Food",
    "Drink",
    "Fun",
    "Medical",
    "School"
]

ledger = "~/Documents/Me/Finance/my.ledger"
reports_directory = "/home/velo/Documents/Me/Finance/reports/"


d = datetime.datetime.now()


m = d.strftime("%m")
year = d.date().strftime("%Y")
datetime_object = datetime.datetime.strptime(m, "%m")
month_name = datetime_object.strftime("%b")

def get_report_m(acc):
    cmd = "ledger -f "+ledger+" bal "+acc+" --flat -p " + month_name[0:3]
    report = os.popen(cmd).read()
    return report

def generate_report_string(account, report_data):
    title = pyfiglet.figlet_format(account, font="big")
    body = report_data
    return title + "\n" + body



final_report = ""

title_font = "big"
final_report += pyfiglet.figlet_format("Financial", font=title_font) + "\n" + pyfiglet.figlet_format("Report", font=title_font)
final_report += "\n\n" + month_name + " " + year + "\n\n\n\n\n\n\n\n"

reports = []
for account in accounts:
    report = get_report_m(account)
    if len(report.strip()) > 5:
        final_report += "\n" + generate_report_string(account, report)

file_name = "Financial Report "+month_name+" "+year
file = open(reports_directory+file_name, "w")
file.writelines(final_report)
file.close()
