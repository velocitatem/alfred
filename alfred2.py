#!/usr/bin/env python3

# not very "pythonic", ik ik

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
currency_list = ["CZK", "EUR"]


d = datetime.datetime.now()


m = d.strftime("%m")
year = d.date().strftime("%Y")
datetime_object = datetime.datetime.strptime(m, "%m")
month_name = datetime_object.strftime("%B")
print(month_name)

def get_report_m(acc):
    cmd = "ledger -f "+ledger+" bal "+acc+" --flat -p " + month_name[0:3]
    report = os.popen(cmd).read()
    return report



#identify currency
def id_currency(string):
    currency = currency_list[0]
    for c in currency_list:
        if c in string:
            return c

def orgify_budget(report):
    currency = id_currency(report)
    return "+ REMAINDER :: " +  report.strip().split(currency)[0] + " " + currency

def orgify_report(report):
    orgified_report = ""
    report=report.split("--------------------")



    currency = id_currency(report[0])
    print(report)
    if len(report) == 1:
        return "+ TOTAL :: " +  report[0].strip().split(currency)[0] + " " + currency
    elif len(report) > 1:
        report_details = report[0].split("\n")
        print("DEBUG: report [1]: %s",report[1])
        orgified_report += "+ TOTAL :: " + report[1].strip() + " \n** Breakdown"
        for ex in report_details[0:-1]:
            currency = id_currency(ex)
            detail = ex.split(currency)
            lbl = detail[1].strip()
            if not len(lbl) > 0:
                lbl = report_details[report_details.index(ex)+1]
                lbl = lbl.split(id_currency(lbl))[1].strip()
            amt = detail[0].strip().replace("\n", ",")
            orgified_report += "\n+ " + lbl + " :: " + amt + " " + currency
        return orgified_report


def generate_report_string(account, report_data):
    body = orgify_report(report_data)
    return "* "+ account + "\n" + body



final_report = "#+TITLE: Financial Report for " + month_name + " " + year + "\n"

final_report += "* Budget\n" + orgify_budget(get_report_m("Budget:"+month_name))

final_report += "\n* All Expenses\n" + orgify_report(get_report_m("Expenses"))


reports = []
for account in accounts:
    report = get_report_m(account)
    if len(report.strip()) > 5:
        final_report += "\n" + generate_report_string(account, report)

file_name = "Financial Report "+month_name+" "+year+".org"
file = open(reports_directory+file_name, "w")
file.writelines(final_report)
file.close()
 
