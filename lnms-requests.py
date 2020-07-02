import re
import json
import requests
import xlsxwriter

url = "https://ow-lnms01.int/api/v0/devices"

headers = {
    "Authorization": "Bearer 88f275fbf13a65a95dc17ee7c400ff41",
    "cache-control": "no-cache",
    "Postman-Token": "92fcc6c3-0825-411a-95b0-ca1e67139161",
}

response = requests.request("GET", url, headers=headers, verify=False)

workbook = xlsxwriter.Workbook("C:\\Scripts\\DevNet\\fcc-switches.xlsx")
worksheet = workbook.add_worksheet()

response_dict = json.loads(response.text)

row = 1
col = 0

bold = workbook.add_format({'bold': True})

worksheet.write("A1", "HOST", bold)
worksheet.write("B1", "OS", bold)
worksheet.write("C1", "VERSION", bold)
worksheet.write("D1", "HARDW", bold)

for i in range(len(response_dict["devices"])):
    hostname = response_dict["devices"][i]["hostname"]
    os = response_dict["devices"][i]["os"]
    os_version = response_dict["devices"][i]["version"]
    hardware = response_dict["devices"][i]["hardware"]
    worksheet.write(row, col, hostname)
    worksheet.write(row, col + 1, os)
    worksheet.write(row, col + 2, os_version)
    worksheet.write(row, col + 3, hardware)
    row += 1

workbook.close()
